from scipy.io import wavfile
from copy import deepcopy
from scipy.ndimage import gaussian_filter
from numpy import concatenate

# Names of the files
music_filename = "music.wav"
voice_filename = "voice.wav"
# Reads wav files, here we suppose the rates are the same (fsm == fsv)
fsm, music = wavfile.read(music_filename)
fsv, voice = wavfile.read(voice_filename)
# Voice start time >= 1 here
start_second = 9
# Starts index of the voice
start_index = start_second * fsm
# Blur parameters
# Here, one level of blur crescendo lasts 0.1 second
blur_crescendo_level_range = fsm // 5
# Final sigma of blur function
blur_sigma = 6
# Number of levels of the blur crescendo
blur_crescendo_levels = blur_sigma - 1
# Makes a copy of the read-only array normal beginning
simple_data = deepcopy(music)
data = deepcopy(music[:start_index - blur_crescendo_level_range * blur_crescendo_levels])
# Adds the blur crescendo
for level in range(blur_crescendo_levels):
    # Start index of the level
    blur_start = start_index - blur_crescendo_level_range * (blur_crescendo_levels - level)
    data = concatenate((data, 
                        gaussian_filter(data[blur_start:blur_start + blur_crescendo_level_range], sigma = level + 1)),
                        axis = 0)
# Adds the blured music with the normal end
data = concatenate((data, 
                    gaussian_filter(music[start_index:start_index + len(voice)], sigma = blur_sigma), 
                    music[start_index + len(voice):]),
                    axis=0)

# Superimpose voice to music
for i in range(len(voice)):
    # Passing to int to avoid data overflow
    data[start_index + i] = (int(data[start_index + i][0]) + voice[i][0]) // 2
    simple_data[start_index + i] = (int(simple_data[start_index + i][0]) + voice[i][0]) // 2

# Exports new wav files
wavfile.write('output_without_blur.wav', fsm, simple_data)
wavfile.write('output_with_blur.wav', fsm, data)

print("Done.")