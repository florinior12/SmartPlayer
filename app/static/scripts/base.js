$(document).ready(function () {
    //hide the laoding circle
    $('#loading_songs').hide();
    //function executed when searching for a song on youtube
    //makes an ajax request fo the server, which is handled by the methods from routes.py
    //the ajax request sends the search query and the server will return the response which is html format containing the videos
    function yt_search() {
      $.ajax({
            url: '/search_song',
              data: JSON.stringify({ query : $('#search_query').val()}),
              type: 'POST',
              beforeSend : function() {
              $('#my_container').html('');
              $('#loading_songs').show();

            },
              success: function(response) {
                  $('#loading_songs').hide();
                  $('#my_container').html(response);
              },
              error: function(response) {
                  console.log("Something went wrong! See response below" )
                  console.log(response)
              },
              contentType: 'application/json;charset=UTF-8'
          });
    }
    //execute the yt_search function when clicking the search button
    $('button#search_button').click(function() {
           yt_search();
           return false;
        });
    //execute yt_search whne hitting enter on the text input area
    $('input#search_query').on('keydown', function(e) {
        if (e.which == 13) {
            e.preventDefault();
            yt_search();
        }
      });

    //get all the songs from the db in html format and put them in a div
    $('#show_songs').click(function() {
           $.ajax({
            url: '/show_all',
            type: 'GET',
            success: function(response) {
                  $('#my_container').html(response);
              }
          });
           return false;
        });

    //when user clicks the like button make an ajax request to add the song to the db
    //if the request is successfull the like button changes
    $('button.like_button').click(function() {
        var button = $(this);

        $.ajax({
            url: '/add_video',
            data: JSON.stringify({ link:player.getVideoData()['video_id'],
             yt_title:player.getVideoData()['title'],
              artist:$('#song_artist').text(),
               track:$('#song_title').text()}),
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

    //when clicking anchors having index_page class the app asks for the popular songs of the moment
    $('a.index_page').click(function() {
      $.ajax({
        url  : '/popular_songs',
        type : 'POST',
        data: JSON.stringify({type:'popular'}),
        beforeSend : function() {
          $('#my_container').html('');
          $('#loading_songs').show();

        },
        success: function(response) {
          $('#loading_songs').hide();
          $('#my_container').html(response);
      },
        contentType: 'application/json;charset=UTF-8'
      });
      return false;
    });   
    //get more songs from the artist 
    $('a.more_artist').click(function() {
      $.ajax({
        url : '/popular_songs',
        type: 'POST',
        beforeSend : function() {
          console.log("WDADADASDASDAS");
          $('#my_container').html('');
          $('#loading_songs').show();

        },
        data: JSON.stringify({type:'artist_top',artist_name:$('h6#song_artist').text()}),
        success: function(response) {
          $('#loading_songs').hide();
          $('#my_container').html(response);
        },
        contentType: 'application/json;charset=UTF-8'
      });
      return false;
    });
    //get more songs of same genre
    $('a.more_genre').click(function() {
      $.ajax({
        url : '/popular_songs',
        type: 'POST',
        beforeSend : function() {
          $('#my_container').html('');
          $('#loading_songs').show();

        },
        data: JSON.stringify({type:'genre_top',artist_name:$('h6#song_artist').text(),track_name:$('h5#song_title').text()}),
        success: function(response) {
          $('#loading_songs').hide();
          $('#my_container').html(response);
        },
        contentType: 'application/json;charset=UTF-8'
      });
      return false;
    });
});
