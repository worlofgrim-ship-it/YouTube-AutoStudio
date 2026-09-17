import os
import json

from system.setup import setup_project
from system.detector import check_system


PROJECT_NAME = "YouTube-AutoStudio"


def log(text):
    print(text)


def load_settings():

    path = "config/settings.json"

    if not os.path.exists(path):

        os.makedirs("config", exist_ok=True)

        settings = {

            "channel_name": "Nundas",

            "blender_path": "",

            "ffmpeg_path": "",

            "video": {

                "fps": 30,

                "frames": 150,

                "resolution": "360x640"

            },

            "youtube": {

                "enabled": False,

                "privacy": "private"

            }

        }


        with open(
            path,
            "w",
            encoding="utf8"
        ) as f:

            json.dump(
                settings,
                f,
                indent=4
            )


        return settings


    with open(
        path,
        "r",
        encoding="utf8"
    ) as f:

        return json.load(f)



def pipeline(settings):


    print()

    print("Starting AutoStudio pipeline")

    print("-----------------------------")


    # future modules go here

    print("Finding video idea...")

    print("Generating script...")

    print("Creating voice...")

    print("Creating thumbnail...")

    print("Rendering Blender scene...")

    print("Encoding MP4...")

    print("Uploading...")

    print()

    print("Pipeline finished")



def main():


    print("="*40)

    print(PROJECT_NAME)

    print("="*40)


    setup_project()


    settings = load_settings()


    print()

    print(
        "Channel:",
        settings["channel_name"]
    )


    settings = check_system(settings)

save_settings(settings)


    pipeline(settings)



if __name__ == "__main__":

    main()
