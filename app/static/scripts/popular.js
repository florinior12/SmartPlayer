
$('a#play_track_name').click(function() {
  var track_name = $(this).text();
  var artist_name = $(this).closest('tr').next().text();
  $.ajax ({
    url : '/play_song',
    data: JSON.stringify({track: track_name, artist: artist_name, type: 'lastfm'}),
    type: 'POST',
    success: function(response) {
      player.loadVideoById(response['id']);
      $('h5#song_title').text(track_name);
      $('h6#song_artist').text(artist_name);

    },
    dataType: "json",
    contentType: 'application/json;charset=UTF-8'
  });
  return  false;
});