from enum import (
    Flag,
    auto,
)
import cairocffi
from libqtile.widget import tasklist
from ... import (
    util,
    theme,
)
from ..tooltip import Tooltip


__all__ = [
    'TaskList',
]


class WindowState(Flag):
    DEFAULT = 0
    FOCUSED = auto()
    UNFOCUSED = auto()
    MINIMIZED = auto()

    @classmethod
    def from_window(cls, window, current_window=None):
        state = WindowState(WindowState.DEFAULT)
        if window.minimized:
            state |= WindowState.MINIMIZED

        if window is current_window:
            state |= WindowState.FOCUSED
        else:
            state |= WindowState.UNFOCUSED
        return state


class TaskList(tasklist.TaskList):
    @staticmethod
    def _icon_get_dimensions(string):
        return tuple(map(int, string.split('x')))

    @staticmethod
    def _icon_scale_matrix(size, newsize):
        matrix = cairocffi.Matrix()
        sp = newsize / size
        matrix.scale(sp, sp)
        return matrix

    @classmethod
    def _icon_surface(cls, icon):
        return util.cairo.duplicate_surface(
            cairocffi.ImageSurface.create_for_data(
                icon[1],
                cairocffi.FORMAT_ARGB32,
                *cls._icon_get_dimensions(icon[0]),
            ),
        )

    @classmethod
    def _icon_render(cls, window, size, state=WindowState.DEFAULT):
        icon = sorted(
            iter(window.icons.items()),
            key=lambda icon: abs(size - max(cls._icon_get_dimensions(icon[0])))
        )[0]
        surface = cls._icon_surface(icon)

        if WindowState.UNFOCUSED in state:
            util.cairo.darken(surface, 0.5)

        if WindowState.MINIMIZED in state:
            util.cairo.grayscale(surface)

        return surface

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._tooltip = Tooltip(**theme.tooltip)

    def get_window_icon(self, window):
        if not window.icons:
            return None

        wid = window.window.wid
        state = WindowState.from_window(
            window,
            current_window=self.bar.screen.group.current_window,
        )
        cache = self._icons_cache

        if wid in cache:
            if state in cache[wid]:
                return cache[wid][state]
        else:
            cache[wid] = {}

        surface = self._icon_render(window, self.icon_size, state=state)
        width, height = util.cairo.get_surface_size(surface)
        pattern = cairocffi.SurfacePattern(surface)

        size = max(width, height)
        if size != self.icon_size:
            pattern.set_matrix(self._icon_scale_matrix(
                self.icon_size,
                size,
            ))

        cache[wid][state] = pattern
        return pattern

    def mouse_enter(self, x, y):
        super().mouse_enter(x, y)
        win = self.get_clicked(x, y)
        if win is not None:
            self._tooltip.text = win.name

            x = min(
                self.bar.width - self._tooltip.width,
                self.offset,
            ) + x
            y = self.bar.height
            self._tooltip.show(x, y)

    def mouse_leave(self, x, y):
        super().mouse_enter(self.margin_x + x, y)
        self._tooltip.hide()

    def get_taskname(self, window):
        return ''
