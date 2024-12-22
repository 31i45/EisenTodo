from typing import Dict


class Task:
    """
    Task类用于表示任务对象，封装了任务的各项属性及相关操作方法，
    严格把控任务数据的合法性与完整性，为整个任务管理系统提供标准的数据模型基础。
    """
    def __init__(self, name: str, description: str, progress: int, category: str):
        """
        初始化Task对象。

        参数：
        - name (str)：任务名称，长度需在1 - 100个字符之间。
        - description (str)：任务描述，可为任意长度字符串。
        - progress (int)：任务进度，取值范围是0 - 100的整数。
        - category (str)：任务类别，取值应为"紧急重要"、"重要不紧急"、"紧急不重要"、"不紧急不重要"之一。

        抛出异常：
        - ValueError：如果传入的参数不符合上述要求，抛出此异常并明确提示相应的错误信息，
                      确保创建的任务对象从初始数据就是合法合规的。
        """
        self._validate_name(name)
        self._validate_progress(progress)
        self._validate_category(category)
        self._name = name
        self._description = description
        self._progress = progress
        self._category = category

    @property
    def name(self) -> str:
        """
        获取任务名称。

        返回：
        - str：任务名称。
        """
        return self._name

    @property
    def description(self) -> str:
        """
        获取任务描述。

        返回：
        - str：任务描述。
        """
        return self._description

    @property
    def progress(self) -> int:
        """
        获取任务进度。

        返回：
        - int：任务进度。
        """
        return self._progress

    @property
    def category(self) -> str:
        """
        获取任务类别。

        返回：
        - str：任务类别。
        """
        return self._category

    @staticmethod
    def _validate_name(name: str):
        """
        私有方法，用于验证任务名称的合法性，要求长度在1 - 100个字符之间。

        参数：
        - name (str)：要验证的任务名称。

        抛出异常：
        - ValueError：如果任务名称长度不符合要求，抛出此异常，明确提示用户输入正确的名称长度范围。
        """
        if not (1 <= len(name) <= 100):
            raise ValueError("任务名称长度需在1 - 100个字符之间")

    @staticmethod
    def _validate_progress(progress: int):
        """
        私有方法，用于验证任务进度的合法性，要求取值范围是0 - 100。

        参数：
        - progress (int)：要验证的任务进度。

        抛出异常：
        - ValueError：如果任务进度不在0 - 100范围内，抛出此异常，明确提示用户输入正确的进度范围。
        """
        if not (0 <= progress <= 100):
            raise ValueError("任务进度需在0到100之间")

    @staticmethod
    def _validate_category(category: str):
        """
        私有方法，用于验证任务类别的合法性，要求取值为规定的几个类别之一。

        参数：
        - category (str)：要验证的任务类别。

        抛出异常：
        - ValueError：如果任务类别输入不合法，抛出此异常，明确提示用户输入合法的类别选项。
        """
        valid_categories = ["紧急重要", "重要不紧急", "紧急不重要", "不紧急不重要"]
        if category not in valid_categories:
            raise ValueError(f"任务类别输入不合法，有效类别为：{', '.join(valid_categories)}")

    def to_dict(self) -> Dict[str, object]:
        """
        将任务对象转换为字典形式，方便进行数据持久化等操作，如存储到文件或与其他数据格式进行转换。

        返回：
        - Dict[str, object]：包含任务各属性的字典，键分别为'name'、'description'、'progress'、'category'，
                            对应的值为任务对象相应的属性值。
        """
        return {
            "name": self.name,
            "description": self.description,
            "progress": self.progress,
            "category": self.category
        }

    @classmethod
    def from_dict(cls, task_dict: Dict[str, object]) -> 'Task':
        """
        类方法，从给定的字典数据创建Task对象，主要用于从存储的数据（如文件读取后的数据）恢复任务对象。

        参数：
        - task_dict (Dict[str, object])：包含任务各属性的字典，需包含'name'、'description'、'progress'、'category'键，
                                        且对应的值需符合任务属性的合法性要求。

        返回：
        - Task：根据字典数据创建的Task对象。

        抛出异常：
        - ValueError：如果字典中数据不符合任务属性要求（如缺少必要键或值不合法等情况），抛出此异常并明确提示相应错误。
        """
        name = task_dict.get("name")
        description = task_dict.get("description")
        progress = task_dict.get("progress")
        category = task_dict.get("category")
        if None in (name, description, progress, category):
            raise ValueError("任务字典数据不完整，缺少必要的任务属性信息")
        return cls(name, description, progress, category)