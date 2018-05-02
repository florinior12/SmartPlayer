from app import app
from app import db
try:
  db.create_all()
except Exception as e:
  print('WARNING: DATABASE HAS NOT BEEN FOUND!')
app.run(debug=True)
