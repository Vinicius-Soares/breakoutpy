import os
import simpleaudio

playing = False
audio_thread = None
path = os.path.abspath("sounds/arcade_music_loop.wav")
wave_obj = simpleaudio.WaveObject.from_wave_file(path)
main_theme = wave_obj.play()
