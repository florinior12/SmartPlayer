from flask import request, jsonify
from app import app, db
from app.models import Songs
from app.songs_api import track_tags
import datetime

#method for adding songs in the database
def add_song(request):
  #get request's data as json format
  req_json = request.get_json()
  link = req_json['link']
  #date = datetime.datetime.strptime(request.get_json()['date'],"%Y-%m-%d").date()
  yt_title = req_json['yt_title']
  artist = req_json['artist']
  track = req_json['track']
  #timestamps
  created_at = datetime.datetime.now()
  updated_at = datetime.datetime.now()
  #if the artist and song are not know add the song to the database without tags
  if artist == 'Unknown artist' and track == 'Unknown track':
    song = Songs(song_link=link, song_title=yt_title, created_at=created_at, updated_at=updated_at)
  else:
    #get tags from last fm
    tags = track_tags(artist,track,key=app.config['LASTFM_API_KEY'])
    song = Songs(song_link=link, song_title=track, song_artist=artist,  tags=tags, created_at=created_at, updated_at=updated_at)

  try:
    db.session.add(song)
    db.session.commit()
  except Exception as e:
    print('Song already added!')
  
#method to get all songs from database
def show_songs():
  songs = Songs.query.all()
  return songs
#method to delete all songs from databases
def delete_all_songs():
  Songs.query.delete()
  db.session.commit()
