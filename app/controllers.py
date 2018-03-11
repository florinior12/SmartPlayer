from flask import request, jsonify
from app import db
from app.models import Songs
import datetime

def add_song(request):
  link = request.get_json()['link']
  date = datetime.datetime.strptime(request.get_json()['date'],"%Y-%m-%d").date()
  title = request.get_json()['title']
  created_at = datetime.datetime.now()
  updated_at = datetime.datetime.now()

  song = Songs(song_link=link, song_date=date, song_title=title, created_at=created_at, updated_at=updated_at)

  db.session.add(song)
  db.session.commit()

def show_songs():
  songs = Songs.query.all()
  return songs

def delete_all_songs():
  Songs.query.delete()
  db.session.commit()
