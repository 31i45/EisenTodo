from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from input_validation import validate_task_name, validate_task_progress, validate_task_category
from utils import show_success_message, show_error_message, save_last_path
from task_model import Task

def add_task_from_popup(screen, name_input: TextInput, desc_input: TextInput, progress_input: TextInput, category_input: TextInput, popup: Popup) -> None:
    """
    从弹窗中添加任务。

    参数：
    - screen：当前屏幕对象。
    - name_input (TextInput)：任务名称输入框。
    - desc_input (TextInput)：任务描述输入框。
    - progress_input (TextInput)：任务进度输入框。
    - category_input (TextInput)：任务类别输入框。
    - popup (Popup)：弹窗对象。
    """
    try:
        name = name_input.text
        desc = desc_input.text
        progress = progress_input.text
        category = category_input.text
        validate_task_name(name)
        validate_task_progress(progress)
        validate_task_category(category)
        task = Task(name, desc, int(progress), category)
        screen.task_manager.add_task(task)
        show_success_message("任务添加成功！")
        popup.dismiss()
        screen.update_task_list()
        save_last_path("backup_path", name_input.text)
    except ValueError as e:
        show_error_message(str(e))

def edit_task_from_popup(screen, name_input: TextInput, desc_input: TextInput, progress_input: TextInput, category_input: TextInput, popup: Popup) -> None:
    """
    从弹窗中编辑任务。

    参数：
    - screen：当前屏幕对象。
    - name_input (TextInput)：任务名称输入框。
    - desc_input (TextInput)：任务描述输入框。
    - progress_input (TextInput)：任务进度输入框。
    - category_input (TextInput)：任务类别输入框。
    - popup (Popup)：弹窗对象。
    """
    try:
        name = name_input.text
        desc = desc_input.text
        progress = progress_input.text
        category = category_input.text
        validate_task_name(name)
        validate_task_progress(progress)
        validate_task_category(category)
        task = Task(name, desc, int(progress), category)
        screen.task_manager.edit_task(screen.selected_task_index, task)
        show_success_message("任务编辑成功！")
        popup.dismiss()
        screen.update_task_list()
    except ValueError as e:
        show_error_message(str(e))

def delete_task_from_popup(screen, popup: Popup) -> None:
    """
    从弹窗中删除任务。

    参数：
    - screen：当前屏幕对象。
    - popup (Popup)：弹窗对象。
    """
    try:
        screen.task_manager.delete_task(screen.selected_task_index)
        show_success_message("任务删除成功！")
        popup.dismiss()
        screen.update_task_list()
    except IndexError as e:
        show_error_message(str(e))

def view_tasks_by_category(screen, category_input: TextInput, popup: Popup) -> None:
    """
    按类别查看任务。

    参数：
    - screen：当前屏幕对象。
    - category_input (TextInput)：任务类别输入框。
    - popup (Popup)：弹窗对象。
    """
    try:
        category = category_input.text
        validate_task_category(category)
        screen.display_tasks(screen.task_manager.get_tasks_by_category(category))
        popup.dismiss()
    except ValueError as e:
        show_error_message(str(e))

def filter_tasks(screen, keyword_input: TextInput, progress_min_input: TextInput, progress_max_input: TextInput, popup: Popup) -> None:
    """
    筛选任务。

    参数：
    - screen：当前屏幕对象。
    - keyword_input (TextInput)：关键字输入框。
    - progress_min_input (TextInput)：最小进度输入框。
    - progress_max_input (TextInput)：最大进度输入框。
    - popup (Popup)：弹窗对象。
    """
    try:
        keyword = keyword_input.text
        progress_min = int(progress_min_input.text) if progress_min_input.text else 0
        progress_max = int(progress_max_input.text) if progress_max_input.text else 100
        filters = {"progress": (progress_min, progress_max)}
        screen.display_tasks(screen.task_manager.filter_tasks(keyword, filters))
        popup.dismiss()
    except ValueError as e:
        show_error_message(str(e))

def sort_tasks(screen, sort_key_input: TextInput, ascending_input: TextInput, popup: Popup) -> None:
    """
    排序任务。

    参数：
    - screen：当前屏幕对象。
    - sort_key_input (TextInput)：排序键输入框。
    - ascending_input (TextInput)：升序输入框。
    - popup (Popup)：弹窗对象。
    """
    try:
        sort_key = sort_key_input.text
        ascending = ascending_input.text.lower() == 'true'
        screen.display_tasks(screen.task_manager.sort_tasks(sort_key, ascending))
        popup.dismiss()
    except ValueError as e:
        show_error_message(str(e))

def backup_tasks(screen, backup_path_input: TextInput, popup: Popup) -> None:
    """
    备份任务数据。

    参数：
    - screen：当前屏幕对象。
    - backup_path_input (TextInput)：备份路径输入框。
    - popup (Popup)：弹窗对象。
    """
    try:
        backup_path = backup_path_input.text
        screen.task_manager.persistence.export_tasks(backup_path)
        show_success_message("任务数据备份成功！")
        popup.dismiss()
        save_last_path("backup_path", backup_path)
    except (ValueError, IOError, PermissionError) as e:
        show_error_message(str(e))

def restore_tasks(screen, restore_path_input: TextInput, popup: Popup) -> None:
    """
    恢复任务数据。

    参数：
    - screen：当前屏幕对象。
    - restore_path_input (TextInput)：恢复路径输入框。
    - popup (Popup)：弹窗对象。
    """
    try:
        restore_path = restore_path_input.text
        screen.task_manager.persistence.import_tasks(restore_path)
        show_success_message("任务数据恢复成功！")
        popup.dismiss()
        screen.update_task_list()
        save_last_path("restore_path", restore_path)
    except (ValueError, IOError, PermissionError) as e:
        show_error_message(str(e))