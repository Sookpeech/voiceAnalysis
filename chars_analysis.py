# API: https://aiopen.etri.re.kr/guide_wiseNLU.php#group07
from os import access
from urllib import response
from imports import ACCESS_KEY
import urllib3
import json


def countCharacters(transcripts):
    count = 0
    for x in transcripts:
        for i in range(len(x)):
            if ord('가')<=ord(x[i])<=ord('힣'):
                count+=1
    return count

def checkClosingRemarks():
    openApiURL = "http://aiopen.etri.re.kr:8000/WiseNLU_spoken"
    accessKey = ACCESS_KEY
    analysisCode = "morp"
    text = "안녕하세요, 저는 조은비이며 굉장히 지쳐있습니다."

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

    return_objects = json.loads(response.data)['return_object']
    sentences = return_objects["sentence"]
    morps = sentences[0]["morp"]
    for morp in morps:
        if morp["type"]=="EF":
            print(morp)
        elif morp["type"]=="EC" and morp["lemma"][-1]=="요":
            print(morp)

    

