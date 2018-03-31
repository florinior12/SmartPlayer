from flask import render_template, request, jsonify, session
from app import app, db
from app.youtube_videos import youtube_search
from app.helpers import parse_response, search_liked
from app.models import Songs
from app.controllers import add_song, show_songs, delete_all_songs
from app.songs_api import top_tracks, search_track
import datetime



@app.route('/show_all', methods=['GET', 'POST'])
def show_all():
  songs = show_songs()
  #print(results)
  return render_template('show_all.html', songs=songs)

@app.route('/add_video', methods=['POST'])
def add_video():
  try:
    add_song(request)
    return jsonify(message="Song added!")
  except Exception as e:
    print(e)
    return jsonify(message="Song failed to add!")
  
@app.route('/delete_all', methods=['GET'])
def delete_all():
  delete_all_songs()
  return render_template('show_all.html',message="Deleted all songs")

@app.route('/play_song', methods = ['POST'])
def play_song():
  if request.get_json()['type'] == 'lastfm':
    query = request.get_json()['artist'] + ' ' + request.get_json()['track']
    response = youtube_search(max_results=1,q=query,key=app.config['YOUTUBE_API_KEY'])
    video = parse_response(response)
    return jsonify({"id":video['id']})
  elif request.get_json()['type'] == 'yt':
    song_info = search_track(request.get_json()['title'], key=app.config['LASTFM_API_KEY']) #returns a dictionary
    return jsonify(song_info)

@app.route('/check_liked', methods=['POST'])
def check_liked():
  liked = search_liked(request.get_json()['id'])
  return jsonify({"liked":liked})

@app.route('/search_song', methods=['POST'])
def search_song():
  response = youtube_search(q=request.get_json()['query'],key=app.config['YOUTUBE_API_KEY'])
  video_list = parse_response(response)
  return render_template('search.html',videos_yt=video_list)

@app.route('/popular_songs', methods=['GET'])
def popular_songs():
  video_list = []
  if not 'songs_list' in session:
      session['songs_list'] = top_tracks(key=app.config['LASTFM_API_KEY'])
  return render_template('popular.html', songs_lfm=session['songs_list'])

@app.route('/', methods=["GET", "POST"])
@app.route('/index', methods=["GET", "POST"])
def index():
  return render_template('base.html')

