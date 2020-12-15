from datetime import date
from libqtile.widget import Clock
from ..tooltip import Tooltip
from ... import theme


__all__ = [
    'Clock',
]


class Clock(Clock):
    defaults = [
        ('tooltip_format', '%Y/%m/%d', 'format tooltip output'),
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_defaults(self.__class__.defaults)
        self._tooltip = Tooltip(**theme.tooltip)

    def tooltip(self):
        return date.today().strftime(self.tooltip_format)

    def mouse_enter(self, x, y):
        # set x to prevent drawing offscreen
        x = min(
            self.bar.width - self._tooltip.width,
            self.offset,
        )
        y = self.bar.height
        self._tooltip.show(x, y, self.tooltip())

    def mouse_leave(self, x, y):
        self._tooltip.hide()
