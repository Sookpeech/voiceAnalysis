def printTone(localJitter, localShimmer, rapJitter, apq3Shimmer, apq11Shimmer):
    # TODO
    return

def printWPM(count, duration):
    text = "김눈송님의 말하기 속도는 {}입니다.\n김눈송님은 1분당 {}단어를 전달하였으며, 적정 단어 수는 96 이상 124 미만입니다."
    WPM = count/(duration/60)
    if WPM < 96:
        print(text.format("느린 편", WPM))
    elif 96<=WPM<124:
        print(text.format("적정한 편", WPM))
    elif WPM<=124:
        print(text.format("빠른 편", WPM))

def printClosingRemarks(count):
    # TODO
    return 
