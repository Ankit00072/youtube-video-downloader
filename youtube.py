import tkinter as tk
from tkinter import messagebox
from pytube import YouTube

def download_video():
    
    url = url_entry.get()
    audio_quality = audio_quality_var.get()
    video_quality = video_quality_var.get()

    try:
        yt = YouTube(url)
        if audio_quality:
            audio_stream = yt.streams.filter(only_audio=True).first()
            audio_stream.download(output_path='Downloads', filename_prefix='audio_')
        if video_quality:
            video_stream = yt.streams.filter(progressive=True, file_extension='mp4', resolution=video_quality).first()
            video_stream.download(output_path='downloads/')
        messagebox.showinfo("Success", "Video downloaded successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

root = tk.Tk()
root.title("YouTube Video Downloader")

# Creativity: Adding a welcome message
welcome_label = tk.Label(root, text="Welcome to YouTube Video Downloader!", font=("Arial", 14, "bold"), fg="blue")
welcome_label.pack(pady=10)

# Entry for YouTube video URL
url_label = tk.Label(root, text="Enter YouTube Video URL:")
url_label.pack(pady=5)

url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

# Creativity: Adding a label for audio quality
audio_quality_label = tk.Label(root, text="Select Audio Quality:")
audio_quality_label.pack(pady=5)

# Dropdown for audio quality options
audio_quality_var = tk.StringVar()
audio_quality_options = ["Best", "Low", "Medium"]
audio_quality_var.set("Best")

audio_quality_menu = tk.OptionMenu(root, audio_quality_var, *audio_quality_options)
audio_quality_menu.pack(pady=5)

# Creativity: Adding a label for video quality
video_quality_label = tk.Label(root, text="Select Video Quality:")
video_quality_label.pack(pady=5)

# Dropdown for video quality options
video_quality_var = tk.StringVar()
video_quality_options = ["720p", "480p", "360p", "240p"]
video_quality_var.set("720p")

video_quality_menu = tk.OptionMenu(root, video_quality_var, *video_quality_options)
video_quality_menu.pack(pady=5)

# Download button
download_button = tk.Button(root, text="Download Video", command=download_video, )
download_button.pack(pady=10)

# Creativity: Adding credits
credits_label = tk.Label(root, text="Developed by ERACODING", font=("Arial", 10), fg="red", )
credits_label.pack(pady=5)

root.mainloop()
