import sys
import qtile_config


__all__ = qtile_config.__all__


module = sys.modules[__name__]
for prop in __all__:
    setattr(module, prop, getattr(qtile_config, prop))
