import sys
from yt_dlp import YoutubeDL

def download_playlist(url):
    ydl_opts = {
        "outtmpl": "downloads/%(playlist_index)s - %(title)s.%(ext)s",
        "ignoreerrors": True,
        "format": "best",
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    playlist_url = sys.argv[1]
    download_playlist(playlist_url)
