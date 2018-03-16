from flask import render_template, request, jsonify
from app import app, db
from app.youtube_videos import youtube_search
from app.helpers import parse_response, search_liked
from app.models import Songs
from app.controllers import add_song, show_songs, delete_all_songs
from app.songs_api import top_tracks
import datetime

@app.route('/show_all', methods=['GET'])
def show_all():
  results = show_songs()
  #print(results)
  return render_template('show_all.html', results=results)

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
  return render_template('index.html',title='Home',message="Deleted all songs")

@app.route('/play_song', methods = ['POST'])
def play_song():
  query = request.get_json()['artist'] + ' ' + request.get_json()['track']
  #print(query)
  response = youtube_search(max_results=1,q=query,key=app.config['YOUTUBE_API_KEY'])
  video = parse_response(response)
  #print(video['id'])
  return jsonify({"id":video['id']})

@app.route('/check_liked', methods=['POST'])
def check_liked():
  print("I RECEIVED " + request.get_json()['id'])
  liked = search_liked(request.get_json()['id'])
  return jsonify({"liked":liked})

@app.route('/', methods=["GET", "POST"])
@app.route('/index', methods=["GET", "POST"])
def index():
  video_list = []
  songs_list = []
  if request.form:
    response = youtube_search(q=request.form.get("song"),key=app.config['YOUTUBE_API_KEY'])
    video_list = parse_response(response)
  else:
    songs_list = top_tracks(key=app.config['LASTFM_API_KEY'])
    

  return render_template('index.html',title='Home',videos_yt=video_list, songs_lfm=songs_list)

