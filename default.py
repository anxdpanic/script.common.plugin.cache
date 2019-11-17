"""
    Cache service for Kodi
    Version 0.8

    Copyright (C) 2010-2011 Tobias Ussing And Henrik Mosgaard Jensen
    Copyright (C) 2019 anxdpanic

    This file is part of script.common.plugin.cache

    SPDX-License-Identifier: GPL-3.0-only
    See LICENSES/GPL-3.0-only.txt for more information.
"""

import sys
import xbmc
import xbmcaddon
import xbmcvfs

settings = xbmcaddon.Addon(id='script.common.plugin.cache')
dbg = settings.getSetting("debug") == "true"
dbglevel = 3


def run():
    sys.path = [settings.getAddonInfo('path') + "/lib"] + sys.path
    import StorageServer
    s = StorageServer.StorageServer(False)
    xbmc.log(" StorageServer Module loaded RUN")
    xbmc.log(s.plugin + " Starting server")
    s.run()
    return True


if __name__ == "__main__":
    if settings.getSetting("autostart") == "true":
        run()
