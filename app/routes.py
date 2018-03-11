from flask import render_template, request, jsonify
from app import app, db
from app.youtube_videos import youtube_search
from app.helpers import parse_response
from app.models import Songs
from app.controllers import add_song, show_songs, delete_all_songs
import datetime

@app.route('/show_all', methods=['GET'])
def show_all():
  results = show_songs()
  print(results)
  return render_template('show_all.html', results=results)

@app.route('/addVideo', methods=['POST'])
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


@app.route('/', methods=["GET", "POST"])
@app.route('/index', methods=["GET", "POST"])
def index():
  video_list = []
  if request.form:
    response = youtube_search(q=request.form.get("song"),key=app.config['API_KEY'])
    video_list = parse_response(response)

  return render_template('index.html',title='Home',results=video_list)

