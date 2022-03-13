#!/usr/bin/env python3

from curses import meta
import dbus
import os


from mpris2 import get_players_uri
from mpris2 import Player

players = []

print("Players\n---")
for uri in get_players_uri():
    media_player = Player(dbus_interface_info={'dbus_uri': uri})
    
    metadata = media_player.Metadata
    player = dbus.SessionBus().get_object(uri, '/org/mpris/MediaPlayer2')
    status = status=player.Get('org.mpris.MediaPlayer2.Player', 'PlaybackStatus', dbus_interface='org.freedesktop.DBus.Properties')
    for key, val in media_player.Metadata.items():
        if "xesam:title" not in metadata.keys():
            if status == 'Playing':
                print(f"--{metadata['xesam:url']}| useMarkup=false iconName='media-playback-pause' bash='dbus-send --print-reply --dest={uri} /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.PlayPause' terminal=false")
            else:
                print(f"--{metadata['xesam:url']}| useMarkup=false iconName='media-playback-start' bash='dbus-send --print-reply --dest={uri} /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.PlayPause' terminal=false")

            break
        else:
            if status == 'Playing':
                print(f"--{metadata['xesam:title']}: {metadata['xesam:artist'][0]}| useMarkup=false iconName='media-playback-pause' bash='dbus-send --print-reply --dest={uri} /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.PlayPause' terminal=false")
            else:
                print(f"--{metadata['xesam:title']}: {metadata['xesam:artist'][0]}| useMarkup=false iconName='media-playback-start' bash='dbus-send --print-reply --dest={uri} /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.PlayPause' terminal=false")

            break

    # print("---")