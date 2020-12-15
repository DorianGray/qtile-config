from box import Box


__all__ = [
    'theme',
]


defaults = Box(
    font='Hack Bold',
    foreground='DDDDFF',
    background='1A1A1A',
    padding=7,
)

theme = Box(
    widget_defaults=defaults,
    extension_defaults=defaults,
    wallpaper=Box(
        url='/usr/share/sddm/themes/sugar-candy/Backgrounds/Space.jpg',
        mode='fill',
    ),
    power=Box(
        line_weight=0.1,
        line_color=defaults.foreground,
        rotate=0.0,
    ),
    clock=Box(
        format='%H:%M',
        tooltip_format='%Y/%m/%d',
    ),
    group=Box(
        this_current_screen_border=defaults.foreground,
        this_screen_border=defaults.foreground,
    ),
    tasklist=Box(
        borderwidth=0,
    ),
    systray=Box(
        icon_size=64,
        padding=15,
    ),
    tooltip=Box(
        font_size=36,
        horizontal_padding=15,
        vertical_padding=10,
        **defaults
    ),
)
