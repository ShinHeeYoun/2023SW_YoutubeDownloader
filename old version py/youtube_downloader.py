import tkinter as tk
from tkinter import filedialog
from pytube import YouTube
import threading
from ttkthemes import ThemedTk

def download_youtube_video():
    def download():
        try:
            # 유튜브 영상 URL을 입력 받음
            youtube_url = url_entry.get()

            # 다운로드 위치 선택
            download_path = filedialog.askdirectory()

            # YouTube 객체 생성
            yt = YouTube(youtube_url)

            # 영상 포맷 중에서 가장 품질이 좋은 포맷 선택
            video = yt.streams.get_highest_resolution()

            # 다운로드 시작
            status_label.config(text=f'다운로드 중: {yt.title}')
            video.download(download_path)
            status_label.config(text='다운로드 완료!')

        except Exception as e:
            status_label.config(text='에러: 입력이 잘못되었습니다. 올바른 유튜브 동영상 URL을 입력하십시오.')

    # 쓰레드 생성 및 시작
    download_thread = threading.Thread(target=download)
    download_thread.start()

# GUI 생성
app = ThemedTk(theme="plastik")  # You can change the theme here
app.title('YouTube Downloader')

# 레이블과 엔트리 위젯 추가
url_label = tk.Label(app, text='Enter YouTube Video URL:', font=('Helvetica', 12))
url_label.grid(row=0, column=0, pady=10, padx=10)  # padx 옵션 추가

url_entry = tk.Entry(app, width=40, font=('Helvetica', 12))
url_entry.grid(row=0, column=1, pady=10)

# Download 버튼을 URL 입력 창 바로 오른쪽에 위치
download_button = tk.Button(app, text='Download', command=download_youtube_video, font=('Helvetica', 12))
download_button.grid(row=0, column=2, padx=20, pady=20)  # padx 옵션 추가

# 상태 표시 레이블 추가
status_label = tk.Label(app, text='', font=('Helvetica', 12))
status_label.grid(row=1, column=0, columnspan=3, pady=10)

# GUI 실행
app.mainloop()
