import os
import threading
import variables
import simpleaudio


def play_audio():
    variables.main_theme = variables.wave_obj.play()
    variables.main_theme.wait_done()


def start_loop():
    variables.playing = True
    variables.audio_thread = threading.Thread(target=loop_play, daemon=True)
    variables.audio_thread.start()


def loop_play():
    while variables.playing:
        play_audio()


def stop_play():
    variables.playing = False
    simpleaudio.stop_all()
