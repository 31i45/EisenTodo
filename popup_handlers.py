from functools import partial
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from utils import COLOR_THEME, apply_color_theme, show_success_message, show_error_message
from popup_utils import create_text_input, create_button
from task_operations import add_task_from_popup, edit_task_from_popup, delete_task_from_popup, view_tasks_by_category, filter_tasks, sort_tasks, backup_tasks, restore_tasks

def show_add_task_popup(screen) -> None:
    """
    显示添加任务的弹窗。

    参数：
    - screen：当前屏幕对象。
    """
    popup = Popup(title='添加任务', size_hint=(0.8, 0.8), background_color=COLOR_THEME["popup_bg_color"])
    layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

    name_input = create_text_input('任务名称（1-100个字符）', r'[^\w\s-]')
    desc_input = create_text_input('任务描述', r'')
    progress_input = create_text_input('任务进度（0-100之间的整数）', r'[^\d]')
    category_input = create_text_input('任务类别（紧急重要、重要不紧急、紧急不重要、不紧急不重要）', r'[^紧急重要|重要不紧急|紧急不重要|不紧急不重要]')

    add_button = create_button('添加', partial(add_task_from_popup, screen, name_input, desc_input, progress_input, category_input, popup))
    cancel_button = create_button('取消', popup.dismiss)

    layout.add_widget(name_input)
    layout.add_widget(desc_input)
    layout.add_widget(progress_input)
    layout.add_widget(category_input)
    layout.add_widget(add_button)
    layout.add_widget(cancel_button)

    popup.content = layout
    apply_color_theme(layout)
    popup.open()

def show_edit_task_popup(screen) -> None:
    """
    显示编辑任务的弹窗。

    参数：
    - screen：当前屏幕对象。
    """
    popup = Popup(title='编辑任务', size_hint=(0.8, 0.8), background_color=COLOR_THEME["popup_bg_color"])
    layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

    name_input = create_text_input('任务名称（1-100个字符）', r'[^\w\s-]')
    desc_input = create_text_input('任务描述', r'')
    progress_input = create_text_input('任务进度（0-100之间的整数）', r'[^\d]')
    category_input = create_text_input('任务类别（紧急重要、重要不紧急、紧急不重要、不紧急不重要）', r'[^紧急重要|重要不紧急|紧急不重要|不紧急不重要]')

    edit_button = create_button('编辑', partial(edit_task_from_popup, screen, name_input, desc_input, progress_input, category_input, popup))
    cancel_button = create_button('取消', popup.dismiss)

    layout.add_widget(name_input)
    layout.add_widget(desc_input)
    layout.add_widget(progress_input)
    layout.add_widget(category_input)
    layout.add_widget(edit_button)
    layout.add_widget(cancel_button)

    popup.content = layout
    apply_color_theme(layout)
    popup.open()

def show_delete_task_popup(screen) -> None:
    """
    显示删除任务的弹窗。

    参数：
    - screen：当前屏幕对象。
    """
    popup = Popup(title='删除任务', size_hint=(0.8, 0.8), background_color=COLOR_THEME["popup_bg_color"])
    layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

    delete_button = create_button('删除', partial(delete_task_from_popup, screen, popup))
    cancel_button = create_button('取消', popup.dismiss)

    layout.add_widget(Label(text="确定要删除这个任务吗？", color=COLOR_THEME["text_color"]))
    layout.add_widget(delete_button)
    layout.add_widget(cancel_button)

    popup.content = layout
    apply_color_theme(layout)
    popup.open()

def show_tasks_by_category_popup(screen) -> None:
    """
    显示按类别查看任务的弹窗。

    参数：
    - screen：当前屏幕对象。
    """
    popup = Popup(title='按类别查看任务', size_hint=(0.8, 0.8), background_color=COLOR_THEME["popup_bg_color"])
    layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

    category_input = create_text_input('任务类别（紧急重要、重要不紧急、紧急不重要、不紧急不重要）', r'[^紧急重要|重要不紧急|紧急不重要|不紧急不重要]')
    view_button = create_button('查看', partial(view_tasks_by_category, screen, category_input, popup))
    cancel_button = create_button('取消', popup.dismiss)

    layout.add_widget(category_input)
    layout.add_widget(view_button)
    layout.add_widget(cancel_button)

    popup.content = layout
    apply_color_theme(layout)
    popup.open()

def show_filter_tasks_popup(screen) -> None:
    """
    显示筛选任务的弹窗。

    参数：
    - screen：当前屏幕对象。
    """
    popup = Popup(title='筛选任务', size_hint=(0.8, 0.8), background_color=COLOR_THEME["popup_bg_color"])
    layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

    keyword_input = create_text_input('关键字', r'')
    progress_min_input = create_text_input('最小进度（0-100）', r'[^\d]')
    progress_max_input = create_text_input('最大进度（0-100）', r'[^\d]')
    filter_button = create_button('筛选', partial(filter_tasks, screen, keyword_input, progress_min_input, progress_max_input, popup))
    cancel_button = create_button('取消', popup.dismiss)

    layout.add_widget(keyword_input)
    layout.add_widget(progress_min_input)
    layout.add_widget(progress_max_input)
    layout.add_widget(filter_button)
    layout.add_widget(cancel_button)

    popup.content = layout
    apply_color_theme(layout)
    popup.open()

def show_sort_tasks_popup(screen) -> None:
    """
    显示排序任务的弹窗。

    参数：
    - screen：当前屏幕对象。
    """
    popup = Popup(title='排序任务', size_hint=(0.8, 0.8), background_color=COLOR_THEME["popup_bg_color"])
    layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

    sort_key_input = create_text_input('排序键（name, progress, category）', r'[^\w]')
    ascending_input = create_text_input('升序（True/False）', r'[^\w]')
    sort_button = create_button('排序', partial(sort_tasks, screen, sort_key_input, ascending_input, popup))
    cancel_button = create_button('取消', popup.dismiss)

    layout.add_widget(sort_key_input)
    layout.add_widget(ascending_input)
    layout.add_widget(sort_button)
    layout.add_widget(cancel_button)

    popup.content = layout
    apply_color_theme(layout)
    popup.open()

def show_backup_tasks_popup(screen) -> None:
    """
    显示备份任务数据的弹窗。

    参数：
    - screen：当前屏幕对象。
    """
    popup = Popup(title='备份任务数据', size_hint=(0.8, 0.8), background_color=COLOR_THEME["popup_bg_color"])
    layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

    backup_path_input = create_text_input('备份路径', r'')
    backup_button = create_button('备份', partial(backup_tasks, screen, backup_path_input, popup))
    cancel_button = create_button('取消', popup.dismiss)

    layout.add_widget(backup_path_input)
    layout.add_widget(backup_button)
    layout.add_widget(cancel_button)

    popup.content = layout
    apply_color_theme(layout)
    popup.open()

def show_restore_tasks_popup(screen) -> None:
    """
    显示恢复任务数据的弹窗。

    参数：
    - screen：当前屏幕对象。
    """
    popup = Popup(title='恢复任务数据', size_hint=(0.8, 0.8), background_color=COLOR_THEME["popup_bg_color"])
    layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

    restore_path_input = create_text_input('恢复路径', r'')
    restore_button = create_button('恢复', partial(restore_tasks, screen, restore_path_input, popup))
    cancel_button = create_button('取消', popup.dismiss)

    layout.add_widget(restore_path_input)
    layout.add_widget(restore_button)
    layout.add_widget(cancel_button)

    popup.content = layout
    apply_color_theme(layout)
    popup.open()