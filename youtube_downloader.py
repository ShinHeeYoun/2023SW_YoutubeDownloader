# youtube_downloader.py

from pytube import YouTube, exceptions
from tkinter import filedialog

def download_youtube_video(url, download_path, status_callback):
    try:
        # YouTube 객체 생성
        yt = YouTube(url)

        # 영상 포맷 중에서 가장 품질이 좋은 포맷 선택
        video = yt.streams.get_highest_resolution()

        # 다운로드 시작
        # status_callback(f'다운로드 중: {yt.title}')
        video.download(download_path)
        # status_callback('다운로드 완료!')

    except exceptions.RegexMatchError:
        status_callback('에러: 올바른 유튜브 동영상 URL이 아닙니다. 올바른 URL을 입력하십시오.')
    except exceptions.VideoUnavailable:
        status_callback('에러: 선택한 동영상은 다운로드할 수 없습니다. 다른 동영상을 시도하십시오.')
    except Exception as e:
        status_callback(f'에러: {str(e)}')
