import os
import threading
import variables
import simpleaudio

# simpleaudio.stop_all()


def play_audio():
    path = os.path.abspath("arcade_music_loop.wav")
    wave_obj = simpleaudio.WaveObject.from_wave_file(path)
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
