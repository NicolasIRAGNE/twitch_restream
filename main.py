'''
File: main.py
Created Date: 16/11/2024
Author: Nicolas Iragne (nicoragne@hotmail.fr)
-----
This script aims to broadcast a playlist of videos to a rtsp server (usually
Twitch).
-----
'''

import yt_dlp
import os
import dotenv

if __name__ == "__main__":
    dotenv.load_dotenv()
    PLAYLIST_URL = os.getenv("PLAYLIST_URL")
    OUTPUT_URL = os.getenv("OUTPUT_URL")
    ydl_opts = {
        'format': 'best',
        'outtmpl': 'videos/%(id)s.%(ext)s',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        playlist = ydl.extract_info(PLAYLIST_URL, download=True)
        for video in playlist['entries']:
            print(f"Now broadcasting {video['id']} - {video['title']}")
            os.system(f"ffmpeg -re -i \"videos/{video['id']}.mp4\" -c copy -f flv {OUTPUT_URL}")
