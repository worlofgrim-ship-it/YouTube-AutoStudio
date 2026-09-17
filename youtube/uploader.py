import os

from googleapiclient.discovery import build

from googleapiclient.http import MediaFileUpload


from youtube.auth import get_credentials

from youtube.metadata import create_metadata



VIDEO_FILE = "output/videos/autostudio_short.mp4"

THUMBNAIL_FILE = "output/thumbnails/thumbnail.png"



def upload_video(settings):


    print(
        "Connecting to YouTube..."
    )


    credentials = get_credentials()


    youtube = build(

        "youtube",

        "v3",

        credentials=credentials

    )


    metadata = create_metadata(

        settings.get(

            "last_topic",

            "Amazing discovery"

        )

    )



    body = {


        "snippet":

        {


            "title":

            metadata["title"],


            "description":

            metadata["description"],


            "tags":

            metadata["tags"],


            "categoryId":

            "28"

        },


        "status":

        {


            "privacyStatus":

            settings["youtube"]["privacy"]

        }

    }



    media = MediaFileUpload(

        VIDEO_FILE,

        chunksize=1024*1024,

        resumable=True

    )



    request = youtube.videos().insert(

        part="snippet,status",

        body=body,

        media_body=media

    )



    response = None



    while response is None:


        status,response = request.next_chunk()


        if status:

            print(

                "Uploading:",

                int(status.progress()*100),

                "%"

            )



    video_id = response["id"]



    print()

    print(

        "Uploaded!"

    )


    print(

        "Video ID:",

        video_id

    )



    if os.path.exists(THUMBNAIL_FILE):


        youtube.thumbnails().set(

            videoId=video_id,

            media_body=

            MediaFileUpload(

                THUMBNAIL_FILE

            )

        ).execute()



        print(

            "Thumbnail uploaded"

        )
