from app.models import Songs
def parse_response(response):
  video_list = []
  for video in response[1]:
      _link = "https://www.youtube.com/watch?v=" + video['id']['videoId']
      _title = video['snippet']['title']
      _date = video['snippet']['publishedAt'].split('T')[0]
      _thumbnail = video['snippet']['thumbnails']['default']['url']
      _liked = check_liked(_link)

      video_list.append({'link':_link,
        'title':_title,
        'date':_date,
        'thumbnail':_thumbnail,
        'liked':_liked
        })

  print("Parsed a total of " + str(len(video_list)) + " videos")
  #print(video_list)
  if len(video_list)>1:
    return video_list
  else:
    return video_list[0]

def check_liked(link):
  if Songs.query.filter_by(song_link=link).first():
    return 'Liked'
  else:
    return ''
