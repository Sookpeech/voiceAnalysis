# API: https://aiopen.etri.re.kr/guide_wiseNLU.php#group07
from os import access
from urllib import response
from imports import ACCESS_KEY
import urllib3
import json
import wave

def getDurationSec(path):
    audio = wave.open(path)
    frames = audio.getnframes()
    rate = audio.getframerate()
    duration = frames/float(rate)
    return duration

def countNumOfWords(transcript):
    count = 0
    for i in range(len(transcript)):
        if transcript[i]==" ":
            count+=1
    return count+1

def checkClosingRemarks(transcript):
    openApiURL = "http://aiopen.etri.re.kr:8000/WiseNLU_spoken"
    accessKey = ACCESS_KEY
    analysisCode = "morp"
    text = transcript
    result = False

    requestJson = {
        "access_key": accessKey,
        "argument": {
            "text" : text,
            "analysis_code": analysisCode
        }
    }

    http = urllib3.PoolManager()
    response = http.request(
        "POST",
        openApiURL,
        headers={"Content-Type": "application/json; charset=UTF-8"},
        body = json.dumps(requestJson)
    )

    # check closing remarks are appropriate
    return_objects = json.loads(response.data)['return_object']
    sentences = return_objects["sentence"]
    morps = sentences[0]["morp"]
    for morp in morps:
        if morp["type"]=="EF" or (morp["type"]=="EC" and morp["lemma"][-1]=="요"):
            if morp["position"] >= len(text.encode())-10: #TODO: 맺음말 위치 확인
                result = True

    return result
    

