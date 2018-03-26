$('a.play_id').click(function() {
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