# !pip install praat-parselmouth
# !pip install pydub

import parselmouth
from parselmouth.praat import call

# measure pitch
def measurePitch(f0min, f0max, unit, wav_file_title, wav_file_path):
    voiceID = parselmouth.Sound(wav_file_path+wav_file_title+".wav")
    sound = parselmouth.Sound(voiceID) # read the sound
    pointProcess = call(sound, "To PointProcess (periodic, cc)", f0min, f0max)
    localJitter = call(pointProcess, "Get jitter (local)", 0, 0, 0.0001, 0.02, 1.3)
    rapJitter = call(pointProcess, "Get jitter (rap)", 0, 0, 0.0001, 0.02, 1.3)
    localShimmer =  call([sound, pointProcess], "Get shimmer (local)", 0, 0, 0.0001, 0.02, 1.3, 1.6)
    apq3Shimmer = call([sound, pointProcess], "Get shimmer (apq3)", 0, 0, 0.0001, 0.02, 1.3, 1.6)
    apq11Shimmer =  call([sound, pointProcess], "Get shimmer (apq11)", 0, 0, 0.0001, 0.02, 1.3, 1.6)

    return localJitter, localShimmer, rapJitter, apq3Shimmer, apq11Shimmer