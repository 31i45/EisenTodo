import os
import pathlib
from typing import Union, List

def validate_file_path(file_path: str) -> bool:
    """
    验证文件路径的合法性，检查是否为空、是否存在以及当前进程对其是否有相应权限等。

    参数：
    - file_path (str)：要验证的文件路径。

    抛出异常：
    - ValueError：如果文件路径为空，抛出此异常，提示用户提供有效的文件路径。
    - FileNotFoundError：如果文件路径对应的文件或目录不存在，抛出此异常，提示用户检查文件路径。
    - PermissionError：如果没有对文件或其所在目录的相应权限（读或写等），抛出此异常，提示用户检查权限设置。
    """
    if not file_path:
        raise ValueError("文件路径不能为空")
    file_path = str(pathlib.Path(file_path).resolve())
    file_obj = pathlib.Path(file_path)
    if not file_obj.exists():
        raise FileNotFoundError(f"文件 {file_path} 不存在，请检查文件路径")
    elif file_obj.is_dir():
        if not os.access(file_path, os.W_OK | os.R_OK):
            raise PermissionError(f"没有对目录 {file_path} 的读写权限，请检查权限设置")
    else:
        if not os.access(file_path, os.W_OK) and not os.access(file_path, os.R_OK):
            raise PermissionError(f"没有对文件 {file_path} 的读写权限，请检查权限设置")
    return True

def create_directory_for_path(file_path: str) -> bool:
    """
    为给定的文件路径创建对应的目录（如果该目录不存在的话），保障后续文件操作能顺利进行。

    参数：
    - file_path (str)：文件路径，会提取其所在目录路径并创建目录（如果不存在）。

    返回：
    - bool：如果目录创建成功或者已经存在则返回True，否则返回False。
    """
    dir_path = os.path.dirname(file_path)
    if dir_path and not os.path.exists(dir_path):
        try:
            os.makedirs(dir_path)
            return True
        except OSError as e:
            print(f"创建目录 {dir_path} 时出错: {str(e)}")
            return False
    return True

def get_file_extension(file_path: str) -> str:
    """
    获取文件路径对应的文件扩展名，用于后续根据扩展名进行不同的业务逻辑处理（如判断文件类型等）。

    参数：
    - file_path (str)：文件路径。

    返回：
    - str：文件的扩展名，包含点号（例如 '.csv'），如果文件没有扩展名则返回空字符串。
    """
    return os.path.splitext(file_path)[1]

def is_same_path(path1: str, path2: str) -> bool:
    """
    判断两个文件路径是否指向同一个实际的文件或目录，考虑路径的规范化、大小写敏感性等因素（基于操作系统特性）。

    参数：
    - path1 (str)：第一个文件路径。
    - path2 (str)：第二个文件路径。

    返回：
    - bool：如果两个路径指向同一文件或目录则返回True，否则返回False。
    """
    return pathlib.Path(path1).resolve() == pathlib.Path(path2).resolve()

def list_files_in_directory(directory_path: str) -> List[str]:
    """
    列出指定目录下的所有文件（不包含子目录中的文件），方便进行批量文件操作相关的功能实现（如遍历备份文件等）。

    参数：
    - directory_path (str)：要列出文件的目录路径，需是合法存在且具有相应读取权限的目录。

    抛出异常：
    - FileNotFoundError：如果指定的目录不存在，抛出此异常，提示用户检查目录路径。
    - PermissionError：如果没有对该目录的读取权限，抛出此异常，提示用户检查权限设置。

    返回：
    - list：目录下所有文件的文件名列表（包含完整路径），如果目录为空则返回空列表。
    """
    if not os.path.exists(directory_path):
        raise FileNotFoundError(f"目录 {directory_path} 不存在，请检查目录路径")
    if not os.access(directory_path, os.R_OK):
        raise PermissionError(f"没有对目录 {directory_path} 的读取权限，请检查权限设置")
    return [os.path.join(directory_path, file) for file in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, file))]