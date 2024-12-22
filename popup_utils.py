import re
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from utils import COLOR_THEME

def create_text_input(hint_text: str, input_filter: str) -> TextInput:
    """
    创建一个带有提示文本和输入过滤器的TextInput。

    参数：
    - hint_text (str)：提示文本。
    - input_filter (str)：输入过滤器的正则表达式。

    返回：
    - TextInput：创建的TextInput对象。
    """
    return TextInput(
        hint_text=hint_text,
        multiline=False,
        size_hint_y=None,
        height=30,
        foreground_color=COLOR_THEME["text_color"],
        cursor_color=COLOR_THEME["text_color"],
        background_color=COLOR_THEME["popup_bg_color"],
        hint_text_color=COLOR_THEME["input_hint_color"],
        input_filter=lambda text, from_undo: re.sub(input_filter, '', text)
    )

def create_button(text: str, callback) -> Button:
    """
    创建一个带有文本和回调函数的Button。

    参数：
    - text (str)：按钮文本。
    - callback：按钮点击时的回调函数。

    返回：
    - Button：创建的Button对象。
    """
    return Button(
        text=text,
        size_hint=(0.4, None),
        height=40,
        on_release=callback
    )