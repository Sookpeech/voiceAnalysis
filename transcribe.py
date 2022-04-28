from msilib.schema import Media
from urllib import request
from ast import literal_eval
import boto3
from botocore.config import Config
import wave

transcripts = []
bucket_name = "sookpeech-wavfile"

# Config for transcribe
my_config = Config(
    region_name = 'ap-northeast-2',
    signature_version = 'v4',
    retries={
        'max_attempts': 5,
        'mode' : 'standard'
     }
)

def uploadTos3(wav_file_title, wav_file_path, count):
    s3 = boto3.resource('s3')
    save_cnt = 0
    for i in range(count):
        file = '{}{}_{}.wav'.format(wav_file_path, wav_file_title, i)
        # if duration of wav file is shorter than 1 sec, do not upload
        if getDurationChunk(file)<=1.0:
            continue
        audio = open(file, 'rb')
        try:
            upload = s3.Bucket(bucket_name).put_object(Key="{}/{}_{}.wav".format(wav_file_title, wav_file_title, save_cnt), Body=audio)
            save_cnt+=1
        except:
            print("failed to upload wav_file_{} to s3", save_cnt)

    return save_cnt

# create transcribe jobs for splited wav files and get transcribe results
def return_transcripts_async(saved_file_count, wav_file_title):
    global transcripts

    transcribe = boto3.client('transcribe', config=my_config)
    for i in range(saved_file_count):
        transcribeWavFile(wav_file_title, i, transcribe)

    for i in range(saved_file_count):
        getTranscribeResult(wav_file_title, i, transcribe)

    return transcripts

# create transcribe jobs for splited wav files
def transcribeWavFile(wav_file_title, count, transcribe):

    # run transcribe
    job_uri = 'https://s3.ap-northeast-2.amazonaws.com/{}/{}/{}_{}.wav'.format(bucket_name,wav_file_title, wav_file_title, count)
    job_name = '{}_{}'.format(wav_file_title, count)

    print(f">>> transcirbe job <{job_name}> start!")
    transcribe.start_transcription_job(
        TranscriptionJobName = job_name,
        Media={'MediaFileUri': job_uri},
        MediaFormat='wav',
        LanguageCode = 'ko-KR',
        Settings={
            'ShowSpeakerLabels': False
        }
    )
    print(f">>> transcirbe job <{job_name}> started!")

# get transcribe results
def getTranscribeResult(wav_file_title, count, transcribe):
    global transcripts
    job_name = '{}_{}'.format(wav_file_title, count)
    print(f">>> transcirbe job <{job_name}> try to get!")

    # check transcription compeleted or failed
    while True:
        status = transcribe.get_transcription_job(TranscriptionJobName = job_name)
        if status['TranscriptionJob']['TranscriptionJobStatus'] in ['COMPLETED', 'FAILED']:
            save_json_uri = status['TranscriptionJob']['Transcript']['TranscriptFileUri']
            break
    save_json_uri = status['TranscriptionJob']['Transcript']['TranscriptFileUri']

    # browse transcribe result
    load = request.urlopen(save_json_uri)
    confirm = load.status
    result = load.read().decode('utf-8')
    result_text = literal_eval(result)['results']['transcripts'][0]['transcript']

    print(f">>> transcirbe job <{job_name}> end to get!")
    transcripts.append(result_text)


def deleteTranscribeJob(wav_file_title, count):
    # delete transcribe job
    # when you start to run transcribe on the same job-name, it will evoke Badrequest error
    delete_transcribe = boto3.client('transcribe', config=my_config)
    for i in range(count):
        job_name = '{}_{}'.format(wav_file_title, i)
        res = delete_transcribe.delete_transcription_job(
            TranscriptionJobName = job_name
        ) 

def deleteS3WavFile(wav_file_title):
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucket_name)
    bucket.objects.filter(Prefix=wav_file_title).delete()

def getDurationChunk(path):
    audio = wave.open(path)
    frames = audio.getnframes()
    rate = audio.getframerate()
    duration = frames/float(rate)
    return duration