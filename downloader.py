# downloader.py

from pytube import YouTube

def download_video(youtube_url, download_path, status_callback):
    try:
        # YouTube 객체 생성
        yt = YouTube(youtube_url)

        # 영상 포맷 중에서 가장 품질이 좋은 포맷 선택
        video = yt.streams.get_highest_resolution()

        # 다운로드 시작
        status_callback(f'다운로드 중: {yt.title}')
        video.download(download_path)
        status_callback('다운로드 완료!')

    except Exception as e:
        status_callback('에러: 입력이 잘못되었습니다. 올바른 유튜브 동영상 URL을 입력하십시오.')
