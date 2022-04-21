from calendar import c
import pause_detection as pd
import transcribe as ts
import tone_analysis as tone
import chars_analysis as ca

# measure pitch from wav file
wav_file_title = "news1"
wav_file_path = ".\\audio_files\\" # wav file path

(localJitter, localShimmer, rapJitter, apq3Shimmer, apq11Shimmer) = tone.measurePitch(155, 334, "Hertz", wav_file_title, wav_file_path)

# split wav file using pause_detection
chunk_count = pd.splitByPause(wav_file_path+wav_file_title+".wav", wav_file_title) + 1

# upload all splited wav files to s3
ts.upload_to_s3(wav_file_title, wav_file_path, chunk_count)

# transcribe all splited wav files
transcripts = []
for i in range(chunk_count):
    transcript = ts.transcribe_wav_file(wav_file_title, i)
    transcripts.append(transcript)

# check speech speed & closing remarks
for transcript in transcripts:
    ca.countCharacters(transcript)
    ca.checkClosingRemarks(transcript)