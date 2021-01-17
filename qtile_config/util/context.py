import contextlib
from typing import Optional, Tuple
from libqtile.log_utils import logger as default_logger


@contextlib.contextmanager
def log_exception(
    msg: Optional[str] = None,
    types: Optional[Tuple] = None,
    *,
    reraise=False,
    logger=None,
) -> None:
    msg = '' if msg is None else msg
    types = (BaseException, ) if types is None else types
    logger = default_logger if logger is None else logger
    try:
        yield
    except types:
        logger.exception(msg)
        if reraise:
            raise
