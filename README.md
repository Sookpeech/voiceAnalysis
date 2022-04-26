# Sookpeech/voice_analysis

**for Notice**  
[<img src="https://img.shields.io/badge/Notion-000000?style=for-the-badge&logo=Notion&logoColor=white">](https://plaid-fireman-f9d.notion.site/Sookpeech-voice_analysis-ddcea176a96e44e180580da27fe1855a)

| python file | content |
| --- | --- |
| voice_analysis.py | (main) .wav 파일을 가져온 후 외부 함수 실행 |
| pause_detection.py | pause를 기준으로 .wav 파일을 여러 개로 나누어 export |
| transcribe.py | AWS s3에 나누어진 .wav 파일 업로드, s3 내의 파일들 transcribe 실행 |
| tone_analysis.py | Praat 라이브러리 이용, 목소리 크기/높낮이 강조점 분석 |
| chars_analysis.py | 단어 수 계산, 맺음말 분석 |
| print_to_user.py | 분석 결과 값을 기준과 비교한 후 사용자에게 출력 |

