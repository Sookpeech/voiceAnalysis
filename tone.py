# !pip install praat-parselmouth
# !pip install pydub

import parselmouth
from parselmouth.praat import call

import pause_detection as pd
import transcribe as ts

# measure pitch
def measurePitch(voiceID, f0min, f0max, unit):
    sound = parselmouth.Sound(voiceID) # read the sound
    pointProcess = call(sound, "To PointProcess (periodic, cc)", f0min, f0max)
    localJitter = call(pointProcess, "Get jitter (local)", 0, 0, 0.0001, 0.02, 1.3)
    rapJitter = call(pointProcess, "Get jitter (rap)", 0, 0, 0.0001, 0.02, 1.3)
    localShimmer =  call([sound, pointProcess], "Get shimmer (local)", 0, 0, 0.0001, 0.02, 1.3, 1.6)
    apq3Shimmer = call([sound, pointProcess], "Get shimmer (apq3)", 0, 0, 0.0001, 0.02, 1.3, 1.6)
    apq11Shimmer =  call([sound, pointProcess], "Get shimmer (apq11)", 0, 0, 0.0001, 0.02, 1.3, 1.6)

    return localJitter, localShimmer, rapJitter, apq3Shimmer, apq11Shimmer

# measure pitch from wav file
wav_file_title = "news1"
wav_file_path = ".\\audio_files\\" # wav file path

sound = parselmouth.Sound(wav_file_path+wav_file_title+".wav")
(localJitter, localShimmer, rapJitter, apq3Shimmer, apq11Shimmer) = measurePitch(sound, 155, 334, "Hertz")
print(f"localJitter: {localJitter*100}\nlocalShimmer: {localShimmer*100}\nrapJitter: {rapJitter*100}\napq3Shimmer: {apq3Shimmer*100}\napq11Shimmer: {apq11Shimmer*100}")

# split wav file using pause_detection
pd.splitByPause(wav_file_path+wav_file_title+".wav", wav_file_title)

# test transcribe
ts.transcribe_wav_file(wav_file_title, wav_file_path)
