from pydub import AudioSegment
from pydub.silence import split_on_silence

def splitByPause(wav_file_path, file_title):
    sound = AudioSegment.from_wav(wav_file_path)
    # split audio file
    chunks = split_on_silence(sound, min_silence_len=500, silence_thresh=-40)

    # save splited files
    for i, chunk in enumerate(chunks):
        output_audio = ".\\audio_files\\"+file_title+"_{0}.wav".format(i)
        print("Export complete: ", output_audio)
        chunk.export(output_audio, format="wav")
