from pytube import YouTube
from pytube.exceptions import PytubeError

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage = (bytes_downloaded / total_size) * 100
    print(f"다운로드 중... {percentage:.2f}% 완료", end='\r', flush=True)


def download_video(youtube_url, download_path, status_callback, update_progress_label, download_format):
    try:
         # YouTube 비디오 객체 생성
        yt = YouTube(youtube_url, on_progress_callback=on_progress)

        status_callback(f'찾는 중: {yt.title}')

        filename = None

        if download_format == "mp4":
            # 영상 포맷 중에서 가장 품질이 좋은 mp4 포맷 선택
            selected_stream = yt.streams.get_highest_resolution()
            filename = f"{yt.title}.mp4"
        elif download_format == "mp3":
            # 오디오 포맷 중에서 가장 품질이 좋은 mp3 포맷 선택
            selected_stream = yt.streams.filter(only_audio=True).first()
            # 파일 이름 설정
            filename = f"{yt.title}.mp3"
        else:
            status_callback("에러: 지원하지 않는 다운로드 형식입니다.")
            return

        # 다운로드 시작
        status_callback(f'다운로드 중: {yt.title}')
        selected_stream.download(download_path, filename=filename)
        status_callback('다운로드 완료!')

    except PytubeError as e:
        if 'invalid' in str(e).lower():
            status_callback('에러: 유효한 YouTube 동영상 URL이 아닙니다.')
        elif 'unavailable' in str(e).lower():
            status_callback('에러: 선택한 동영상은 유효하지 않거나 삭제되었습니다.')
        elif 'private' in str(e).lower():
            status_callback('에러: 선택한 동영상은 비공개 상태입니다.')
        elif 'livestream' in str(e).lower():
            status_callback('에러: 선택한 동영상은 라이브 스트리밍 중이어서 다운로드할 수 없습니다.')
        else:
            status_callback(f'에러: {str(e)}')