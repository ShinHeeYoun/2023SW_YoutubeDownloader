# main.py

from youtube_downloader import download_youtube_video
from view import create_gui

def main():
    # GUI에서 다운로드 콜백을 호출하도록 함
    create_gui(download_youtube_video)

if __name__ == "__main__":
    main()
