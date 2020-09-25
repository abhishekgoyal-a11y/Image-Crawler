# Web Crawler

# 1. YOUTUBE
    (A) CHANNEL
         REQUIRE CHANNEL USERNAME OR ID OR URL
            Like:-
              channel url="https://www.youtube.com/user/schafer5" or "https://www.youtube.com/channel/UC4JX40jDee_tINbkjycV4Sg"
              channel username = "schafer5"
              channel id = "UC4JX40jDee_tINbkjycV4Sg"
         DETAILS INCLUDE
              1. Number of Playlist
              2. Channel Details
                   1.total subscribers, videos, views
                   2.all playlists titles, urls, image urls
                   
    (B) PLAYLIST
         REQUIRE PLAYLIST ID OR URL
            Like:-
              playlist url:-"https://www.youtube.com/watch?v=vnd3RfeG3NM&list=PLzMcBGfZo4-lkJr3sqpikNyVzbNZLRiT3" or 
                            "https://www.youtube.com/playlist?list=PLzMcBGfZo4-lkJr3sqpikNyVzbNZLRiT3"
              playlist id:- "PLzMcBGfZo4-lkJr3sqpikNyVzbNZLRiT3"
         DETAILS INCLUDE
              1. Size of Playlist (IN BYTES)
              2. Playlist Details
                   1.VIDEO WISE
                        (A) total comments,views
                        (B) total likes,dislikes
                        (C) time in seconds
                        (D) video, image urls
                        (E) video title
                   1.PLAYLIST WISE
                        (A) total comments,views
                        (B) total likes,dislikes
                        (C) time (hours,minutes,seconds)
                        (F) total videos
              3.Popular videos
                 FILTER BY:-
                    1.Views
                    2.Likes
              4.Playlist Downlaod
                  (A)number of videos
                  (B)from this video to this video
                  (C)till this video
                  (D)from this video
                  (E)specific video like 1,5,7 etc...
    (C) VIDEO

First part will download only one image

What required:- Image Address

Example:- Amirkhan Image

Image Address:- https://upload.wikimedia.org/wikipedia/commons/b/ba/Aamir_Khan_From_The_NDTV_Greenathon_at_Yash_Raj_Studios_%2811%29.jpg

Second part will download all images from that url

What required:- URL

Example:- Amirkhan Images

URL:- https://www.google.com/search?q=amirkhan&rlz=1C1CHBF_enIN828IN828&sxsrf=ALeKk005HXD_iy7Ftgjx9J-bF8i0NKfx9Q:1600179467455&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiL4e-FrevrAhUBXn0KHS6CD9MQ_AUoAnoECB8QBA&biw=1366&bih=625

# Video Crawler

What required:- URL

Example:- YouTube video

URL:- https://www.youtube.com/watch?v=j2WaSbyjRm8

Example:- web video link

URL:- https://www.learningcontainer.com/wp-content/uploads/2020/05/sample-mp4-file.mp4

For more samples:- https://www.learningcontainer.com/mp4-sample-video-files-download/#Sample_MP4_File

# Future Work

1.Download all videos from url


# Youtube API
https://console.developers.google.com/apis/credentials?project=ambient-isotope-289805

http://googleapis.github.io/google-api-python-client/docs/dyn/youtube_v3.html

http://googleapis.github.io/google-api-python-client/docs/dyn/youtube_v3.channels.html

https://developers.google.com/youtube/v3/docs/videos/list

https://developers.google.com/youtube/v3/getting-started
