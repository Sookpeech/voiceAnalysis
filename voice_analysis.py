# -*- coding: utf-8 -*-

from calendar import c
import pause_detection as pd
import transcribe as ts
import tone_analysis as tone
import chars_analysis as ca
import print_to_user as pr
import wave

def getDurationSec(path):
    audio = wave.open(path)
    frames = audio.getnframes()
    rate = audio.getframerate()
    duration = frames/float(rate)
    return duration

# measure pitch from wav file
wav_file_title = "news1"
wav_file_path = ".\\audio_files\\" # wav file path
wav_file_duration = getDurationSec(wav_file_path+wav_file_title+".wav")

localShimmer, rapJitter = tone.measurePitch(155, 334, "Hertz", wav_file_title, wav_file_path)

# split wav file using pause_detection
chunk_count = pd.splitByPause(wav_file_path, wav_file_title) + 1

# upload all splited wav files to s3
saved_file_count = ts.uploadTos3(wav_file_title, wav_file_path, chunk_count)

# transcribe all splited wav files
transcripts = []
for i in range(saved_file_count):
    transcript = ts.transcribeWavFile(wav_file_title, i)
    transcripts.append(transcript)

# check speech speed & closing remarks
words_count = 0 # count num of characters
closing_remark_count = 0 # count num of sentences with appropriate closing remarks
for transcript in transcripts:
    words_count += ca.countNumOfWords(transcript)
    closing_remark_count += ca.checkClosingRemarks(transcript)

# print notice for user  
print("[1] 말하기 속도")
pr.printWPM(words_count, wav_file_duration)
print("[2] 맺음말")
pr.printClosingRemarks(closing_remark_count, chunk_count)
print("[3] 목소리 강조")
pr.printTone(localShimmer*100, rapJitter*100)

# delete s3 files and transcribe job
ts.deleteTranscribeJob(wav_file_title, saved_file_count)
ts.deleteS3WavFile("news1")