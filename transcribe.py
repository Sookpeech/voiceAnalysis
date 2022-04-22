from msilib.schema import Media
from urllib import request
from ast import literal_eval
import boto3
from botocore.config import Config

bucket_name = "sookpeech-wavfile"

def uploadTos3(wav_file_title, wav_file_path, count):
    s3 = boto3.resource('s3')
    for i in range(count):
        audio = open('{}{}_{}.wav'.format(wav_file_path, wav_file_title, i), 'rb')
        try:
            upload = s3.Bucket(bucket_name).put_object(Key="{}/{}_{}.wav".format(wav_file_title, wav_file_title, i), Body=audio)
        except:
            print("failed to upload wav_file_{} to s3", i)

def transcribeWavFile(wav_file_title, count):
    # Config for transcribe
    my_config = Config(
        region_name = 'ap-northeast-2',
        signature_version = 'v4',
        retries={
            'max_attempts': 5,
            'mode' : 'standard'
        }
    )

    # run transcribe
    transcribe = boto3.client('transcribe', config=my_config)
    job_uri = 'https://s3.ap-northeast-2.amazonaws.com/{}/{}/{}_{}.wav'.format(bucket_name,wav_file_title, wav_file_title, count)
    job_name = '{}_{}'.format(wav_file_title, count)
    transcribe.start_transcription_job(
        TranscriptionJobName = job_name,
        Media={'MediaFileUri': job_uri},
        MediaFormat='wav',
        LanguageCode = 'ko-KR',
        Settings={
            'ShowSpeakerLabels': False
        }
    )

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

    print('transcribe count_{}: {}'.format(count, result_text))

    return result_text


# def deleteTranscribeJob():
#     # delete transcribe job
#     # when you start to run transcribe on the same job-name, it will evoke Badrequest error
#     delete_transcribe = boto3.client('transcribe', config=my_config)
#     res = delete_transcribe.delete_transcription_job(
#         TranscriptionJobName = wav_file_title
#     ) 

#     res['ResponseMetadata']['HTTPStatusCode']=='200'
