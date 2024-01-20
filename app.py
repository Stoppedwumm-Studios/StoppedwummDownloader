import tkinter as tk
import threading
import json
import yt_dlp

mainscreen = tk.Tk("DreckPort-Downloader")
downloadFrame = tk.Frame(mainscreen)
label = tk.Label(downloadFrame, text="URL")
text = tk.Entry(downloadFrame)
infoLabel = tk.Label(downloadFrame, text="Downloading...")


def ClickButton():
    infoLabel.pack
    URL = text.get()
    ydl_opts = {}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(URL, download=False)

        # ℹ️ ydl.sanitize_info makes the info json-serializable
        print(json.dumps(ydl.sanitize_info(info)))
    infoLabel.pack_forget()

def ClickButton2():
    ButtonClickThread = threading.Thread(target=ClickButton, daemon=True)
    ButtonClickThread.start()


button = tk.Button(mainscreen, text="Click me", command=ClickButton2)
text.pack()
button.pack()
downloadFrame.pack()

mainscreen.mainloop()