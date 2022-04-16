import pause_detection as pd
import transcribe as ts
import tone_analysis as tone

# measure pitch from wav file
wav_file_title = "news1"
wav_file_path = ".\\audio_files\\" # wav file path

(localJitter, localShimmer, rapJitter, apq3Shimmer, apq11Shimmer) = tone.measurePitch(155, 334, "Hertz", wav_file_title, wav_file_path)
print(f"localJitter: {localJitter*100}\nlocalShimmer: {localShimmer*100}\nrapJitter: {rapJitter*100}\napq3Shimmer: {apq3Shimmer*100}\napq11Shimmer: {apq11Shimmer*100}")

# split wav file using pause_detection
chunk_count = pd.splitByPause(wav_file_path+wav_file_title+".wav", wav_file_title) + 1

# upload wav files to s3
ts.upload_to_s3(wav_file_title, wav_file_path, chunk_count)

# test transcribe
# ts.transcribe_wav_file(wav_file_title, wav_file_path)