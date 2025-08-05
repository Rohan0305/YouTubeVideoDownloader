import yt_dlp
import os

def download_video(url, save_path):
    try:
        ydl_opts = {
            'outtmpl': os.path.join(save_path, '%(title)s.%(ext)s'),
            'format': 'best[ext=mp4]/best',
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            title = info.get('title', 'Unknown title')
            duration = info.get('duration', 0)
            
            ydl.download([url])
            
        return True, title, duration
    except Exception as e:
        return False, str(e), 0

def get_downloads_path():
    return os.path.expanduser("~/Downloads")

def validate_url(url):
    if not url:
        return False, "URL is empty"
    
    if not url.startswith(('http://', 'https://')):
        return False, "URL must start with http:// or https://"
    
    if 'youtube.com' not in url and 'youtu.be' not in url:
        return False, "URL must be from YouTube"
    
    return True, "Valid URL" 