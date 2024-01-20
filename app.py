import tkinter as tk
import threading

mainscreen = tk.Tk("DreckPort-Downloader")
label = tk.Label(mainscreen, text="URL")
text = tk.Entry(mainscreen)


def ClickButton():
    print("Button clicked")

button = tk.Button(mainscreen, text="Click me", command=ClickButton)
text.pack()
button.pack()

mainscreen.mainloop()

import json
import yt_dlp

URL = 'https://www.youtube.com/watch?v=BaW_jenozKc'


ydl_opts = {}
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(URL, download=False)

    # ℹ️ ydl.sanitize_info makes the info json-serializable
    print(json.dumps(ydl.sanitize_info(info)))