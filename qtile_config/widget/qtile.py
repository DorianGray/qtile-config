from libqtile.lazy import lazy
from libqtile.config import Key
from .mixin import KeyMixin
from ..util.key import (
    MOD,
    CONTROL,
    ALT,
    SHIFT,
)


__all__ = [
    'QTile',
]


class QTile(KeyMixin):
    def keys(self):
        return [
            # Switch between windows in current stack pane
            Key(
                [MOD],
                'k',
                lazy.layout.down(),
                desc='Move focus down in stack pane',
            ),
            Key(
                [MOD],
                'j',
                lazy.layout.up(),
                desc='Move focus up in stack pane',
            ),

            # Move windows up or down in current stack
            Key(
                [MOD, CONTROL],
                'k',
                lazy.layout.shuffle_down(),
                desc='Move window down in current stack',
            ),
            Key(
                [MOD, CONTROL],
                'j',
                lazy.layout.shuffle_up(),
                desc='Move window up in current stack',
            ),

            # Switch window focus to other pane(s) of stack
            Key(
                [MOD],
                'space',
                lazy.layout.next(),
                desc='Switch window focus to other pane(s) of stack',
            ),

            # Swap panes of split stack
            Key(
                [MOD, SHIFT],
                'space',
                lazy.layout.rotate(),
                desc='Swap panes of split stack',
            ),

            # Toggle between split and unsplit sides of stack.
            # Split = all windows displayed
            # Unsplit = 1 window displayed, like Max layout, but still with
            # multiple stack panes
            Key(
                [MOD, SHIFT],
                'Return',
                lazy.layout.toggle_split(),
                desc='Toggle between split and unsplit sides of stack',
            ),

            # Toggle between different layouts as defined below
            Key(
                [MOD],
                'Tab',
                lazy.next_layout(),
                desc='Toggle between layouts',
            ),
            Key(
                [ALT],
                'F4',
                lazy.window.kill(),
                desc='Kill focused window',
            ),

            Key(
                [MOD, CONTROL],
                'r',
                lazy.restart(),
                desc='Restart qtile',
            ),
            Key(
                [MOD, CONTROL],
                'q',
                lazy.shutdown(),
                desc='Shutdown qtile',
            ),
            Key(
                [MOD],
                'r',
                lazy.spawncmd(),
                desc='Spawn a command using a prompt widget',
            ),
            Key(
                [CONTROL, ALT],
                'l',
                lazy.spawn('/usr/local/bin/lock-screen'),
                desc='Lock Screen',
            ),
            Key(
                [MOD],
                'Right',
                lazy.screen.next_group(),
                desc='Switch to next group',
            ),
            Key(
                [MOD],
                'Left',
                lazy.screen.prev_group(),
                desc='Switch to previous group',
            ),
        ]
