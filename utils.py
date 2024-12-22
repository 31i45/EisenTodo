import json
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.animation import Animation
from kivy.properties import ListProperty
from EisenTodo.animation_effects import show_success_animation, show_error_animation

# 定义全局的颜色主题字典，方便统一管理界面的颜色风格
COLOR_THEME = {
    "text_color": [1, 1, 1, 1],
    "button_bg_color": [0.2, 0.2, 0.2, 1],
    "button_text_color": [1, 1, 1, 1],
    "popup_bg_color": [0.15, 0.15, 0.15, 1],
    "input_hint_color": [0.5, 0.5, 0.5, 1],
    "success_color": [0, 1, 0, 1],
    "error_color": [1, 0, 0, 1],
    "highlight_color": [0.3, 0.3, 0.3, 1],
    "urgent_important": [1, 0, 0, 1],
    "important_not_urgent": [0, 1, 0, 1],
    "urgent_not_important": [0, 0, 1, 1],
    "not_important_not_urgent": [0.5, 0.5, 0.5, 1],
}

# 配置文件路径，用于存储一些应用相关的配置信息，如上次使用的备份路径等
CONFIG_PATH = "config.json"
config_data = {}

def apply_color_theme(widget) -> None:
    """
    应用颜色主题到指定的界面部件。

    参数：
    - widget：要应用颜色主题的界面部件，可以是BoxLayout、Popup、Button、TextInput或Label。
    """
    if isinstance(widget, BoxLayout) or isinstance(widget, Popup):
        widget.background_color = COLOR_THEME["popup_bg_color"]
    elif isinstance(widget, Button):
        widget.background_color = COLOR_THEME["button_bg_color"]
        widget.color = COLOR_THEME["button_text_color"]
    elif isinstance(widget, TextInput):
        widget.background_color = COLOR_THEME["popup_bg_color"]
        widget.foreground_color = COLOR_THEME["text_color"]
        widget.hint_text_color = COLOR_THEME["input_hint_color"]
        widget.cursor_color = COLOR_THEME["text_color"]
    elif isinstance(widget, Label):
        widget.color = COLOR_THEME["text_color"]
    else:
        print(f"未知的部件类型: {type(widget)}")

def save_last_path(key: str, value: str) -> None:
    """
    保存最后使用的路径到配置文件中。

    参数：
    - key (str)：配置项的键。
    - value (str)：配置项的值。
    """
    global config_data
    config_data[key] = value
    try:
        with open(CONFIG_PATH, 'w') as file:
            json.dump(config_data, file)
    except IOError as e:
        print(f"保存配置文件 {CONFIG_PATH} 时出错: {str(e)}")

def show_success_message(message: str) -> None:
    """
    显示操作成功的提示消息，并应用动画效果。

    参数：
    - message (str)：要显示的提示消息。
    """
    popup = Popup(title='提示', content=Label(text=message, color=COLOR_THEME["success_color"]),
                  size_hint=(0.4, 0.3), background_color=COLOR_THEME["popup_bg_color"])
    apply_color_theme(popup.content)
    show_success_animation(popup.content)
    popup.open()

def show_error_message(message: str) -> None:
    """
    显示操作失败的提示消息，并应用动画效果。

    参数：
    - message (str)：要显示的提示消息。
    """
    popup = Popup(title='提示', content=Label(text=message, color=COLOR_THEME["error_color"]),
                  size_hint=(0.4, 0.3), background_color=COLOR_THEME["popup_bg_color"])
    apply_color_theme(popup.content)
    show_error_animation(popup.content)
    popup.open()