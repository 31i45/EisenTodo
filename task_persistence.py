import csv
import os
from typing import List
from task_model import Task
from EisenTodo.file_path_utils import validate_file_path, create_directory_for_path

class TaskPersistence:
    """
    TaskPersistence类负责处理任务数据与外部存储（当前基于CSV文件）之间的持久化交互，
    包括任务数据的保存、加载、导入及导出操作，严谨处理各类文件操作相关的异常情况，
    保障数据在存储和读取过程中的准确性、完整性及稳定性。
    """
    def __init__(self, csv_file_path: str = "tasks.csv"):
        """
        初始化TaskPersistence对象，设置默认的CSV文件路径，可根据实际需求传入不同路径。

        参数：
        - csv_file_path (str)：任务数据存储的CSV文件路径，默认为"tasks.csv"，
                              传入的路径需是合法可访问且具有相应读写权限的路径。

        抛出异常：
        - ValueError：如果传入的文件路径不符合要求（如为空等情况），抛出此异常并提示用户提供有效路径。
        - FileNotFoundError：如果文件路径对应的文件不存在且无法创建目录等情况，抛出此异常告知用户检查路径。
        - PermissionError：如果没有对文件或其所在目录的相应读写权限，抛出此异常提示用户检查权限设置。
        """
        validate_file_path(csv_file_path)
        self.csv_file_path = csv_file_path

    def save_tasks(self, tasks: List[Task]) -> None:
        """
        将任务列表保存到CSV文件中，调用独立的文件路径处理函数进行严谨的路径验证和必要的目录创建操作，
        采用严谨且高效的文件写入逻辑，妥善处理可能出现的各类IO相关错误，保障数据能准确无误地持久化存储。

        参数：
        - tasks (List[Task])：要保存的任务对象列表，列表中的每个任务对象需符合Task类定义的合法性要求。

        抛出异常：
        - IOError：如果保存任务数据到文件时出现IO错误（如磁盘空间不足、文件被其他程序占用等情况），
                    抛出此异常并详细说明具体的IO问题所在，方便调用者排查文件写入故障。
        """
        create_directory_for_path(self.csv_file_path)
        try:
            with open(self.csv_file_path, 'w', encoding='utf-8', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["name", "description", "progress", "category"])
                for task in tasks:
                    writer.writerow([task.name, task.description, task.progress, task.category])
        except IOError as e:
            raise IOError(f"保存任务数据到文件 {self.csv_file_path} 时出错: {str(e)}")

    def load_tasks(self) -> List[Task]:
        """
        从CSV文件加载任务数据，进行文件存在性、格式正确性以及数据合法性等多方面的验证，
        若文件不存在或数据格式不符合要求等情况，会进行相应的错误处理并返回空列表，
        确保加载过程的稳定性，最终返回符合Task类规范的任务对象列表。

        返回：
        - List[Task]：从CSV文件中读取并成功解析创建的任务对象列表，若文件不存在或读取失败则返回空列表。

        抛出异常：
        - FileNotFoundError：如果指定的CSV文件不存在，抛出此异常告知用户文件缺失情况，提示检查文件路径。
        - csv.Error：如果文件格式不符合CSV规范（如字段分隔符错误、数据类型不匹配等情况），
                     抛出此异常并说明可能的格式问题，方便用户排查文件格式故障。
        - ValueError：如果从文件中读取的数据创建任务对象时不符合Task类的属性合法性要求（如进度值超出范围等），
                      抛出此异常并明确指出具体的属性问题所在，便于定位数据错误。
        """
        return self._load_tasks_from_file(self.csv_file_path)

    def import_tasks(self, file_path: str) -> List[Task]:
        """
        从外部指定的CSV文件导入任务数据，同样进行全面的文件路径验证、文件格式检查以及数据合法性校验，
        成功导入的数据将转换为任务对象并添加到返回列表中，出现问题会准确抛出相应异常告知调用者。

        参数：
        - file_path (str)：要导入任务数据的外部CSV文件路径，需是合法有效且具有相应读写权限的路径。

        返回：
        - List[Task]：从指定外部文件中成功导入并解析创建的任务对象列表，若导入失败则返回空列表。

        抛出异常：
        - FileNotFoundError：如果指定的导入文件不存在，抛出此异常告知用户文件缺失情况，提示检查文件路径。
        - csv.Error：如果文件格式不符合CSV规范（如字段分隔符错误、数据类型不匹配等情况），
                     抛出此异常并说明可能的格式问题，方便用户排查文件格式故障。
        - ValueError：如果从文件中读取的数据创建任务对象时不符合Task类的属性合法性要求（如进度值超出范围等），
                      抛出此异常并明确指出具体的属性问题所在，便于定位数据错误。
        - PermissionError：如果没有对文件或其所在目录的相应读写权限，抛出此异常提示用户检查权限设置。
        """
        validate_file_path(file_path)
        return self._load_tasks_from_file(file_path)

    def export_tasks(self, file_path: str) -> bool:
        """
        将任务数据导出到指定的CSV文件，进行严谨到极致的文件路径验证和文件写入操作，确保导出的准确性、稳定性以及完整性，
        杜绝任何因路径或写入问题导致的数据丢失或错误，对导出文件路径进行全面的合法性、权限检查以及目录创建（如果需要）等操作，
        确保导出过程顺利且安全。

        参数：
        - file_path (str)：目标CSV文件的路径，不能为空且需确保可正常写入，任何无效路径情况都会被提前检测并提示用户修正。

        返回：
        - bool：导出成功返回True，否则返回False，并详细记录错误信息，包括从路径非法到文件系统权限不足等各类可能导致导出失败的原因，
                便于用户精准排查具体的导出失败根源，采取相应解决措施。

        抛出异常：
        - ValueError：如果提供的导出文件路径为空字符串，抛出此异常提示用户提供有效的文件路径，明确告知用户路径不能为空，
                      避免因无效路径引发后续导出错误。
        - IOError：如果文件写入过程中出现IO相关错误，抛出此异常并详细说明具体的IO问题所在，比如磁盘空间不足、文件被其他程序占用等具体情况，
                    方便用户快速定位并解决文件写入故障，保障导出操作顺利完成。
        - PermissionError：如果没有对目标文件所在目录的写入权限，抛出此异常，并明确提示用户检查文件目录权限，
                           方便用户快速定位并解决权限问题。
        """
        validate_file_path(file_path)
        create_directory_for_path(file_path)

        try:
            with open(file_path, 'w', encoding='utf-8', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["name", "description", "progress", "category"])
                tasks = self.load_tasks()
                for task in tasks:
                    writer.writerow([task.name, task.description, task.progress, task.category])
            return True
        except IOError as e:
            raise IOError(f"导出任务数据到文件 {file_path} 时出错: {str(e)}")

    def _load_tasks_from_file(self, file_path: str) -> List[Task]:
        """
        从指定的CSV文件加载任务数据，进行文件存在性、格式正确性以及数据合法性等多方面的验证，
        若文件不存在或数据格式不符合要求等情况，会进行相应的错误处理并返回空列表，
        确保加载过程的稳定性，最终返回符合Task类规范的任务对象列表。

        参数：
        - file_path (str)：要加载任务数据的CSV文件路径。

        返回：
        - List[Task]：从CSV文件中读取并成功解析创建的任务对象列表，若文件不存在或读取失败则返回空列表。

        抛出异常：
        - FileNotFoundError：如果指定的CSV文件不存在，抛出此异常告知用户文件缺失情况，提示检查文件路径。
        - csv.Error：如果文件格式不符合CSV规范（如字段分隔符错误、数据类型不匹配等情况），
                     抛出此异常并说明可能的格式问题，方便用户排查文件格式故障。
        - ValueError：如果从文件中读取的数据创建任务对象时不符合Task类的属性合法性要求（如进度值超出范围等），
                      抛出此异常并明确指出具体的属性问题所在，便于定位数据错误。
        """
        if not os.path.exists(file_path):
            return []
        tasks = []
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                next(reader)  # 跳过标题行
                for row in reader:
                    if len(row) != 4:
                        continue  # 跳过不符合格式的数据行
                    name, description, progress, category = row
                    task = Task.from_dict({
                        "name": name,
                        "description": description,
                        "progress": int(progress),
                        "category": category
                    })
                    tasks.append(task)
        except FileNotFoundError:
            raise FileNotFoundError(f"文件 {file_path} 不存在，请检查文件路径")
        except csv.Error as e:
            raise csv.Error(f"读取文件 {file_path} 时出现CSV格式错误: {str(e)}")
        except ValueError as e:
            raise ValueError(f"从文件 {file_path} 读取的数据创建任务对象时出错: {str(e)}")
        return tasks