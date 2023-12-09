# gui.py

import tkinter as tk
from tkinter import filedialog
import threading
import os
from downloader import download_video

# 전역 변수로 이전 다운로드 경로를 저장할 변수 추가
previous_download_path = None

def download_youtube_video():
    def download():
        # 전역 변수를 사용하여 이전 다운로드 경로 저장
        global previous_download_path

        # 유튜브 영상 URL을 입력 받음
        youtube_url = url_entry.get()

        # 다운로드 위치 선택
        download_path = filedialog.askdirectory()

        # 전역 변수에 이전 다운로드 경로 저장
        previous_download_path = download_path

        # 다운로드 함수 호출
        download_video(youtube_url, download_path, update_status_label)

        # 다운로드 완료 후 폴더 열기 버튼 활성화
        open_folder_button.config(state=tk.NORMAL)

    # 쓰레드 생성 및 시작
    download_thread = threading.Thread(target=download)
    download_thread.start()

def update_status_label(status):
    status_label.config(text=status)

def open_download_folder():
    # 전역 변수로부터 이전 다운로드 경로 가져오기
    global previous_download_path

    # 이전 다운로드 경로가 있을 경우 폴더 열기
    if previous_download_path:
        os.system(f'explorer {os.path.realpath(previous_download_path)}')
    else:
        update_status_label("이전 다운로드 폴더가 없습니다.")

# GUI 생성
app = tk.Tk()
app.title('YouTube Downloader')

# 레이블과 엔트리 위젯 추가
url_label = tk.Label(app, text='유튜브 동영상 URL 입력:')
url_label.grid(row=0, column=0, pady=10, padx=10)  # padx 옵션 추가

url_entry = tk.Entry(app, width=40)
url_entry.grid(row=0, column=1, pady=10)

# Download 버튼을 URL 입력 창 바로 오른쪽에 위치
download_button = tk.Button(app, text='다운로드', command=download_youtube_video)
download_button.grid(row=0, column=2, padx=20, pady=20)  # padx 옵션 추가

# 다운로드 완료 후 폴더 열기 버튼
open_folder_button = tk.Button(app, text='폴더 열기', command=open_download_folder, state=tk.DISABLED)
open_folder_button.grid(row=1, column=2, padx=20, pady=20)  # padx 옵션 추가

# 상태 표시 레이블 추가
status_label = tk.Label(app, text='')
status_label.grid(row=2, column=0, columnspan=3)

# GUI 실행
app.mainloop()
