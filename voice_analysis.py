# -*- coding: utf-8 -*-

from calendar import c
import pause_detection as pd
import transcribe as ts
import tone_analysis as tone
import chars_analysis as ca
import print_to_user as pr
import wave

import time

def getDurationSec(path):
    audio = wave.open(path)
    frames = audio.getnframes()
    rate = audio.getframerate()
    duration = frames/float(rate)
    return duration

# start time check
start_time = time.time()

# measure pitch from wav file
wav_file_title = "news1"
wav_file_path = ".\\audio_files\\" # wav file path
wav_file_duration = getDurationSec(wav_file_path+wav_file_title+".wav")

gender = "W"

if gender == "W":
    shimmer, jitter = tone.measurePitch(155, 334, "Hertz", wav_file_title, wav_file_path)
else:
    shimmer, jitter = tone.measurePitch(85, 196, "Hertz", wav_file_title, wav_file_path)


# split wav file using pause_detection
chunk_count = pd.splitByPause(wav_file_path, wav_file_title) + 1

# upload all splited wav files to s3
saved_file_count = ts.uploadTos3(wav_file_title, wav_file_path, chunk_count)

# start transcribe 
transcripts = ts.return_transcripts_async(saved_file_count, wav_file_title)

# preprocessing transcripts
result = ca.adjustSpacing(transcripts)

# check speech speed & closing remarks
words_count = 0 # count num of characters
closing_remark_count = 0 # count num of sentences with appropriate closing remarks
print("\n")
print(">>>> 말하기 속도와 맺음말을 분석합니다.")
for i in range(len(result)):
    words_count += ca.countNumOfWords(result[i].checked)
    closing_remark_count += ca.checkClosingRemarks(result[i].checked)

# end time check
end_time = time.time()
print()
print()
print()
print(f">>> 소요시간: {end_time-start_time}")

# print notice for user  
print("[1] 말하기 속도")
pr.printWPM(words_count, wav_file_duration)
print("[2] 맺음말")
pr.printClosingRemarks(closing_remark_count, chunk_count)
print("[3] 목소리 강조")
pr.printTone(shimmer*100, jitter*100, gender)

# delete s3 files and transcribe job
print(">>> deleting transcribe jobs and s3 objects")
ts.deleteTranscribeJob(wav_file_title, saved_file_count)
ts.deleteS3WavFile(wav_file_title)
print(">>> complete!")









