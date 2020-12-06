from box import Box


__all__ = [
    'theme',
]


defaults = Box(
    font='Hack Bold',
    fontsize=36,
    padding=5,
)

foreground = Box(
    color='#DDDDFF',
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
        line_color=foreground.color,
        rotate=0.0,
    ),
    clock=Box(
        format='%H:%M',
    ),
)
