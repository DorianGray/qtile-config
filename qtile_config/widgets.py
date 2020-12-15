import libqtile
from .widget import (
    Power,
    Clock,
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
group_box = libqtile.widget.GroupBox(**theme.group)
prompt = libqtile.widget.Prompt()
task_list = TaskList(**theme.tasklist)
spacer = libqtile.widget.Spacer()
systray = libqtile.widget.Systray(**theme.systray)
clock = Clock(**theme.clock)
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
