import os
import threading
import variables
import simpleaudio


def play_audio():
    wave_obj = simpleaudio.WaveObject.from_wave_file("arcade_music_loop.wav")
    main_audio = wave_obj.play()
    main_audio.wait_done()


def start_loop():
    if not variables.playing:
        variables.playing = True
        variables.audio_thread = threading.Thread(target=loop_play)
        variables.audio_thread.start()


def loop_play():
    while variables.playing:
        play_audio()
