# 2023SW_YoutubeDownloader 팀 프로젝트

## 팀 소개
- **팀장:** 김연준
- **팀원:** 신희윤
- **팀원:** 송형준
- **팀원:** 박세영

## 프로젝트 개요
2023년 2학기 공개SW실무 9조는 YouTube 동영상을 다운로드하는 도구를 개발하는 프로젝트를 수행했습니다.

## 사용된 파이썬 코드
프로젝트의 기반이 되는 오픈소스 코드는 [여기](https://github.com/KurtBestor/Hitomi-Downloader/blob/master/src/extractor/youtube_downloader.py)에서 확인할 수 있습니다.

## 프로젝트 설명
프로젝트는 Hitomi-Downloader의 일부 코드를 기반으로 YouTube 동영상을 다운로드하는 도구를 개발했습니다.

### 주요 기능
1. YouTube 동영상 다운로드
2. 빠른 다운로드 및 폴더 즉시 진입 가능
3. 사용자 친화적 단순한 인터페이스

### 코드 예시
```python
# 예시 코드
from youtube_downloader import YouTubeDownloader

# YouTube 동영상 URL
video_url = "https://www.youtube.com/watch?v=LiNXyymCt5I&ab_channel=ChrisCool"

# 다운로더 인스턴스 생성
downloader = YouTubeDownloader()

# 동영상 다운로드
downloader.download(video_url)
