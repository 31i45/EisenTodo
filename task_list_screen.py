import json
import os
from typing import List
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.animation import Animation
from kivy.properties import ListProperty
from task_logic import TaskManager
from task_persistence import TaskPersistence
from input_validation import validate_task_name, validate_task_progress, validate_task_category
from popup_handlers import show_add_task_popup, show_edit_task_popup, show_delete_task_popup, show_tasks_by_category_popup, show_filter_tasks_popup, show_sort_tasks_popup, show_backup_tasks_popup, show_restore_tasks_popup
from utils import COLOR_THEME, CONFIG_PATH, apply_color_theme, save_last_path, show_success_message, show_error_message
from animation_effects import task_list_item_animation  # 导入 task_list_item_animation 函数
from task_model import Task  # 导入 Task 类

class TaskListScreen(Screen):
    """
    TaskListScreen类继承自Screen，用于显示和管理任务列表的屏幕。
    """
    task_list = ListProperty([])

    def __init__(self, **kwargs):
        """
        初始化TaskListScreen对象，加载任务列表和配置数据，并设置界面布局。

        参数：
        - kwargs：其他关键字参数。
        """
        super().__init__(**kwargs)
        self.task_manager = TaskManager(TaskPersistence())
        self.config_data = self.load_config()
        self.task_list_label = Label(text="", markup=True, size_hint_y=None)
        self.update_task_list()
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        self.add_buttons(layout)
        layout.add_widget(self.task_list_label)
        self.add_widget(layout)

    def load_config(self) -> dict:
        """
        加载配置文件中的数据。

        返回：
        - dict：配置数据字典。
        """
        if os.path.exists(CONFIG_PATH):
            try:
                with open(CONFIG_PATH, 'r') as file:
                    return json.load(file)
            except (IOError, json.JSONDecodeError) as e:
                print(f"加载配置文件时出错: {str(e)}")
        return {}

    def update_task_list(self) -> None:
        """
        更新任务列表，应用动画效果并显示任务。
        """
        all_tasks = self.task_manager.get_tasks_by_category("")
        anim = Animation(opacity=0, duration=0.2, t='out_cubic')
        anim &= Animation(text="", duration=0.2, t='out_cubic')
        anim.bind(on_complete=lambda *args: self.display_tasks(all_tasks))
        anim.start(self.task_list_label)

    def display_tasks(self, tasks: List[Task]) -> None:
        """
        显示任务列表中的任务，应用颜色主题和动画效果。

        参数：
        - tasks (List[Task])：任务对象列表。
        """
        task_text = ""
        for task in tasks:
            progress_text = f"<b>进度:</b> {task.progress}%<br><b>类别:</b> {task.category}<br><br>"
            if task.category == "紧急重要":
                task_text += task.name + " " + progress_text[:-4] + f' <font color="{COLOR_THEME["urgent_important"]}">[紧急重要]</font><br><br>'
            elif task.category == "重要不紧急":
                task_text += task.name + " " + progress_text[:-4] + f' <font color="{COLOR_THEME["important_not_urgent"]}">[重要不紧急]</font><br><br>'
            elif task.category == "紧急不重要":
                task_text += task.name + " " + progress_text[:-4] + f' <font color="{COLOR_THEME["urgent_not_important"]}">[紧急不重要]</font><br><br>'
            elif task.category == "不紧急不重要":
                task_text += task.name + " " + progress_text[:-4] + f' <font color="{COLOR_THEME["not_important_not_urgent"]}">[不紧急不重要]</font><br><br>'
        self.task_list_label.text = task_text if task_text else "暂无任务，请添加任务。"
        self.task_list_label.markup = True
        for child in self.task_list_label.children:
            task_list_item_animation(child)

    def add_buttons(self, layout: BoxLayout) -> None:
        """
        添加任务管理的按钮到布局中。

        参数：
        - layout (BoxLayout)：布局对象。
        """
        buttons = [
            ("添加任务", self.show_add_task_popup),
            ("编辑任务", self.show_edit_task_popup),
            ("删除任务", self.show_delete_task_popup),
            ("按类别查看任务", self.show_tasks_by_category_popup),
            ("筛选任务", self.show_filter_tasks_popup),
            ("排序任务", self.show_sort_tasks_popup),
            ("备份任务数据", self.show_backup_tasks_popup),
            ("恢复任务数据", self.show_restore_tasks_popup)
        ]
        for text, callback in buttons:
            button = Button(text=text, size_hint=(0.4, None), height=40, on_release=callback)
            layout.add_widget(button)

    def show_add_task_popup(self) -> None:
        """
        显示添加任务的弹窗。
        """
        show_add_task_popup(self)

    def show_edit_task_popup(self) -> None:
        """
        显示编辑任务的弹窗。
        """
        show_edit_task_popup(self)

    def show_delete_task_popup(self) -> None:
        """
        显示删除任务的弹窗。
        """
        show_delete_task_popup(self)

    def show_tasks_by_category_popup(self) -> None:
        """
        显示按类别查看任务的弹窗。
        """
        show_tasks_by_category_popup(self)

    def show_filter_tasks_popup(self) -> None:
        """
        显示筛选任务的弹窗。
        """
        show_filter_tasks_popup(self)

    def show_sort_tasks_popup(self) -> None:
        """
        显示排序任务的弹窗。
        """
        show_sort_tasks_popup(self)

    def show_backup_tasks_popup(self) -> None:
        """
        显示备份任务数据的弹窗。
        """
        show_backup_tasks_popup(self)

    def show_restore_tasks_popup(self) -> None:
        """
        显示恢复任务数据的弹窗。
        """
        show_restore_tasks_popup(self)