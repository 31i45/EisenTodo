from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from task_list_screen import TaskListScreen

class MainWindow(ScreenManager):
    """
    MainWindow类继承自ScreenManager，用于管理应用程序中的不同屏幕。
    """
    def __init__(self, **kwargs):
        """
        初始化MainWindow对象，添加任务列表屏幕并设置为当前屏幕。

        参数：
        - kwargs：其他关键字参数。
        """
        super().__init__(**kwargs)
        task_list_screen = TaskListScreen(name='task_list')
        self.add_widget(task_list_screen)
        self.current = 'task_list'

class TaskManagerApp(App):
    """
    TaskManagerApp类继承自App，是应用程序的主类，负责构建应用程序的根窗口。
    """
    def build(self):
        """
        构建应用程序的根窗口。

        返回：
        - ScreenManager：返回根窗口对象。
        """
        root = MainWindow()
        return root

if __name__ == '__main__':
    # 运行应用程序
    TaskManagerApp().run()