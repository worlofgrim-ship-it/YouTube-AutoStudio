import os

from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

from google_auth_oauthlib.flow import InstalledAppFlow


SCOPES = [
    "https://www.googleapis.com/auth/youtube.upload"
]


VIDEO_FILE = "output/videos/autostudio_short.mp4"

THUMBNAIL_FILE = "output/thumbnails/thumbnail.png"


CLIENT_SECRET = "config/client_secret.json"



def authenticate():

    flow = InstalledAppFlow.from_client_secrets_file(
        CLIENT_SECRET,
        SCOPES
    )

    credentials = flow.run_local_server(
        port=8080
    )


    youtube = build(
        "youtube",
        "v3",
        credentials=credentials
    )

    return youtube



def upload_video(title, description):

    youtube = authenticate()


    request = youtube.videos().insert(

        part="snippet,status",

        body={

            "snippet": {

                "title": title,

                "description": description,

                "tags": [
                    "science",
                    "what if",
                    "Nundas"
                ],

                "categoryId": "28"

            },

            "status": {

                "privacyStatus": "private"

            }

        },

        media_body=MediaFileUpload(
            VIDEO_FILE,
            chunksize=-1,
            resumable=True
        )

    )


    response = request.execute()


    video_id = response["id"]


    print(
        "Uploaded:",
        video_id
    )


    upload_thumbnail(
        youtube,
        video_id
    )



def upload_thumbnail(
        youtube,
        video_id
):

    if not os.path.exists(
        THUMBNAIL_FILE
    ):
        return


    youtube.thumbnails().set(

        videoId=video_id,

        media_body=MediaFileUpload(
            THUMBNAIL_FILE
        )

    ).execute()


