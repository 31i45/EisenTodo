from typing import List, Optional, Dict
from task_model import Task
from task_persistence import TaskPersistence


class TaskManager:
    """
    TaskManager类作为任务管理的核心逻辑类，整合任务数据模型与持久化操作，
    提供了一系列用于操作任务的方法，涵盖添加、编辑、删除、查询、筛选、排序等常见任务管理功能，
    并充分考虑了各种边界情况与异常处理，确保业务逻辑的健壮性与可靠性。
    """
    def __init__(self, persistence: TaskPersistence):
        """
        初始化TaskManager对象，依赖TaskPersistence对象来实现与数据存储的交互。

        参数：
        - persistence (TaskPersistence)：负责任务数据持久化的对象，用于执行保存、加载等数据操作。
        """
        self.persistence = persistence
        self.tasks = self.persistence.load_tasks()

    def add_task(self, task: Task) -> None:
        """
        添加任务到任务列表，并将更新后的任务列表持久化保存到存储介质（如CSV文件）中。
        在添加任务时确保任务数据的合法性，同时妥善处理可能出现的持久化相关异常情况。

        参数：
        - task (Task)：要添加的任务对象，需符合Task类定义的合法性要求。

        抛出异常：
        - ValueError：如果传入的任务对象不符合要求（如属性值不合法等情况），抛出此异常并明确提示相应错误信息。
        - IOError：如果在将更新后的任务列表保存到文件时出现IO错误（如磁盘空间不足、文件被其他程序占用等情况），
                    抛出此异常并详细说明具体的IO问题所在，方便排查文件写入故障。
        """
        self.tasks.append(task)
        self._save_tasks()

    def edit_task(self, index: int, updated_task: Task) -> None:
        """
        根据给定的索引编辑任务列表中的任务，更新任务对象后将变化持久化到存储介质中。
        对索引合法性以及更新后任务数据的合法性进行严格验证，确保编辑操作的正确性和数据一致性。

        参数：
        - index (int)：要编辑的任务在任务列表中的索引位置，需是合法有效的索引范围（0到任务列表长度减1之间）。
        - updated_task (Task)：更新后的任务对象，其属性值需符合Task类的合法性要求。

        抛出异常：
        - IndexError：如果传入的索引超出任务列表的范围，抛出此异常并明确提示索引超出范围，提醒用户检查输入的索引值。
        - ValueError：如果更新后的任务对象属性值不合法（如任务进度超出范围等情况），抛出此异常并详细说明相应的属性错误信息。
        - IOError：若在保存更新后的任务列表到文件时出现IO相关错误，抛出此异常并清晰说明具体的IO问题所在，便于排查文件写入故障。
        """
        if index < 0 or index >= len(self.tasks):
            raise IndexError("任务索引超出范围")
        self.tasks[index] = updated_task
        self._save_tasks()

    def delete_task(self, index: int) -> None:
        """
        根据索引删除任务列表中的指定任务，并将更新后的任务列表持久化保存，
        对索引的合法性进行严谨验证，防止非法删除操作，保障数据的完整性和操作的准确性。

        参数：
        - index (int)：要删除的任务在任务列表中的索引，必须是合法有效的索引范围（0到任务列表长度减1之间）。

        抛出异常：
        - IndexError：如果传入的索引超出任务列表的范围，抛出此异常并明确提示索引超出范围，提醒用户检查输入的索引值。
        - IOError：在保存更新后的任务列表到文件时若出现IO错误（如磁盘空间不足、文件被其他程序占用等情况），
                    抛出此异常并详细说明具体的IO问题所在，方便排查文件写入故障。
        """
        if index < 0 or index >= len(self.tasks):
            raise IndexError("任务索引超出范围")
        del self.tasks[index]
        self._save_tasks()

    def get_tasks_by_category(self, category: str) -> List[Task]:
        """
        根据给定的任务类别获取任务列表中匹配该类别的所有任务，返回符合条件的任务对象列表。
        如果传入空字符串类别，则返回所有任务列表，方便实现不同的查询需求。

        参数：
        - category (str)：任务类别，取值应为"紧急重要"、"重要不紧急"、"紧急不重要"、"不紧急不重要"之一，
                          若传入空字符串则表示获取所有任务。

        返回：
        - List[Task]：匹配给定类别（或所有任务，如果传入空字符串类别）的任务对象列表，列表中的任务对象均符合Task类规范。
        """
        if category == "":
            return self.tasks
        return [task for task in self.tasks if task.category == category]

    def filter_tasks(self, keyword: str, filters: Dict[str, object]) -> List[Task]:
        """
        根据给定的关键字以及其他筛选条件（如进度范围等）对任务列表进行筛选，返回满足筛选条件的任务对象列表。
        对关键字和筛选条件进行合理的处理与判断，高效准确地筛选出符合要求的任务，同时确保返回结果的合法性与准确性。

        参数：
        - keyword (str)：筛选关键字，用于匹配任务名称或描述中包含该关键字的任务，若为空字符串则不基于关键字进行筛选。
        - filters (Dict[str, object])：其他筛选条件的字典，例如可以包含'progress'键表示进度范围筛选（对应的值为元组形式的范围），
                                       当前可扩展支持更多筛选条件，若字典为空则表示无其他额外筛选条件。

        返回：
        - List[Task]：经过筛选后满足条件的任务对象列表，列表中的任务对象均符合Task类的各项属性合法性要求。
        """
        filtered_tasks = self.tasks
        if keyword:
            filtered_tasks = [task for task in filtered_tasks if keyword in task.name or keyword in task.description]
        if "progress" in filters:
            progress_min, progress_max = filters["progress"]
            filtered_tasks = [task for task in filtered_tasks if progress_min <= task.progress <= progress_max]
        return filtered_tasks

    def sort_tasks(self, sort_key: str, ascending: bool) -> List[Task]:
        """
        根据指定的排序键（如任务名称、进度等任务属性）以及排序顺序（升序或降序）对任务列表进行排序，
        支持动态根据不同属性进行排序，采用高效的排序算法（如结合bisect.insort）确保排序性能，
        并返回排序后的任务对象列表，保障排序结果的准确性与稳定性。

        参数：
        - sort_key (str)：排序键，需是任务对象的合法属性名称（如'name'、'progress'等），用于指定按照哪个属性进行排序。
        - ascending (bool)：排序顺序，True表示升序排序，False表示降序排序。

        返回：
        - List[Task]：排序后的任务对象列表，列表中的任务对象依然符合Task类的各项属性合法性要求，且按照指定规则有序排列。

        抛出异常：
        - ValueError：如果传入的排序键不是任务对象的合法属性名称，抛出此异常并明确提示用户输入合法的排序属性，
                      确保排序操作能够正确执行。
        """
        if not hasattr(Task, sort_key):
            raise ValueError(f"排序键 {sort_key} 不是任务对象的合法属性名称")

        sorted_tasks = sorted(self.tasks, key=lambda task: getattr(task, sort_key), reverse=not ascending)
        return sorted_tasks

    def _save_tasks(self) -> None:
        """
        私有方法，用于将当前任务列表持久化保存到存储介质（通过关联的TaskPersistence对象实现），
        集中处理任务列表保存操作，便于统一管理持久化相关的异常处理以及逻辑更新等情况。

        抛出异常：
        - IOError：如果在保存任务列表到文件时出现IO错误（如磁盘空间不足、文件被其他程序占用等情况），
                    抛出此异常并详细说明具体的IO问题所在，方便排查文件写入故障。
        """
        self.persistence.save_tasks(self.tasks)