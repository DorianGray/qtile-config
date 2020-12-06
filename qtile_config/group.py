from libqtile.config import Group


__all__ = [
    'groups',
]

groups = [
    Group('Terminal', spawn='alacritty -t Terminal -e tmux-session qtile'),
    Group('Web', spawn='google-chrome'),
]
