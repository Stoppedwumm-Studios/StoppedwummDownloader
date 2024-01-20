import tkinter as tk
from yt_dlp import YoutubeDL

def ClickButton():
    print("Button clicked")

mainscreen = tk.Tk("DreckPort-Downloader")

text = tk.Label(mainscreen, text="Test")
button = tk.Button(mainscreen, text="Click me", command=ClickButton)
text.pack()
button.pack()
mainscreen.mainloop()