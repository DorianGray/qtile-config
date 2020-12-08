import libqtile
from .widget import (
    Power,
    Bar,
    QTile,
    TaskList,
)
from . import theme


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
group_box = libqtile.widget.GroupBox()
prompt = libqtile.widget.Prompt()
task_list = TaskList(borderwidth=0)
spacer = libqtile.widget.Spacer()
systray = libqtile.widget.Systray()
clock = libqtile.widget.Clock(**theme.clock)
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
