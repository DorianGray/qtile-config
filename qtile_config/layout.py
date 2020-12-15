from libqtile import layout
from libqtile.config import Match


__all__ = [
    'floating_layout',
    'layouts',
]


layouts = [
    layout.Max(),
    layout.Tile(),
]


floating_layout = layout.Floating(float_rules=[
    Match(wm_class='confirm'),
    Match(wm_class='dialog'),
    Match(wm_class='download'),
    Match(wm_class='error'),
    Match(wm_class='file_progress'),
    Match(wm_class='notification'),
    Match(wm_class='splash'),
    Match(wm_class='toolbar'),
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),
    Match(wm_class='maketag'),
    Match(title='branchdialog'),
    Match(title='pinentry'),  # GPG key password entry
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(wm_class='Steam'),  # Steam
    Match(title='Steam'),
    Match(wm_class='qgui'),  # qgui
])
