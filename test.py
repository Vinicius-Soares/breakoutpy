import simpleaudio
from glob import glob


wave_obj = simpleaudio.WaveObject.from_wave_file(glob("*/arcade_music_loop.wav"))
main_audio = wave_obj.play()
main_audio.wait_done()
