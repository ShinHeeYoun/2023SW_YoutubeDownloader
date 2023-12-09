# view.py

import tkinter as tk
from tkinter import filedialog
import threading

def create_gui(download_callback):
    app = tk.Tk()
    app.title('YouTube Downloader')

    url_label = tk.Label(app, text='Enter YouTube Video URL:')
    url_label.grid(row=0, column=0, pady=10, padx=10)

    url_entry = tk.Entry(app, width=40)
    url_entry.grid(row=0, column=1, pady=10)

    def download_button_clicked():
        # 다운로드 버튼 클릭 시 다운로더 모듈 호출
        download_thread = threading.Thread(
            target=download_callback,
            args=(url_entry.get(), filedialog.askdirectory(), status_label.config)
        )
        download_thread.start()

    download_button = tk.Button(app, text='Download', command=download_button_clicked)
    download_button.grid(row=0, column=2, padx=20, pady=20)

    status_label = tk.Label(app, text='')
    status_label.grid(row=1, column=0, columnspan=3)

    app.mainloop()
