import os
import asyncio
from libqtile import hook
from .util.sync import await_sync


__all__ = []


DISPLAY = os.getenv('DISPLAY', None)
HOME = os.getenv('HOME', None)


@hook.subscribe.startup_once
@await_sync
async def _autostart():
    await asyncio.create_subprocess_exec(
        "compton",
        "--config",
        "{}/.config/compton/compton.conf".format(HOME),
        "-dbus",
        "-d",
        DISPLAY,
    )
    await asyncio.create_subprocess_exec(
        "xautolock",
        "-time",
        "10",
        "-detectsleep",
        "-locker",
        "/usr/local/bin/xautolocker",
    )
    await asyncio.create_subprocess_exec("unclutter", "-root")
