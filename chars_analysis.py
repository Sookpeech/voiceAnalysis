def countCharacters(transcripts):
    count = 0
    for x in transcripts:
        for i in range(len(x)):
            if ord('가')<=ord(x[i])<=ord('힣'):
                count+=1
    return count
