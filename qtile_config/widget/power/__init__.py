import math
import cairocffi

from libqtile import bar
# from libqtile.log_utils import logger
from libqtile.widget import base


__all__ = [
    'Power',
]


def hex2rgb(s):
    s = s.lstrip("#")
    return tuple(float(int(s[i:i+2], 16)) for i in (0, 2, 4))


class Power(base._Widget, base.MarginMixin):
    orientations = base.ORIENTATION_BOTH
    defaults = [
        ("rotate", 0.0, "rotate the image in degrees counter-clockwise"),
    ]

    def __init__(self, length=bar.CALCULATED, **config):
        base._Widget.__init__(self, length, **config)
        self.add_defaults(self.__class__.defaults)
        self.add_defaults(base.MarginMixin.defaults)
        self._variable_defaults["margin"] = 0

    def _configure(self, qtile, pbar):
        base._Widget._configure(self, qtile, pbar)
        self.length = self.calculate_length()

    def draw(self):
        surface = self.drawer
        ctx = surface.ctx

        width, height = self.get_size()

        ctx.move_to(self.offset, width)
        surface.clear(self.background or self.bar.background)
        ctx.save()

        ctx.translate(self.margin_x, self.margin_y)
        ctx.set_fill_rule(cairocffi.FILL_RULE_EVEN_ODD)
        ctx.set_source_rgb(*hex2rgb("#FFFFDD"))
        centerx, centery = width / 2, height / 2
        radius = (width / 2) * 0.6
        ctx.set_line_width(min(height, width) * 0.1)
        ctx.arc_negative(
            centerx,
            centery,
            radius,
            math.radians(230),
            math.radians(310),
        )
        ctx.stroke()
        rect_width = width * 0.1
        rect_height = (height * 0.7) / 2
        ctx.rectangle(
            centerx - (rect_width / 2),
            centery - rect_height,
            rect_width,
            centery * 0.8,
        )
        ctx.fill()

        ctx.restore()

        if self.bar.horizontal:
            surface.draw(
                offsetx=self.offset,
                width=self.width,
            )
        else:
            surface.draw(
                offsety=self.offset,
                height=self.width,
            )

    def get_size(self):
        size = None
        if self.bar.horizontal:
            size = self.bar.height
        else:
            size = self.bar.width

        return size, size

    def calculate_length(self):
        if self.bar.horizontal:
            return self.bar.height + (self.margin_x * 2)
        else:
            return self.bar.width + (self.margin_y * 2)
