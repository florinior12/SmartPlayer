$(document).ready(function () {
    var liked = false;
    $(function() {
      $('button.like_button').click(function() {
          // var video_date = $(this).closest('tr')
          //   .prev()
          //   .find('td.video_date')
          //   .html();
          // var video_id = $(this).closest('tr')
          //   .prev()
          //   .prev()
          //   .find('td.video_id')
          //   .find('a')
          //   .attr('href');
          // var video_title = $(this).closest('tr')
          //   .prev()
          //   .prev()
          //   .find('td.video_id')
          //   .find('.video_title')
          //   .html();
          var button = $(this);
          //console.log(player.getVideoData());

          $.ajax({
              url: '/add_video',
              data: JSON.stringify({ link:player.getVideoData()['video_id'], title:player.getVideoData()['title']}),
              type: 'POST',
              success: function(response) {
                  $("#love_button").attr("src","static/images/liked.png");
              },
              error: function(response) {
                  console.log("Something went wrong! See response below" )
                  console.log(response)
              },
              dataType: "json",
              contentType: 'application/json;charset=UTF-8'

          });
      });
      $('a.play_id').click(function() {
        console.log('NOT DEAD');
        play_button = $(this);
        $.ajax ({
          url : '/play_song',
          data: JSON.stringify({title: play_button.text(), type: 'yt'}),
          type: 'POST',
          success: function(response) {
            player.loadVideoById(play_button.attr('id')); //get video id from url
            $('h5#song_title').text(response['title']);
            $('h6#song_artist').text(response['artist']);
          },
          dataType: "json",
          contentType: 'application/json;charset=UTF-8'
        })
        return false;
      });
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
    });
});
