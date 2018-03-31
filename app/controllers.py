from flask import request, jsonify
from app import app, db
from app.models import Songs
from app.songs_api import track_tags
import datetime

def add_song(request):
  req_json = request.get_json()
  #print(req_json)
  link = req_json['link']
  #date = datetime.datetime.strptime(request.get_json()['date'],"%Y-%m-%d").date()
  yt_title = req_json['yt_title']
  artist = req_json['artist']
  track = req_json['track']
  created_at = datetime.datetime.now()
  updated_at = datetime.datetime.now()
  if artist == 'Unknown artist' and track == 'Unknown track':
    song = Songs(song_link=link, song_title=yt_title, created_at=created_at, updated_at=updated_at)
  else:
    tags = track_tags(artist,track,key=app.config['LASTFM_API_KEY'])
    song = Songs(song_link=link, song_title=track, song_artist=artist,  tags=tags, created_at=created_at, updated_at=updated_at)
    
  print('The song is ' + str(song))
  try:
    db.session.add(song)
    db.session.commit()
  except Exception as e:
    print('Song already added!')
  

def show_songs():
  songs = Songs.query.all()
  return songs

def delete_all_songs():
  Songs.query.delete()
  db.session.commit()
