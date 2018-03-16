from app import db

class Songs(db.Model):
  song_id = db.Column('song_id', db.Integer, primary_key = True,autoincrement=True)
  song_link = db.Column(db.String(100))
  song_title = db.Column(db.String(50))
  song_date = db.Column(db.Date())
  created_at = db.Column(db.DateTime())
  updated_at = db.Column(db.DateTime())

  def __init__(self, song_link, song_title, created_at, updated_at, song_date=None):
    self.song_link = song_link
    self.song_title = song_title
    self.song_date = song_date
    self.created_at = created_at
    self.updated_at = updated_at
