# API: https://aiopen.etri.re.kr/guide_wiseNLU.php#group07
from imports import ACCESS_KEY
from hanspell import spell_checker
import urllib3
import json

def adjustSpacing(transcripts):
    new_transcripts = []

    for i in range(len(transcripts)):
        print(">>>> sentence ["+str(i+1)+"]")
        print(">>>> old_sentence: ["+transcripts[i]+"]")
        new_sent = transcripts[i].replace(" ", '')
        print(">>>> sub_sentence: ["+new_sent+"]")
        new_transcripts.append(new_sent)

    result = spell_checker.check(transcripts)

    for i in range(len(transcripts)):
        print(">>>> new_sentence: ["+result[i].checked+"]")

    return result



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
    

