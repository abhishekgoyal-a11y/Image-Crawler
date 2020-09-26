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
                        (D) total videos
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
         REQUIRE VIDEO ID OR URL
            Like:-
              video url="https://www.youtube.com/watch?v=zmdjNSmRXF4"
              video id = "zmdjNSmRXF4"
         DETAILS INCLUDE
              1. Video Details
                  (A)video title
                  (B)video image url
                  (C)time in seconds
                  (D)total comments,views
                  (E)total likes,dislikes
                  (F)time(hours:minutes:seconds)
              2.Donwload video
              3.Video Size(IN BYTES)
# 2. IMAGE
    (A) FIRST PART(downlaod ony one image)
            REQUIRE IMAGE ADDRESS
                Example:- Amirkhan Image
                Like:-
                    Image Address:- https://upload.wikimedia.org/wikipedia/commons/b/ba/Aamir_Khan_From_The_NDTV_Greenathon_at_Yash_Raj_Studios_%2811%29.jpg

    (B) SECOND PART(downlaod all images)
            REQUIRE WEB URL
                Example:- Amirkhan Images
                Like:-
                    URL:- https://www.google.com/search?q=amirkhan&rlz=1C1CHBF_enIN828IN828&sxsrf=ALeKk005HXD_iy7Ftgjx9J-bF8i0NKfx9Q:1600179467455&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiL4e-FrevrAhUBXn0KHS6CD9MQ_AUoAnoECB8QBA&biw=1366&bih=625

# 3. [Price Tracker App](https://github.com/abhishekgoyal-a11y/Price-tracker-app/tree/master/education%20api)
    (A) Ecommerce Website(Amazon,Ebay,Flipkart,Shopclues,Snapdeal)
            REQUIRE PRODUCT URL
                Example:- Redmi Note 9 Pro
                Like:-
                    URL:- https://www.amazon.in/Test-Exclusive-549/dp/B077PWBC78/ref=sxin_3?ascsubtag=amzn1.osa.8e66cb3e-b6fd-442f-941a-90aa55c4b231.A21TJRUUN4KGV.en_IN&creativeASIN=B077PWBC78&cv_ct_cx=mobiles&cv_ct_id=amzn1.osa.8e66cb3e-b6fd-442f-941a-90aa55c4b231.A21TJRUUN4KGV.en_IN&cv_ct_pg=search&cv_ct_wn=osp-single-source-gl-ranking&dchild=1&keywords=mobiles&linkCode=oas&pd_rd_i=B077PWBC78&pd_rd_r=400e04f7-8be0-4235-a63d-e5ccbe9986c7&pd_rd_w=TY55j&pd_rd_wg=lOANA&pf_rd_p=f703f81b-4f72-40ee-805a-081e743c7df4&pf_rd_r=FZ6TZSRMQPMPKJNT67SB&qid=1601110200&sr=1-1-5b72de9d-29e4-4d53-b588-61ea05f598f4&tag=technologytoday-21
                OUTPUT:-
                    PRODUCT NAME:- Redmi Note 9 Pro (Interstellar Black, 4GB RAM, 64GB Storage) - Latest 8nm Snapdragon 720G & Gorilla Glass 5 Protection
                    PRODUCT PRICE:- 13,999.00 
            Similarly you can search any url 
    (A) Elearning Website(Coursera,Edx,Udemy)
            REQUIRE COURSE URL
                Example:- Python programming
                Like:-
                    URL:- https://www.udemy.com/course/python-the-complete-python-developer-course/
                OUTPUT:-
                    COURSE NAME:- Learn Python Programming Masterclass
                    COURSE PRICE:- ₹8,640
            Similarly you can search any url 
                    
# Youtube API(RESOURCES)

https://console.developers.google.com/apis/credentials?project=ambient-isotope-289805

http://googleapis.github.io/google-api-python-client/docs/dyn/youtube_v3.html

http://googleapis.github.io/google-api-python-client/docs/dyn/youtube_v3.channels.html

https://developers.google.com/youtube/v3/docs/videos/list

https://developers.google.com/youtube/v3/getting-started
