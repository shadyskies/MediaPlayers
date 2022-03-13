#!/usr/bin/env python3

from curses import meta
import dbus
import os


from mpris2 import get_players_uri
from mpris2 import Player

players = []

print("Media\n---")
for uri in get_players_uri():
    media_player = Player(dbus_interface_info={'dbus_uri': uri})
    
    metadata = media_player.Metadata
    for key, val in media_player.Metadata.items():
        if "xesam:title" not in metadata.keys():
            print(f"{metadata['xesam:url']}")
            break
        else:
            print(f"{metadata['xesam:title']}: {metadata['xesam:artist'][0]}")
            break
    # print("---")