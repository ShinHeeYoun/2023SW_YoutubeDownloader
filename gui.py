# gui.py

import tkinter as tk
from tkinter import filedialog
import threading
from downloader import download_video

def download_youtube_video():
    def download():
        # 유튜브 영상 URL을 입력 받음
        youtube_url = url_entry.get()

        # 다운로드 위치 선택
        download_path = filedialog.askdirectory()

        # 다운로드 함수 호출
        download_video(youtube_url, download_path, update_status_label)

    # 쓰레드 생성 및 시작
    download_thread = threading.Thread(target=download)
    download_thread.start()

def update_status_label(status):
    status_label.config(text=status)

# GUI 생성
app = tk.Tk()
app.title('YouTube Downloader')

# 레이블과 엔트리 위젯 추가
url_label = tk.Label(app, text='Enter YouTube Video URL:')
url_label.grid(row=0, column=0, pady=10, padx=10)  # padx 옵션 추가

url_entry = tk.Entry(app, width=40)
url_entry.grid(row=0, column=1, pady=10)

# Download 버튼을 URL 입력 창 바로 오른쪽에 위치
download_button = tk.Button(app, text='Download', command=download_youtube_video)
download_button.grid(row=0, column=2, padx=20, pady=20)  # padx 옵션 추가

# 상태 표시 레이블 추가
status_label = tk.Label(app, text='')
status_label.grid(row=1, column=0, columnspan=3)

# GUI 실행
app.mainloop()
