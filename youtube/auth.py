import os

from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials


SCOPES = [

    "https://www.googleapis.com/auth/youtube.upload"

]


TOKEN_FILE = "youtube/token.json"

CLIENT_FILE = "youtube/client_secret.json"



def get_credentials():


    creds = None


    if os.path.exists(TOKEN_FILE):

        creds = Credentials.from_authorized_user_file(

            TOKEN_FILE,

            SCOPES

        )


    if not creds or not creds.valid:


        flow = InstalledAppFlow.from_client_secrets_file(

            CLIENT_FILE,

            SCOPES

        )


        creds = flow.run_local_server(

            port=0

        )


        with open(

            TOKEN_FILE,

            "w"

        ) as file:


            file.write(

                creds.to_json()

            )


    return creds
