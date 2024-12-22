import re
import os
import pathlib
from typing import Union

def validate_task_name(name: str) -> bool:
    """
    验证任务名称的合法性，要求长度在1 - 100个字符之间，且只能包含字母、数字、空格、下划线和短横线。

    参数：
    - name (str)：要验证的任务名称。

    抛出异常：
    - ValueError：如果任务名称长度不符合要求，或者包含非法字符，抛出此异常，明确提示用户输入正确的名称要求。
    """
    if not (1 <= len(name) <= 100):
        raise ValueError("任务名称长度需在1 - 100个字符之间")
    if re.search(r'[^\w\s-]', name):
        raise ValueError("任务名称只能包含字母、数字、空格、下划线和短横线")
    return True

def validate_task_progress(progress: Union[str, int]) -> bool:
    """
    验证任务进度的合法性，要求取值范围是0 - 100的整数。

    参数：
    - progress (str 或 int)：要验证的任务进度表示，可以是字符串形式的数字或直接为整数，会尝试转换为整数进行验证。

    抛出异常：
    - ValueError：如果任务进度不在0 - 100范围内，或者无法转换为整数，抛出此异常，明确提示用户输入正确的进度范围及格式。
    """
    try:
        progress = int(progress)
        if not (0 <= progress <= 100):
            raise ValueError("任务进度需在0到100之间")
        return True
    except ValueError:
        raise ValueError("任务进度需为0到100之间的整数")

def validate_task_category(category: str) -> bool:
    """
    验证任务类别的合法性，要求取值为规定的几个类别之一，即"紧急重要"、"重要不紧急"、"紧急不重要"、"不紧急不重要"。

    参数：
    - category (str)：要验证的任务类别。

    抛出异常：
    - ValueError：如果任务类别输入不合法，抛出此异常，明确提示用户输入合法的类别选项。
    """
    valid_categories = ["紧急重要", "重要不紧急", "紧急不重要", "不紧急不重要"]
    if category not in valid_categories:
        raise ValueError("任务类别输入不合法，请输入紧急重要、重要不紧急、紧急不重要、不紧急不重要之一")
    return True

def validate_file_path(file_path: str) -> bool:
    """
    验证文件路径的合法性，检查是否为空、是否存在以及当前进程对其是否有相应权限等。

    参数：
    - file_path (str)：要验证的文件路径。

    抛出异常：
    - ValueError：如果文件路径为空，抛出此异常，提示用户提供有效的文件路径。
    - FileNotFoundError：如果文件路径对应的文件不存在，抛出此异常，提示用户检查文件路径。
    - PermissionError：如果没有对文件或其所在目录的相应权限（读或写等），抛出此异常，提示用户检查权限设置。
    """
    if not file_path:
        raise ValueError("文件路径不能为空")
    
    file_path = str(pathlib.Path(file_path).resolve())
    file_obj = pathlib.Path(file_path)
    
    if not file_obj.exists():
        raise FileNotFoundError(f"文件 {file_path} 不存在，请检查文件路径")
    elif file_obj.is_dir():
        if not os.access(file_path, os.W_OK | os.R.OK):
            raise PermissionError(f"没有对目录 {file_path} 的读写权限，请检查权限设置")
    else:
        if not os.access(file_path, os.W.OK) and not os.access(file_path, os.R.OK):
            raise PermissionError(f"没有对文件 {file_path} 的读写权限，请检查权限设置")
    return True