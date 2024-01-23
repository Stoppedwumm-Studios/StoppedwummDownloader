import tkinter as tk
from tkinter import filedialog
import threading
from yt_dlp import YoutubeDL
from PIL import ImageTk, Image
import os
import urllib.parse

def download_thumbnail(video_url, output_path='thumbnail.jpg'):
    # Create a yt-dlp instance
    ytdl = YoutubeDL()

    # Get video info
    info_dict = ytdl.extract_info(video_url, download=False)

    # Get the URL of the thumbnail
    thumbnail_url = info_dict.get('thumbnails')[-1]['url']

    # Download the thumbnail
    ytdl.download([thumbnail_url])

    # Get the filename from the URL and sanitize it
    thumbnail_filename = urllib.parse.unquote(thumbnail_url.split('/')[-1])
    thumbnail_filename = ''.join(c for c in thumbnail_filename if c.isalnum() or c in ['.', '_'])

    # Remove file extension '.webp' from thumbnail_filename
    thumbnail_filename = os.path.splitext(thumbnail_filename)[0]
    
    return thumbnail_filename + " [" + thumbnail_filename + "].webp"

def download_video(video_url, save_path):
    # Ensure the directory exists
    os.makedirs(save_path, exist_ok=True)

    # Create a yt-dlp instance
    ytdl = YoutubeDL()
    
    info_dict = ytdl.extract_info(video_url, download=True)
    
    # Get the filename from the URL and sanitize it
    video_filename = info_dict['title'] + ' [' + info_dict['id'] + '].webm'

    # Construct the original downloaded video path
    original_video_path = os.path.join(os.getcwd(), video_filename)

    # Rename the downloaded video to the desired output path
    video_path = os.path.join(save_path, video_filename)
    os.rename(original_video_path, video_path)

    print(f'Video downloaded and saved as: {video_path}')
    return video_path

def download_button_click():
    file_path = filedialog.asksaveasfilename(defaultextension=".webm", filetypes=[("webm files", "*.webm"), ("All files", "*.*")])
    
    if file_path:
        URL = text.get()
        thumbnail_path = download_thumbnail(URL)
        video_path = download_video(URL, os.path.dirname(file_path))
        
        # Delete the thumbnail file
        os.remove(thumbnail_path)

        print(f'Thumbnail downloaded and saved as: {thumbnail_path}')
        print(f'Video downloaded and saved as: {video_path}')

        # Hide the infoFrame
        infoFrame.pack_forget()

def on_closing():
    # Check for a thumbnail and delete it before closing
    thumbnail_path = "maxresdefault [maxresdefault].webp"

    if os.path.exists(thumbnail_path):
        os.remove(thumbnail_path)

on_closing()
mainscreen = tk.Tk("StoppedwummDownloader")
mainscreen.title("StoppedwummDownloader")

infoFrame = tk.Frame(mainscreen)
downloadFrame = tk.Frame(mainscreen)
URLlabel = tk.Label(downloadFrame, text="URL:")
text = tk.Entry(downloadFrame)
infoLabel = tk.Label(downloadFrame, text="Downloading...")
videoTitle = tk.Label(infoFrame, text="Video Title")
videoTitle.pack()

# Added label to show the thumbnail
thumbnail_label = tk.Label(infoFrame)
thumbnail_label.pack()

# Download button


VideoInfo={}

def ClickButton():
    infoLabel.pack()
    URL = text.get()
    ytdl = YoutubeDL()
    info = ytdl.extract_info(URL, download=False)
    thumbnail_path = download_thumbnail(URL)
    infoLabel.pack_forget()
    videoTitle.config(text="Title: " + str(info["title"]))
    
    # Open and display the thumbnail image using PIL
    thumbnail_image = Image.open(thumbnail_path)
    thumbnail_image = thumbnail_image.resize((720, 450), Image.ANTIALIAS)
    thumbnail_tk = ImageTk.PhotoImage(thumbnail_image)
    thumbnail_label.config(image=thumbnail_tk)
    thumbnail_label.image = thumbnail_tk
    
    infoFrame.pack()
    print(info)
    formats = info["formats"]

def ClickButton2():
    ButtonClickThread = threading.Thread(target=ClickButton, daemon=True)
    ButtonClickThread.start()

def Download():
    Thread = threading.Thread(target=download_button_click, daemon=True)
    Thread.run()
    
button = tk.Button(mainscreen, text="Click me", command=ClickButton2)
URLlabel.pack()
text.pack()
button.pack()
downloadFrame.pack()
download_button = tk.Button(infoFrame, text="Download", command=Download)
download_button.pack()

mainscreen.mainloop()
on_closing()
print("Deleted Thumbnail and temporary data, goodbye")
