import yt_dlp
import os

def download_youtube_video_as_mp3(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'ffmpeg_location': 'C:/Users/User/AppData/Local/Programs/Python/bin',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }],
        'postprocessor_args': [
            '-ar', '44100'
        ],
        'keepvideo': False,  
        'outtmpl': '%(title)s.%(ext)s', 
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info_dict)
    
    # Dosya adını yazdırın
    print(f"Dosya '{filename}' olarak kaydedildi.")

youtube_url = input("Lütfen İndirmek İstediğiniz MP3 Dosyasınızın Linkini Buraya Yapıştırınız: ")
download_youtube_video_as_mp3(youtube_url)