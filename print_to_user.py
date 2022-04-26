local_shimmer_std = 3.810
rap_jitter_std = 0.680

def printTone(localShimmer, rapJitter):
    text_shimmer = "※사용자님의 목소리 크기 변화율은 {:.3f}%으로 크기 변화가 {} 편입니다.\n적당한 크기 강조 변화율은 {}%입니다."
    if localShimmer<local_shimmer_std:
        print(text_shimmer.format(localShimmer, "적은", local_shimmer_std))
    else:
        print(text_shimmer.format(localShimmer, "적당한", local_shimmer_std))
    
    text_jitter = "※사용자님의 목소리 높낮이 변화율은 {:.3f}%으로 높낮이 변화가 {} 편입니다.\n적당한 높낮이 변화율은 {}%입니다.\n"
    if rapJitter<rap_jitter_std:
        print(text_jitter.format(rapJitter, "적은", rap_jitter_std))
    else:
        print(text_jitter.format(rapJitter, "적당한", rap_jitter_std))

def printWPM(count, duration):
    text = "※사용자님의 말하기 속도는 {}입니다.\n※김눈송님은 1분당 {:.1f}단어를 전달하였으며, 적정 단어 수는 96 이상 124 미만입니다.\n"
    WPM = count/(duration/60)
    if WPM < 96:
        print(text.format("느린 편", WPM))
    elif 96<=WPM<124:
        print(text.format("적정한 편", WPM))
    elif WPM<=124:
        print(text.format("빠른 편", WPM))

def printClosingRemarks(count, total_count):
    text = "※사용자님이 발화하신 {}문장 중 {:.1f}%의 맺음말이 정확히 인식되었습니다.\n"
    print(text.format(total_count, (count/total_count)*100))
