# import youtube from pytube
import yt_dlp
from pathlib import Path

# set download directory
# this uses Path.home() to find your user folder automatically 
download_folder = Path.home() / "Downloads" / "YT_DWNLDS"
download_folder.mkdir(parents=True, exist_ok=True)

# configure downloader options
ydl_opts = {
    # 'bestvideo+bestaudio' ensures you get 1080p or higher
    'format': 'best',
    # where to save and what to name it 
    'outtmpl': f'{download_folder}/%(title)s.%(ext)s',
    # merge video and audio into an mp4 file
    'merge_output_format': 'mp4',
    'noplaylist': True,
}

try:
    # Ask user to input youtube url
    url = input("Enter YouTube URL: ")
   
    print(f"Checking folder: {download_folder.absolute()}")

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    
    print("\nProcess finished. Check the folder above!")
    # with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    #     print(f"Starting download to: {download_folder}")
    # print("\nDownload Complete!")
except Exception as e:
    print(f"An error occurred:{e}")
    