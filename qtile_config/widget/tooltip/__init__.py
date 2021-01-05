from libqtile.popup import Popup
from libqtile import qtile


class Tooltip(Popup):
    def __init__(self, *args, **kwargs):
        super().__init__(qtile, *args, **kwargs)

    def show(self):
        self.width = self.layout.width + self.horizontal_padding * 2
        self.height = self.layout.height + self.vertical_padding * 2

        self.clear()
        self.draw_text()
        self.place()
        self.unhide()
        self.draw()
