# API: https://aiopen.etri.re.kr/guide_wiseNLU.php#group07
from os import access
from urllib import response
from imports import ACCESS_KEY
import urllib3
import json


def countCharacters(transcript):
    # TODO: 안내 문구
    count = 0
    for i in range(len(transcript)):
        if ord('가')<=ord(x[i])<=ord('힣'):
            count+=1
    return count

def checkClosingRemarks(transcript):
    # TODO: 안내 문구
    openApiURL = "http://aiopen.etri.re.kr:8000/WiseNLU_spoken"
    accessKey = ACCESS_KEY
    analysisCode = "morp"
    text = transcript
    count = 0

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
                count+=1

    return count
    

