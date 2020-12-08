import cairocffi


__all__ = [
    'get_surface_size',
    'duplicate_surface',
    'grayscale',
    'darken',
]


def get_surface_size(surface):
    x, y, w, h = cairocffi.Context(surface).clip_extents()
    return int(w - x), int(h - y)


def duplicate_surface(surface):
    width, height = get_surface_size(surface)
    new_surface = surface.create_similar(
        surface.get_content(),
        width,
        height,
    )
    ctx = cairocffi.Context(new_surface)
    ctx.set_source_surface(surface, 0, 0)
    ctx.operator = cairocffi.OPERATOR_SOURCE
    ctx.paint()
    return new_surface


def grayscale(surface):
    width, height = get_surface_size(surface)
    pattern = cairocffi.SurfacePattern(surface)
    ctx = cairocffi.Context(surface)
    ctx.rectangle(0, 0, width, height)
    ctx.set_source_rgb(0, 0, 0)
    ctx.set_operator(cairocffi.OPERATOR_HSL_SATURATION)
    ctx.mask(pattern)


def darken(surface, percent):
    ctx = cairocffi.Context(surface)
    ctx.set_source_rgba(0, 0, 0, percent)
    ctx.set_operator(cairocffi.OPERATOR_ATOP)
    ctx.paint()
