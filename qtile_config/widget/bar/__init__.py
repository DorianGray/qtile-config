from libqtile import bar
from libqtile.lazy import lazy
from libqtile.config import Key
from ..mixin import KeyMixin


class Bar(bar.Bar, KeyMixin):
    def keys(self):
        return [
            Key(
                [],
                'XF86MonBrightnessDown',
                lazy.spawn('xbacklight -dec 5'),
                desc='Dim screen',
            ),
            Key(
                [],
                'XF86MonBrightnessUp',
                lazy.spawn('xbacklight -inc 5'),
                desc='Dim screen',
            ),
            Key(
                [],
                'Print',
                lazy.spawn('sleep 0.5 && scrot -s'),
                desc='Screenshot',
            ),
            Key(
                [],
                'XF86AudioMute',
                lazy.spawn('amixer set Master toggle'),
                desc='Toggle Mute',
            ),
            Key(
                [],
                'XF86AudioRaiseVolume',
                lazy.spawn('amixer set Master 5%+'),
                desc='Increase volume',
            ),
            Key(
                [],
                'XF86AudioLowerVolume',
                lazy.spawn('amixer set Master 5%-'),
                desc='Decrease volume',
            ),
        ]
