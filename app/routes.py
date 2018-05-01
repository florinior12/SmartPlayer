from flask import render_template, request, jsonify, session
from app import app, db
from app.youtube_videos import youtube_search
from app.helpers import parse_response, search_liked
from app.models import Songs
from app.controllers import add_song, show_songs, delete_all_songs
from app.songs_api import top_tracks, search_track, artist_top_tracks, genre_top_tracks
import datetime


#this method will return the liked songs from the db and render a html page with these songs
@app.route('/show_all', methods=['GET', 'POST'])
def show_all():
  songs = show_songs()
  #print(results)
  return render_template('show_all.html', songs=songs)

#this method adds a certain song to the db
@app.route('/add_video', methods=['POST'])
def add_video():
  try:
    add_song(request)
    return jsonify(message="Song added!")
  except Exception as e:
    print(e)
    return jsonify(message="Song failed to add!")
  
#this method deletes all songs from db
@app.route('/delete_all', methods=['GET'])
def delete_all():
  delete_all_songs()
  return render_template('show_all.html',message="Deleted all songs")

#this method will play a certain song
@app.route('/play_song', methods = ['POST'])
def play_song():
  #the song can be from youtube or from lastfm
  if request.get_json()['type'] == 'lastfm':
    #if the song is from lastfm, it must be searched on youtube
    query = request.get_json()['artist'] + ' ' + request.get_json()['track']
    response = youtube_search(max_results=1,q=query,key=app.config['YOUTUBE_API_KEY'])
    video = parse_response(response)
    #we will return the youtube id of the song in order to be played on youtube
    return jsonify({"id":video['id']})
  elif request.get_json()['type'] == 'yt':
    #if the song is obtained from youtube search we start playing it and search for its details on lastfm
    song_info = search_track(request.get_json()['title'], key=app.config['LASTFM_API_KEY']) #returns a dictionary
    #return the details from lastfm
    return jsonify(song_info)

#check if a certain song is liked (if it's in the db)
@app.route('/check_liked', methods=['POST'])
def check_liked():
  liked = search_liked(request.get_json()['id'])
  return jsonify({"liked":liked})

#search for a certain song on youtube
@app.route('/search_song', methods=['POST'])
def search_song():
  response = youtube_search(q=request.get_json()['query'],key=app.config['YOUTUBE_API_KEY'])
  video_list = parse_response(response)
  return render_template('search.html',videos_yt=video_list)

#this method uses the lastfm api in order to obtain some new songs
#currently it uses the same html and changes the parameters that change the html
@app.route('/popular_songs', methods=['GET', 'POST'])
def popular_songs():
  req_json = request.get_json()
  #here is obtains popular songs of the moment
  if req_json['type'] == 'popular':
    #looks in the current session if the popular songs have already been obtained to not get them again
    if not 'popular_songs' in session:
        session['popular_songs'] = top_tracks(key=app.config['LASTFM_API_KEY'])
    return render_template('popular.html', songs_lfm=session['popular_songs'])
  #here is obtains the top songs of the current playing artist
  elif req_json['type'] == 'artist_top':
    sess_param = req_json['artist_name']
    if not sess_param in session:
      session[sess_param] = artist_top_tracks(sess_param,key=app.config['LASTFM_API_KEY'])
    return render_template('popular.html', songs_lfm=session[sess_param])
  #get songs from the same genre as the current playing
  elif req_json['type'] == 'genre_top':
    sess_param = req_json['artist_name'] + req_json['track_name']
    if not sess_param in session:
      session[sess_param] = genre_top_tracks(req_json['artist_name'],req_json['track_name'],key=app.config['LASTFM_API_KEY'])
    return render_template('popular.html', songs_lfm=session[sess_param])



@app.route('/', methods=["GET", "POST"])
@app.route('/index', methods=["GET", "POST"])
def index():
  return render_template('base.html')

