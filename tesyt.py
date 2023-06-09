# import urllib.parse
# import urllib.request
# from googleapiclient.discovery import build
# from googleapiclient.errors import HttpError

# # Masukkan API key yang sudah didapatkan
# API_KEY = "AIzaSyCo1xZ7bw0IHDErAoOBuqC-fWraUu0esPo"

# # Masukkan id video yang ingin ditampilkan informasinya dan didownload
# VIDEO_ID = "NTyqTObrCDY"

# # Buat objek youtube dengan menggunakan API key
# youtube = build('youtube', 'v3', developerKey=API_KEY)

# try:
#     # Ambil informasi video
#     video_response = youtube.videos().list(
#         part='snippet, contentDetails, statistics',
#         id=VIDEO_ID
#     ).execute()

#     if not video_response['items']:
#         print("Video tidak ditemukan")
#     else:
#         # Tampilkan informasi video
#         # title = video_response['items'][0]['snippet']['title']
#         # duration = video_response['items'][0]['contentDetails']['duration']
#         # likes = video_response['items'][0]['statistics'].get('likeCount', 'N/A')
#         # dislikes = video_response['items'][0]['statistics'].get('dislikeCount', 'N/A')
#         # views = video_response['items'][0]['statistics'].get('viewCount', 'N/A')
#         # print("Judul: ", title)
#         # print("Durasi: ", duration)
#         # print("Likes: ", likes)
#         # print("Dislikes: ", dislikes)
#         # print("Views: ", views)

#         # Download video
#         video_url = "https://www.youtube.com/watch?v=" + VIDEO_ID
#         video_info_url = "https://www.youtube.com/get_video_info?video_id=" + VIDEO_ID
#         video_info_response = urllib.request.urlopen(video_info_url).read().decode()
#         video_info = urllib.parse.parse_qs(video_info_response)
#         video_formats = video_info['adaptive_fmts'][0].split(',')
#         video_formats.extend(video_info['url_encoded_fmt_stream_map'][0].split(','))
#         for video_format in video_formats:
#             video_format = urllib.parse.parse_qs(video_format)
#             itag = video_format['itag'][0]
#             mime_type = video_format['type'][0].split(';')[0]
#             if 'video/mp4' in mime_type or 'audio/mpeg' in mime_type or 'audio/mp4' in mime_type:
#                 url = video_format['url'][0]
#                 quality = video_format.get('quality_label', [''])[0]
#                 res = video_format.get('resolution', [''])[0]
#                 fps = video_format.get('fps', [''])[0]
#                 if 'video' in mime_type:
#                     print("Video - Format: ", mime_type, ", Resolusi: ", res, ", FPS: ", fps, ", Kualitas: ", quality, ", URL: ", url)
#                 elif 'audio' in mime_type:
#                     print("Audio - Format: ", mime_type, ", Kualitas: ", quality, ", URL: ", url)
#                 else:
#                     print("Format tidak dikenali")
#                     print("Format: ", mime_type, ", URL: ", url)
# except HttpError as error:
#     print("Terjadi kesalahan: ", error)

# Video ID
# from pytube import YouTube

# masukkan URL video yang ingin Anda lihat resolusinya
# url = "https://www.youtube.com/watch?v=TUPNWkDfZp8"

# buat objek YouTube dengan URL video
# yt = YouTube(url)

# dapatkan daftar stream video yang tersedia
# video_streams = yt.streams.first()

# loop melalui daftar stream video dan tampilkan resolusi setiap stream
# for stream in video_streams:
#     print(stream.resolution)


# try:
#     video_response = youtube.videos().list(
#         part='id,snippet,contentDetails, fileDetails',
#         id=video_id
#     ).execute()

#     if len(video_response['items']) == 0:
#         print("Video not found.")
        # return
    # else:
        # Extract the list of download links for the video in various resolutions
        # download_links = video_response['items'][0]['contentDetails']['videoQuality']
        # qua = video_response['items'][0]['fileDetails']['fileSize']
        # print(qua)
        # Print the available video resolutions
        # print("Available resolutions:")
        # for lin in qua:
        #     print(lin)
        # for link in download_links:
        #     print(link['qualityLabel'])

# except HttpError as e:
#     print("An HTTP error %d occurred:/n%s" % (e.resp.status, e.content))

# except Exception as e:
#     print("An error occurred:/n%s" % (str(e)))

# try:
#     # Get video information
#     video_response = youtube.videos().list(
#         part='snippet',
#         id=video_id
#     ).execute()

#     # Get video title
#     video_title = video_response['items'][0]['snippet']['title']

#     # Get video stream URL
#     video_stream_url = "https://www.youtube.com/watch?v=" + video_id
#     video_stream_url += "&pbj=1"
#     request = urllib.request.urlopen(video_stream_url)
#     data = request.read().decode('utf-8')
#     request.close()
#     stream_url = "https://www.youtube.com" + /
#         data.split('"url":"')[1].split('","')[0]

#     # Download video
#     urllib.request.urlretrieve(stream_url, video_title + ".mp4")
#     print("Video downloaded successfully!")

# except HttpError as e:
#     print("An HTTP error %d occurred:/n%s" % (e.resp.status, e.content))

# except Exception as e:
#     print("An error occurred:/n%s" % (str(e)))


# Tautan video YouTube



# Retrieve video URL
# video_url = f'https://www.youtube.com/watch?v={video_id}'

# # Retrieve video download URLs for different resolutions
# video_info_url = f'https://www.youtube.com/get_video_info?video_id={video_id}&el=embedded&ps=default&eurl=&gl=US&hl=en'
# video_info_response = urllib.request.urlopen(video_info_url).read().decode('utf-8')
# video_info = urllib.parse.parse_qs(video_info_response)

# video_formats = video_info['url_encoded_fmt_stream_map'][0].split(',')
# video_urls = {}
# for fmt in video_formats:
#     video_data = urllib.parse.parse_qs(fmt)
#     video_resolution = video_data['quality_label'][0]
#     video_url = video_data['url'][0]
#     video_urls[video_resolution] = video_url

# # Display available video resolutions
# print('Available Resolutions:')
# for resolution in video_urls.keys():
#     print(f'- {resolution}')

# Ask user to choose a resolution
# chosen_resolution = input('Choose a resolution: ')

# # Download video with chosen resolution
# if chosen_resolution in video_urls:
#     video_url = video_urls[chosen_resolution]
#     urllib.request.urlretrieve(video_url, f'{video_title}-{chosen_resolution}.mp4')
#     print(f'{video_title} ({chosen_resolution}) has been downloaded.')
# else:
#     print('Invalid resolution chosen.')

# importing the module
# from pytube import YouTube

# SAVE_PATH = "E:/Kuliah Amikom/Projek Pribadi/Website/Youtube Downloader"


# def get_resolutions(VIDEO_ID, type='video'):
#     url = f'https://www.youtube.com/watch?v={VIDEO_ID}'

#     if type == 'video':
#         Files = YouTube(url).streams.filter(type='video', file_extension='mp4')
#         resolution_attr = 'resolution'
#         str_for_replace = 'p'
#     elif type == 'audio':
#         Files = YouTube(url).streams.filter(type='audio')
#         resolution_attr = 'abr'
#         str_for_replace = 'kbps'
#     else:
#         return {}

#     resolutions = {}

#     for stream in Files:
#         resolution = getattr(stream, resolution_attr).replace(str_for_replace, '')
#         filesize = stream.filesize
#         resolutions[resolution] = filesize
    
#     sorted_resolutions = dict(sorted(resolutions.items(), key=lambda x: int(x[0]), reverse=True))
#     return sorted_resolutions

# res = get_resolutions('dCNTQmbqFSs', type='audio')

# for reso, filesize in res.items():
#     print(f'{reso} - {filesize}')
# def format_file_size(file_size):
#     if file_size < 1024:
#         return str(file_size) + ' B'
#     elif file_size < 1024 * 1024:
#         return '{:.1f} KB'.format(file_size / 1024)
#     elif file_size < 1024 * 1024 * 1024:
#         return '{:.1f} MB'.format(file_size / (1024 * 1024))
#     else:
#         return '{:.1f} GB'.format(file_size / (1024 * 1024 * 1024))

# def format_file_size(file_size):
#     if file_size < 1000:
#         return f"{file_size} B"
#     elif file_size < 1000000:
#         return f"{file_size / 1000:.1f} KB"
#     elif file_size < 1000000000:
#         return f"{file_size / 1000000:.1f} MB"
#     else:
#         return f"{file_size / 1000000000:.1f} GB"


# def download_files(VIDEO_ID, resolution, type='video', title=None):
#     url = f'https://www.youtube.com/watch?v={VIDEO_ID}'

#     if type == 'video':
#         Files = YouTube(url).streams.filter(type='video', file_extension='mp4', progressive=False, resolution=f'{resolution}p').desc().first().download()
#         return send_file(Files, as_attachment=True, download_files=f'{title} - {resolution}p.mp4')
    
#     elif type == 'audio':
#         Files = YouTube(url).streams.filter(type='audio', abr=f'{resolution}kbps').first()
#         return send_file(Files, as_attachment=True, download_files=f'{title} - {resolution}kbps.mp3')        

# download_files('dCNTQmbqFSs', resolution='48', type='audio', title='hghg')
# download_files('dCNTQmbqFSs', resolution='1080', title='hghg')
# from pytube import YouTube

# def download_files(VIDEO_ID, resolution, title, type):
#     url = f'https://www.youtube.com/watch?v={VIDEO_ID}'

#     if type == 'video':
#         Files = YouTube(url).streams.filter(type='video', file_extension='mp4')
#         for i in Files:
#             print(i)
#         # return send_file(Files, as_attachment=True, download_name=f'{title} - {resolution}p.mp4')
    
#     elif type == 'audio':
#         Files = YouTube(url).streams.filter(type='audio', abr=f'{resolution}kbps').first().download()
#         # return send_file(Files, as_attachment=True, download_name=f'{title} - {resolution}kbps.mp3')  

# download_files('dQw4w9WgXcQ', '1080', 'adad', 'video')

# from pytube import YouTube
# from moviepy.editor import VideoFileClip, AudioFileClip

# def download_and_merge_audio_video(url, output_path):
#     try:
#         yt = YouTube(url)

#         # Filter stream dengan format video dan audio
#         streams = yt.streams.filter(res='1080p', progressive=False, file_extension='mp4')

#         # Pilih stream dengan resolusi 1080p yang memiliki audio
#         stream = streams.first()

#         # Download video dengan audio
#         video_filename = stream.download(output_path=output_path)

#         # Ambil path file audio
#         audio_filename = video_filename.replace('.mp4', '.mp3')

#         # Download audio saja
#         audio = yt.streams.get_audio_only()
#         audio.download(output_path=output_path, filename=audio_filename)

#         # Menggabungkan audio dan video
#         video = VideoFileClip(video_filename)
#         audio = AudioFileClip(audio_filename)
#         final_video = video.set_audio(audio)

#         # Simpan video hasil gabungan
        
#         final_video.write_videofile(output_path + '/merged_video.mp4')

#         print("Download dan penggabungan selesai.")

#     except Exception as e:
#         print("Terjadi kesalahan:", str(e))

# # Contoh penggunaan
# url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
# output_path = "E:/Kuliah Amikom/Projek Pribadi/Website/Youtube Downloader"

# download_and_merge_audio_video(url, output_path)


# pasti
# from flask import Flask, render_template, request, send_file
# from pytube import YouTube
# import io

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('tesindex.html')

# @app.route('/download', methods=['POST'])
# def download():
#     url = request.form['url']
#     try:
#         yt = YouTube(url)

#         video_content = io.BytesIO()
#         Files = yt.streams.filter(type='video', file_extension='mp4', progressive=False, resolution=f'{720}p').desc().first().stream_to_buffer(video_content)

#         t = yt.title
        
#         video_content.seek(0)  # Mengatur posisi awal objek BytesIO

#         return send_file(video_content, as_attachment=True, download_name='.mp4')
#     except Exception as e:
#         return str(e)

# if __name__ == '__main__':
#     app.run(debug=True)

# from flask import Flask, render_template, request
# from pytube import YouTube
# from threading import Thread
# from flask_socketio import SocketIO

# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'secret_key'
# socketio = SocketIO(app)

# @app.route('/', methods=['GET', 'POST'])
# def home():
#     if request.method == 'POST':
#         video_url = request.form['url']
#         thread = Thread(target=download_video, args=(video_url,))
#         thread.start()

#     return render_template('index.html')

# def download_video(url):
#     youtube = YouTube(url, on_progress_callback=on_progress)
#     video = youtube.streams.first()
#     video.download()

# @socketio.on('progress')
# def on_progress(stream, chunk, bytes_remaining):
#     total_bytes = stream.filesize
#     bytes_downloaded = total_bytes - bytes_remaining
#     progress = (bytes_downloaded / total_bytes) * 100
#     socketio.emit('progress', {'progress': progress})

# @socketio.on('connect')
# def test_connect():
#     print('Client connected')

# @socketio.on('disconnect')
# def test_disconnect():
#     print('Client disconnected')

# if __name__ == '__main__':
#     socketio.run(app, debug=True)




# from pytube import YouTube

# url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

# yt = YouTube(url).streams.filter(type='video', file_extension='mp4', progressive=True, resolution='720p').desc().first()

# print(yt.url)
import requests

def download_file(url, save_path):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print("File berhasil diunduh ke:", save_path)
    else:
        print("Gagal mengunduh file.")

url = "https://rr4---sn-2uuxa3vh-wvbz.googlevideo.com/videoplayback?expire=1683771141&ei=pfpbZI_rDsy99QOq2LrYAw&ip=2001%3A448a%3A4040%3A1173%3Abddf%3Abf8a%3A9f6c%3Ab9c3&id=o-ACVjdTLucOspRBHtArVTIt7wo5a4sl8sRgQ_nlGLRE8P&itag=22&source=youtube&requiressl=yes&mh=7c&mm=31%2C29&mn=sn-2uuxa3vh-wvbz%2Csn-npoe7nsl&ms=au%2Crdu&mv=m&mvi=4&pl=52&initcwndbps=667500&vprv=1&mime=video%2Fmp4&cnr=14&ratebypass=yes&dur=212.091&lmt=1674233742818000&mt=1683749118&fvip=2&fexp=24007246&c=ANDROID_MUSIC&txp=4532434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Ccnr%2Cratebypass%2Cdur%2Clmt&sig=AOq0QJ8wRQIgMmws2GFVuHskzeaFVHSONVE8rsqv6ieQtHwXKHEexd4CIQC1a8LfyQnVspBHUOo51IEhn7k6DWXYUJk0w1VbzGqCBg%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRAIgAVxgdnDNZp6jORyNqHjZYEiRxQ_bA6X_6Ie6Nlp52AwCICyXUnuHqHMmpVDj7zW4uSe9eZfJBphfOJCO5XjnBaVi"
save_path = "C:/Users/tegar/Downloads/video.mp4"

download_file(url, save_path)