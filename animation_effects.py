from kivy.animation import Animation
from kivy.uix.widget import Widget

def show_success_animation(widget: Widget, repeat: int = 3) -> None:
    """
    为操作成功提示信息的展示部件添加特定的动画效果，包含闪烁、缩放等组合动画，使其更具视觉吸引力和趣味性，
    突出显示操作成功的提示信息，增强用户操作后的积极反馈感。

    参数：
    - widget (Widget)：要添加动画效果的界面部件，通常是包含操作成功提示信息的Label等组件。
    - repeat (int)：动画重复次数，默认为3次。
    """
    anim = Animation(opacity=1, scale=(1.1, 1.1), duration=0.2, t='out_cubic')
    anim &= Animation(opacity=0.8, scale=(1, 1), duration=0.1, t='out_cubic')
    anim &= Animation(opacity=1, scale=(1.05, 1.05), duration=0.1, t='out_cubic')
    anim &= Animation(opacity=1, scale=(1, 1), duration=0.1, t='out_cubic')
    anim.repeat = repeat
    anim.start(widget)

def show_error_animation(widget: Widget, repeat: int = 3) -> None:
    """
    针对操作失败提示信息的展示部件打造了包含淡入淡出、颜色变化等的动画效果，突出显示错误提示以吸引用户关注，
    让用户能快速察觉到操作出现问题，方便用户及时知晓并处理异常情况。

    参数：
    - widget (Widget)：要添加动画效果的界面部件，通常是包含操作失败提示信息的Label等组件。
    - repeat (int)：动画重复次数，默认为3次。
    """
    anim = Animation(opacity=0, duration=0.1, t='in_cubic')
    anim &= Animation(opacity=1, color=(1, 0, 0, 1), duration=0.2, t='out_cubic')  # 变为红色表示错误
    anim &= Animation(opacity=0.8, color=(1, 0, 0, 0.8), duration=0.1, t='out_cubic')
    anim &= Animation(opacity=1, color=(1, 0, 0, 1), duration=0.1, t='out_cubic')
    anim &= Animation(opacity=0, duration=0.1, t='in_cubic')
    anim.repeat = repeat
    anim.start(widget)

def task_list_item_animation(widget: Widget) -> None:
    """
    为任务列表中的单个项目在更新时应用淡入、缩放、位移等组合动画，让列表更新过程更加平滑自然且生动，
    提升任务列表更新时的视觉效果，优化用户查看任务列表变化的体验。

    参数：
    - widget (Widget)：要添加动画效果的界面部件，通常是任务列表中的单个Item对应的组件。
    """
    anim = Animation(opacity=0, scale=(0.8, 0.8), y=widget.y - 10, duration=0.1, t='in_cubic')
    anim &= Animation(opacity=1, scale=(1.05, 1.05), y=widget.y, duration=0.2, t='out_cubic')
    anim &= Animation(scale=(1, 1), duration=0.1, t='out_cubic')
    anim.start(widget)