"""
This module contains functions related to the alarm system.
"""
import playsound
import os

def sound_alarm():
    """
    Sound the alarm.
    """
    if os.name == 'posix':
        # Play the default system sound on Mac
        playsound.playsound("/System/Library/Sounds/Glass.aiff")
    elif os.name == 'nt':
        # Play the default system sound on Windows
        playsound(os.path.join(os.environ["WINDIR"], 'Media', 'Alarm01.wav'))

def stop_alarm():
    """
    Stop the alarm.
    """
    pass