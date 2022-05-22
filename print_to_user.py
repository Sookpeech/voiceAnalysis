w_jitter_up = 2.310
w_jitter_down = 1.599
w_shimmer_up = 12.221
w_shimmer_down = 7.393

m_jitter_up = 3.023
m_jitter_down = 2.159
m_shimmer_up = 13.526
m_shimmer_down = 10.132

def printWomenTone(shimmer, jitter):
    # shimmer
    shimmer_text = "※사용자님의 목소리 크기 변화율은 {:.3f}%로 크기 변화폭이 {} 편입니다.\n 여성의 평균적인 변화율은 {}% ~ {}%입니다.\n"
    if shimmer<=w_shimmer_up and w_shimmer_down<=shimmer:
        print(shimmer_text.format(shimmer, "적당한", w_shimmer_down, w_shimmer_up)+"\n")
    elif shimmer <= w_shimmer_down:
        print(shimmer_text.format(shimmer, "작은",  w_shimmer_down, w_shimmer_up)+" 목소리 크기 변화가 적은 경우 좋은 내용이 지루하게 들릴 가능성이 있습니다.\n")
    else:
        print(shimmer_text.format(shimmer, "큰", w_shimmer_down, w_shimmer_up)+" 목소리 크기 변화가 과도하게 큰 경우 오히려 전달력이 떨어질 가능성이 있습니다.\n")
    
    # jitter
    jitter_text = "※사용자님의 목소리 높낮이 변화율은 {:.3f}%으로 높낮이 변화폭이 {} 편입니다.\n 여성의 평균적인 변화율은 {}% ~ {}%입니다.\n"
    if jitter<=w_jitter_up and w_jitter_down<=jitter:
        print(jitter_text.format(jitter, "적당한", w_jitter_down, w_jitter_up)+"\n")
    elif jitter <= w_jitter_down:
        print(jitter_text.format(jitter, "작은",  w_jitter_down, w_jitter_up)+" 목소리 크기 변화가 적은 경우 좋은 내용이 지루하게 들릴 가능성이 있습니다.\n")
    else:
        print(jitter_text.format(jitter, "큰", w_jitter_down, w_jitter_up)+" 목소리 크기 변화가 과도하게 큰 경우 오히려 전달력이 떨어질 가능성이 있습니다.\n")

def printMenTone(shimmer, jitter):
    # shimmer
    shimmer_text = "※사용자님의 목소리 크기 변화율은 {:.3f}%로 크기 변화폭이 {} 편입니다.\n남성의 평균적인 변화율은 {}% ~ {}%입니다.\n"
    if shimmer<=m_shimmer_up and m_shimmer_down<=shimmer:
        print(shimmer_text.format(shimmer, "적당한", m_shimmer_down, m_shimmer_up)+"\n")
    elif shimmer <= m_shimmer_down:
        print(shimmer_text.format(shimmer, "작은",  m_shimmer_down, m_shimmer_up)+" 목소리 크기 변화가 적은 경우 좋은 내용이 지루하게 들릴 가능성이 있습니다.\n")
    else:
        print(shimmer_text.format(shimmer, "큰", m_shimmer_down, m_shimmer_up)+" 목소리 크기 변화가 과도하게 큰 경우 오히려 전달력이 떨어질 가능성이 있습니다.\n")
    
    # jitter
    jitter_text = "※사용자님의 목소리 높낮이 변화율은 {:.3f}%으로 높낮이 변화폭이 {} 편입니다.\n남성의 평균적인 변화율은 {}% ~ {}%입니다.\n"
    if jitter<=m_jitter_up and m_jitter_down<=jitter:
        print(jitter_text.format(jitter, "적당한", m_jitter_down, m_jitter_up)+"\n")
    elif jitter <= m_jitter_down:
        print(jitter_text.format(jitter, "작은",  m_jitter_down, m_jitter_up)+" 목소리 크기 변화가 적은 경우 좋은 내용이 지루하게 들릴 가능성이 있습니다.\n")
    else:
        print(jitter_text.format(jitter, "큰", m_jitter_down, m_jitter_up)+" 목소리 크기 변화가 과도하게 큰 경우 오히려 전달력이 떨어질 가능성이 있습니다.\n")

def printTone(shimmer, jitter, gender):
    if gender == "W":
        printWomenTone(shimmer, jitter)
    else:
        printMenTone(shimmer, jitter)


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
