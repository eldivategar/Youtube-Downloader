from flask import Flask, redirect, render_template, url_for, request, send_file, Response, stream_with_context
from pytube import YouTube

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

import isodate
import requests

app = Flask(__name__)

API_KEY = "AIzaSyCo1xZ7bw0IHDErAoOBuqC-fWraUu0esPo"

youtube = build('youtube', 'v3', developerKey=API_KEY)

@app.before_request
def redirect_youtubele():
    url = request.url
    if 'youtube.com/watch?v=' in url:
        video_id = url.split('=')[1]
        # print('url asli=', url, '\n')
        # print('url_video=', video_id, '\n')
        return redirect(url_for('choose_resolution', VIDEO_ID=video_id))

@app.route('/', defaults={'placeholder': 'Link', 'error': False})
@app.route('/<placeholder>', defaults={'error': False}, methods=['GET'])
@app.route('/<placeholder>/<error>', methods=['GET'])
def home(placeholder, error):
    if error == 'Not_Found':
        return render_template('index.html', placeholder = 'Link', error = True)
    else:
        if placeholder == 'Link':
            return render_template('index.html', placeholder = 'Link', error = False)
        elif placeholder == 'title':
            return render_template('index.html', placeholder = 'Title', error = False)
        else:
            return 'Halaman tidak ditemukan'


@app.route('/result', methods=['GET'])
def get_list_video():
    get_title = request.args.get('title')
    
    result = get_list_video(get_title)
    
    return render_template('single-page-options.html', result = result, get_title = get_title)


@app.route('/choose-resolution/', methods=['GET'])       
@app.route('/choose-resolution/<VIDEO_ID>')       
def choose_resolution(VIDEO_ID=None):   
    if VIDEO_ID is None:
        get_link = request.args.get('link')
        VIDEO_ID = get_link[-11:]

    result = get_video_info(VIDEO_ID)

    if result is None:
        # Handle the case where no video information was found
        return redirect(url_for('home', placeholder='Link', error='Not_Found'))

    title = result['title']
    channel = result['channel']
    description = result['description']
    views = result['views']
    duration = result['duration']
    likes = result['likes']
    thumbnail = result['thumbnail']

    resolutions_MP4 = get_resolutions(VIDEO_ID)
    resolutions_MP3 = get_resolutions(VIDEO_ID, type='audio')
    
    
    return render_template('resolutions.html', VIDEO_ID=VIDEO_ID, title = title, channel = channel, description = description, views = views, duration = duration, likes = likes, thumbnail = thumbnail, resolutions_MP4 = resolutions_MP4.items(), resolutions_MP3 = resolutions_MP3.items())


@app.route('/download_files/<VIDEO_ID>/<resolution>/<title>/<type>')
def download_files(VIDEO_ID, resolution, title, type):
    url = f'https://www.youtube.com/watch?v={VIDEO_ID}'

    if type == 'video':
        Files = YouTube(url).streams.filter(type='video', file_extension='mp4', progressive=True, resolution=f'{resolution}p').desc().first()
        file_url = Files.url

        response = requests.get(file_url, stream=True)        
        if response.status_code == 200:
            return send_file(response.raw, as_attachment=True, download_name=f'{title} - {resolution}p.mp4')
        
        else:
            print('Gagal mengunduh...')

        # return send_file(video_content, as_attachment=True, download_name=f'{title} - {resolution}p.mp4', mimetype='video/mp4')

    elif type == 'audio':
        Files = YouTube(url).streams.filter(type='audio', abr=f'{resolution}kbps').first()
        file_url = Files.url

        headers = {
            'Range': 'bytes=0-',
            'Accept-Ranges': 'bytes'
        }

        response = requests.get(file_url, headers=headers, stream=True)
        headers.pop('Range', None)
        headers.pop('Accept-Ranges', None)

        return send_file( stream_with_context(response.iter_content(chunk_size=1024)), as_attachment=True, download_name=f'{title} - {resolution}kbps.mp3', mimetype='audio/mpeg')



def get_resolutions(VIDEO_ID, type='video'):
    url = f'https://www.youtube.com/watch?v={VIDEO_ID}'

    if type == 'video':
        Files = YouTube(url).streams.filter(type='video', progressive=True, file_extension='mp4')
        resolution_attr = 'resolution'
        str_for_replace = 'p'
    elif type == 'audio':
        Files = YouTube(url).streams.filter(type='audio')
        resolution_attr = 'abr'
        str_for_replace = 'kbps'
    else:
        return {}

    resolutions = {}

    for stream in Files:
        resolution = getattr(stream, resolution_attr).replace(str_for_replace, '')
        filesize = stream.filesize
        filesize = format_file_size(filesize)
        resolutions[resolution] = filesize
    
    sorted_resolutions = dict(sorted(resolutions.items(), key=lambda x: int(x[0]), reverse=True))
    return sorted_resolutions



def get_video_info(VIDEO_ID):
    try:
        video_response = youtube.videos().list(
            part='snippet, contentDetails, statistics',
            id=VIDEO_ID
        ).execute()

        if video_response is None or not video_response['items']:
            print("Video tidak ditemukan")
            return None

        else:
            title = video_response['items'][0]['snippet']['title']
            channel = video_response['items'][0]['snippet']['channelTitle']
            description = video_response['items'][0]['snippet']['description']
            duration = video_response['items'][0]['contentDetails']['duration']
            duration_in_seconds = isodate.parse_duration(duration).total_seconds()
            duration_formatted = str(int(duration_in_seconds // 3600)) + ":" + \
                                str(int((duration_in_seconds % 3600) // 60)).zfill(2) + ":" + \
                                str(int(duration_in_seconds % 60)).zfill(2)
            thumbnail = video_response['items'][0]['snippet']['thumbnails']['standard']['url']
            likes = video_response['items'][0]['statistics'].get('likeCount', 'N/A')
            likes = format_likes(int(likes))
            views = video_response['items'][0]['statistics'].get('viewCount', 'N/A')
            views = format_views(int(views))

        return {'title': title, 'channel': channel, 'description': description, 
                'duration': duration_formatted, 'thumbnail': thumbnail, 'likes': likes, 'views': views}

    except HttpError as e:
        print('Error: ', e)

def get_list_video(TITLE):

    try:
        search_response = youtube.search().list(
            q=TITLE,
            type='video',
            part='id,snippet',
            maxResults = 15
        ).execute()
        
        videos = []
        for search_result in search_response.get('items', []):
            videos.append({
                'title': search_result['snippet']['title'],
                'url': search_result['id']['videoId'],
                'thumbnail': search_result['snippet']['thumbnails']['high']['url'],
                'description':search_result['snippet']['description']
            })        
        
        return videos

    except HttpError as e:
        print(f"An error occurred: {e}")



# Parsing Format
def format_file_size(file_size):
    if file_size < 1000:
        return f"{file_size} B"
    elif file_size < 1000000:
        return f"{file_size / 1000:.1f} KB"
    elif file_size < 1000000000:
        return f"{file_size / 1000000:.1f} MB"
    else:
        return f"{file_size / 1000000000:.1f} GB"


def format_views(views):
    if views >= 1000000000:
        return '{:.1f}B'.format(views / 1000000000)
    elif views >= 1000000:
        return '{:.1f}M'.format(views / 1000000)
    elif views >= 1000:
        return '{:.1f}K'.format(views / 1000)
    else:
        return '{}'.format(views)

def format_likes(likes):
    if likes >= 1000000000:
        return '{:.1f}B'.format(likes / 1000000000)
    elif likes >= 1000000:
        return '{:.1f}M'.format(likes / 1000000)
    elif likes >= 1000:
        return '{:.1f}K'.format(likes / 1000)
    else:
        return '{}'.format(likes)


if __name__ == '__main__':
    app.run(debug=True)