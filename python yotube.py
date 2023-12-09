from pytube import YouTube

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage = (bytes_downloaded / total_size) * 100
    print(f"다운로드 중... {percentage:.2f}% 완료", end='\r', flush=True)

def download_video(video_url, save_path='.', resolution='highest'):
    try:
        # YouTube 비디오 객체 생성
        yt = YouTube(video_url, on_progress_callback=on_progress)

        # 사용 가능한 화질 옵션 확인
        available_streams = yt.streams.filter(file_extension='mp4')

        # 사용자가 선택한 화질에 맞는 스트림 선택
        if resolution == 'highest':
            video_stream = available_streams.get_highest_resolution()
        else:
            video_stream = available_streams.filter(res=resolution).first()

        if not video_stream:
            print("선택한 화질이 유효하지 않습니다.")
            return

        # 다운로드
        print("다운로드를 시작합니다...")
        video_stream.download(output_path=save_path)
        print(f"\n다운로드 완료: {yt.title}")

    except Exception as e:
        print(f"\n다운로드 중 오류 발생: {e}")

if __name__ == "__main__":
    video_url = input("다운로드할 유튜브 비디오 URL을 입력하세요: ")
    download_path = input("다운로드할 경로를 입력하세요 (기본값은 현재 디렉토리입니다): ")
    resolution = input("원하는 화질을 선택하세요 (highest 또는 화질 옵션, 기본값은 highest입니다): ")

    if not download_path:
        download_path = '.'

    download_video(video_url, download_path, resolution)
