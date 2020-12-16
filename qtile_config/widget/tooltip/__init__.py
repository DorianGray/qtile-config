from libqtile.popup import Popup
from libqtile import qtile


class Tooltip(Popup):
    def __init__(self, *args, **kwargs):
        super().__init__(qtile, *args, **kwargs)

    def show(self, x, y, text=None):
        self.x = x
        self.y = y
        if text is not None:
            self.text = text

        width, height = self.layout.layout.get_pixel_size()
        height += self.vertical_padding * 2
        width += self.horizontal_padding * 2
        self.width = width
        self.height = height
        # window must be placed prior to drawing because reasons
        self.place()
        # once placed, we can safely draw to our internal buffer
        self.clear()  # clear with background color
        self.draw_text()
        # once the buffer is filled, we unhide the window and draw to it
        self.unhide()
        self.draw()
