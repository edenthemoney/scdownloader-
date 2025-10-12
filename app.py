from flask import Flask, render_template, request, jsonify, send_file
import yt_dlp
import os
import uuid
from pathlib import Path
import threading
import time
import zipfile
import shutil

app = Flask(__name__)

# Create downloads directory
DOWNLOAD_DIR = Path('downloads')
DOWNLOAD_DIR.mkdir(exist_ok=True)

# Store download status
download_status = {}

def download_audio(url, download_id):
    """Download audio from SoundCloud URL"""
    try:
        download_status[download_id] = {
            'status': 'downloading',
            'progress': 0,
            'message': 'Starting download...',
            'files': []
        }
        
        output_path = DOWNLOAD_DIR / download_id
        output_path.mkdir(exist_ok=True)
        
        def progress_hook(d):
            if d['status'] == 'downloading':
                try:
                    percent = d.get('_percent_str', '0%').strip()
                    download_status[download_id]['progress'] = percent
                    download_status[download_id]['message'] = f'Downloading: {percent}'
                except:
                    pass
            elif d['status'] == 'finished':
                download_status[download_id]['message'] = 'Processing...'
        
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320',
            }],
            'outtmpl': str(output_path / '%(playlist_index)s - %(title)s.%(ext)s'),
            'progress_hooks': [progress_hook],
            'quiet': False,
            'no_warnings': False,
            'extract_flat': False,  # Must be False to download all playlist items
            'ignoreerrors': True,  # Continue on individual track errors in playlists
            'noplaylist': False,  # Ensure playlists are processed
            'yes_playlist': True,  # Force playlist download
            'playlistend': None,  # Download all items, no limit
            'concurrent_fragment_downloads': 4,  # Reduced to avoid overwhelming FFmpeg
            'http_chunk_size': 10485760,  # 10MB chunks for faster downloads
            'retries': 10,  # Retry failed downloads
            'fragment_retries': 10,  # Retry failed fragments
            'skip_unavailable_fragments': False,  # Ensure complete tracks
            'keepvideo': False,  # Remove temp files to save space
            'writethumbnail': False,  # Skip thumbnails for speed
            'writesubtitles': False,  # Skip subtitles for speed
            'postprocessor_args': [
                '-threads', '4',  # Limit threads to avoid FFmpeg crashes
                '-loglevel', 'error',  # Reduce FFmpeg verbosity
            ],
            'prefer_ffmpeg': True,  # Explicitly prefer FFmpeg
            'fixup': 'detect_or_warn',  # Auto-fix file issues
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # First, extract info to check what we're dealing with
            info = ydl.extract_info(url, download=False)
            
            # Log what we detected
            if info:
                if 'entries' in info:
                    entry_count = len([e for e in info['entries'] if e is not None])
                    print(f"Playlist detected: {info.get('title', 'Unknown')} with {entry_count} entries")
                    download_status[download_id]['message'] = f'Found {entry_count} tracks in playlist...'
                else:
                    print(f"Single track detected: {info.get('title', 'Unknown')}")
                    print(f"Duration: {info.get('duration', 'Unknown')} seconds")
            
            # Now download
            info = ydl.extract_info(url, download=True)
            
            # Get list of downloaded files
            files = []
            for file in output_path.glob('*.mp3'):
                files.append({
                    'name': file.name,
                    'size': f"{file.stat().st_size / (1024*1024):.2f} MB"
                })
            
            print(f"Total MP3 files found: {len(files)}")
            
            if len(files) == 0:
                raise Exception("No tracks were successfully downloaded. Check if the URL is valid or tracks are available.")
            
            # Create ZIP file with all tracks (use STORED for speed since MP3s are already compressed)
            download_status[download_id]['message'] = 'Creating ZIP file...'
            zip_path = output_path / 'soundcloud_download.zip'
            
            with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_STORED) as zipf:
                for file in output_path.glob('*.mp3'):
                    zipf.write(file, file.name)
            
            zip_size = f"{zip_path.stat().st_size / (1024*1024):.2f} MB"
            
            # Check if playlist had errors
            success_msg = f'Successfully downloaded {len(files)} track(s)!'
            if info and 'entries' in info:
                expected = len([e for e in info['entries'] if e is not None])
                if len(files) < expected:
                    success_msg += f' (Some tracks may have failed - check if they are private or restricted)'
            
            download_status[download_id] = {
                'status': 'completed',
                'progress': 100,
                'message': success_msg,
                'files': files,
                'download_id': download_id,
                'zip_ready': True,
                'zip_size': zip_size
            }
            
    except Exception as e:
        download_status[download_id] = {
            'status': 'error',
            'progress': 0,
            'message': f'Error: {str(e)}',
            'files': []
        }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/download', methods=['POST'])
def start_download():
    data = request.json
    url = data.get('url', '').strip()
    
    if not url:
        return jsonify({'error': 'No URL provided'}), 400
    
    if 'soundcloud.com' not in url:
        return jsonify({'error': 'Please provide a valid SoundCloud URL'}), 400
    
    # Generate unique download ID
    download_id = str(uuid.uuid4())
    
    # Start download in background thread
    thread = threading.Thread(target=download_audio, args=(url, download_id))
    thread.daemon = True
    thread.start()
    
    return jsonify({'download_id': download_id})

@app.route('/status/<download_id>')
def get_status(download_id):
    status = download_status.get(download_id, {
        'status': 'not_found',
        'message': 'Download not found'
    })
    return jsonify(status)

@app.route('/download-zip/<download_id>')
def download_zip(download_id):
    zip_path = DOWNLOAD_DIR / download_id / 'soundcloud_download.zip'
    if zip_path.exists():
        return send_file(zip_path, as_attachment=True, download_name='soundcloud_tracks.zip')
    return jsonify({'error': 'ZIP file not found'}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5001, threaded=True)
