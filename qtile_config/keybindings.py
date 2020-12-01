from libqtile.config import (
    Key,
    Drag,
    Click,
)
from libqtile.lazy import lazy


__all__ = [
    "keys",
    "mouse",
    "MOD",
    "CONTROL",
    "SHIFT",
    "ALT",
]


MOD = "mod4"
CONTROL = "control"
SHIFT = "shift"
ALT = "mod1"


keys = [
    # Switch between windows in current stack pane
    Key([MOD], "k", lazy.layout.down(),
        desc="Move focus down in stack pane"),
    Key([MOD], "j", lazy.layout.up(),
        desc="Move focus up in stack pane"),

    # Move windows up or down in current stack
    Key([MOD, CONTROL], "k", lazy.layout.shuffle_down(),
        desc="Move window down in current stack "),
    Key([MOD, CONTROL], "j", lazy.layout.shuffle_up(),
        desc="Move window up in current stack "),

    # Switch window focus to other pane(s) of stack
    Key([MOD], "space", lazy.layout.next(),
        desc="Switch window focus to other pane(s) of stack"),

    # Swap panes of split stack
    Key([MOD, SHIFT], "space", lazy.layout.rotate(),
        desc="Swap panes of split stack"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([MOD, SHIFT], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),

    # Toggle between different layouts as defined below
    Key([MOD], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([ALT], "F4", lazy.window.kill(), desc="Kill focused window"),

    Key([MOD, CONTROL], "r", lazy.restart(), desc="Restart qtile"),
    Key([MOD, CONTROL], "q", lazy.shutdown(), desc="Shutdown qtile"),
    Key([MOD], "r", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),
    Key(
        [CONTROL, ALT],
        "l",
        lazy.spawn("/usr/local/bin/lock-screen"),
        desc="Lock Screen",
    ),
    Key(
        [MOD],
        'Right',
        lazy.screen.next_group(),
        desc="Switch to next group",
    ),
    Key(
        [MOD],
        'Left',
        lazy.screen.prev_group(),
        desc="Switch to previous group",
    ),
    Key(
        [],
        "XF86MonBrightnessDown",
        lazy.spawn("xbacklight -dec 5"),
        desc="Dim screen",
    ),
    Key(
        [],
        "XF86MonBrightnessUp",
        lazy.spawn("xbacklight -inc 5"),
        desc="Dim screen",
    ),
    Key(
        [],
        "Print",
        lazy.spawn("sleep 0.5 && scrot -s"),
        desc="Screenshot",
    ),
    Key(
        [],
        'XF86AudioMute',
        lazy.spawn('amixer set Master toggle'),
        desc="Toggle Mute",
    ),
    Key(
        [],
        'XF86AudioRaiseVolume',
        lazy.spawn('amixer set Master 5%+'),
        desc="Increase volume",
    ),
    Key(
        [],
        'XF86AudioLowerVolume',
        lazy.spawn('amixer set Master 5%-'),
        desc="Decrease volume",
    ),
]

# Drag floating layouts.
mouse = [
    Drag([MOD], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([MOD], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([MOD], "Button2", lazy.window.bring_to_front())
]
