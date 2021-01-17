import math
import cairocffi

from libqtile import bar
from libqtile.widget import base
from libqtile.config import Key
from libqtile.utils import rgb
from ... import util


__all__ = [
    'Power',
]


class Power(base._Widget, base.MarginMixin, util.key.KeyMixin):
    orientations = base.ORIENTATION_BOTH
    defaults = [
        ('rotate', 135.0, 'rotate the image in degrees counter-clockwise'),
        ('line_weight', 0.125, 'how thick the lines should be, by percentage'),
        ('line_color', 'DDDDFF', 'line color'),
    ]

    def __init__(self, *args, length=bar.CALCULATED, **kwargs):
        base._Widget.__init__(self, length, *args, **kwargs)
        self.add_defaults(self.__class__.defaults)
        self.add_defaults(base.MarginMixin.defaults)
        self._variable_defaults['margin'] = 0
        self._pressed = False

    def keys(self):
        return [
            Key(
                [],
                'XF86PowerOff',
                lambda: None,
                desc='Power button',
            ),
        ]

    def draw(self):
        width, height = self.get_size()

        self.drawer.clear(self.background or self.bar.background)
        ctx = self.drawer.new_ctx()

        if self.rotate != 0.0:
            ctx.translate(width/2, height/2)
            ctx.rotate(math.radians(self.rotate))
            ctx.translate(-width/2, -height/2)

        ctx.translate(self.margin_x, self.margin_y)
        ctx.set_fill_rule(cairocffi.FILL_RULE_EVEN_ODD)
        ctx.set_source_rgba(*rgb(self.line_color))
        centerx, centery = width / 2, height / 2
        radius = (width / 2) * 0.6
        ctx.set_line_width(min(height, width) * self.line_weight)
        ctx.arc_negative(
            centerx,
            centery,
            radius,
            math.radians(230),
            math.radians(310),
        )
        ctx.stroke()

        rect_width = width * self.line_weight
        rect_height = (height * 0.7) / 2
        ctx.rectangle(
            centerx - (rect_width / 2),
            centery - rect_height,
            rect_width,
            centery * 0.8,
        )
        ctx.fill()

        if self._pressed:
            offset_x = math.ceil(width * 0.025)
            offset_y = math.ceil(height * 0.025)
        else:
            offset_x = 0
            offset_y = 0

        if self.bar.horizontal:
            self.drawer.draw(
                offsetx=self.offset + offset_x,
                width=self.width,
                offsety=offset_y,
            )
        else:
            self.drawer.draw(
                offsety=self.offset + math.floor(self.offset_y),
                height=self.height,
                offsetx=offset_x,
            )

    def button_press(self, x, y, button):
        if button == 1:
            self._pressed = True
            self.draw()
        return super().button_press(x, y, button)

    def button_release(self, x, y, button):
        self._pressed = False
        self.draw()
        return super().button_release(x, y, button)

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
