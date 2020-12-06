from .widget import (
    Power,
    Bar,
    QTile,
)
from . import theme
from libqtile import widget


__all__ = [
    'group_box',
    'prompt',
    'task_list',
    'spacer',
    'systray',
    'clock',
    'power',
    'bar',
    'qtile',
]


qtile = QTile()
group_box = widget.GroupBox()
prompt = widget.Prompt()
task_list = widget.TaskList()
spacer = widget.Spacer()
systray = widget.Systray()
clock = widget.Clock(**theme.clock)
power = Power(**theme.power)
bar = Bar(
    [
        group_box,
        prompt,
        task_list,
        spacer,
        systray,
        clock,
        power,
    ],
    64,
)
