# gui.py

import tkinter as tk
from tkinter import filedialog
import threading
import os
from pytube import YouTube
from pytube.exceptions import PytubeError

# 전역 변수로 이전 다운로드 경로를 저장할 변수 추가, 디폴트는 실행기 위치치
previous_download_path = None

def update_progress_label(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage = (bytes_downloaded / total_size) * 100
    progress_label.config(text=f'진행도: {percentage:.2f}%')
    app.event_generate("<<UpdateStatus>>", when="tail", data=f'다운로드 중... {percentage:.2f}% 완료')
    app.update()  # Tkinter 업데이트 처리

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage = (bytes_downloaded / total_size) * 100
    print(f"다운로드 중... {percentage:.2f}% 완료", end='\r', flush=True)

def download_video(youtube_url, download_path, status_callback, progress_callback, download_format):
    try:
        yt = YouTube(youtube_url, on_progress_callback=progress_callback)
        status_callback(f'찾는 중: {yt.title}')

        filename = None

        if download_format == "mp4":
            selected_stream = yt.streams.get_highest_resolution()
            filename = f"{yt.title}.mp4"
        elif download_format == "mp3":
            selected_stream = yt.streams.filter(only_audio=True).first()
            filename = f"{yt.title}.mp3"
        else:
            status_callback("에러: 지원하지 않는 다운로드 형식입니다.")
            return

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

def download_youtube_video():
    def download():
        global previous_download_path

        youtube_url = url_entry.get()
        download_path = filedialog.askdirectory()
        previous_download_path = download_path
        chosen_format = download_format.get()

        download_video(youtube_url, download_path, update_status_label, update_progress_label, chosen_format)

        open_folder_button.config(state=tk.NORMAL)

    download_thread = threading.Thread(target=download)
    download_thread.start()

def update_download_format():
    global download_format

    chosen_format = download_format

def update_status_label(status):
    status_label.config(text=status)

def open_download_folder():
    global previous_download_path

    if previous_download_path:
        os.system(f'explorer {os.path.realpath(previous_download_path)}')
    else:
        update_status_label("이전 다운로드 폴더가 없습니다.")

app = tk.Tk()
app.title('YouTube Downloader')

download_format = tk.StringVar()
download_format.set("mp4")

mp4_radio = tk.Radiobutton(app, text="MP4", variable=download_format, value="mp4", command=update_download_format)
mp4_radio.grid(row=1, column=0, padx=10)

mp3_radio = tk.Radiobutton(app, text="MP3", variable=download_format, value="mp3", command=update_download_format)
mp3_radio.grid(row=1, column=1, padx=10)

url_label = tk.Label(app, text='유튜브 동영상 URL 입력:')
url_label.grid(row=0, column=0, pady=10, padx=10)

url_entry = tk.Entry(app, width=40)
url_entry.grid(row=0, column=1, pady=10)

download_button = tk.Button(app, text='다운로드', command=download_youtube_video)
download_button.grid(row=0, column=2, padx=20, pady=20)

open_folder_button = tk.Button(app, text='폴더 열기', command=open_download_folder, state=tk.DISABLED)
open_folder_button.grid(row=1, column=2, padx=20, pady=20)

status_label = tk.Label(app, text='')
status_label.grid(row=2, column=0, columnspan=3)

progress_label = tk.Label(app, text='진행도: 0%', pady=10)
progress_label.grid(row=3, column=0, columnspan=3)

app.mainloop()
