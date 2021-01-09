from libqtile.config import Group


__all__ = [
    'groups',
]

groups = [
    Group(' ', spawn='alacritty -t Terminal -e tmux-session qtile'),
    Group('', spawn='google-chrome'),
]
