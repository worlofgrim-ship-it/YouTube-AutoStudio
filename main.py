import os
import json
import datetime


PROJECT_NAME = "YouTube-AutoStudio"


def log(message):

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    os.makedirs("logs", exist_ok=True)

    with open(
        "logs/runtime.log",
        "a",
        encoding="utf-8"
    ) as file:
        file.write(
            f"[{timestamp}] {message}\n"
        )

    print(message)



def create_folders():

    folders = [

        "logs",

        "output/videos",
        "output/thumbnails",
        "output/scripts",

        "ideas",

        "script/prompts",

        "voice",

        "video",

        "thumbnail",

        "upload",

        "analytics",

        "scheduler",

        "config"

    ]


    for folder in folders:
        os.makedirs(
            folder,
            exist_ok=True
        )


    log(
        "Folder structure verified"
    )



def load_settings():

    path = "config/settings.json"


    if not os.path.exists(path):

        settings = {

            "channel_name": "Nundas",

            "video_type":
            "youtube_shorts",

            "style":
            "3D animated documentary",

            "length_seconds":
            60

        }


        with open(
            path,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                settings,
                file,
                indent=4
            )


        log(
            "Created default settings"
        )


        return settings



    with open(
        path,
        "r",
        encoding="utf-8"
    ) as file:

        settings = json.load(file)


    log(
        "Settings loaded"
    )


    return settings




def pipeline():

    from ideas.trend_finder import find_topic

    from script.generator import generate_script

    from voice.tts import create_voice

    from thumbnail.generator import create_thumbnail



    # -------------------------
    # FIND IDEA
    # -------------------------

    log(
        "Finding video idea..."
    )


    topic = find_topic()


    log(
        "Topic found: "
        + topic
    )



    # -------------------------
    # GENERATE SCRIPT
    # -------------------------

    log(
        "Generating script..."
    )


    script_data = generate_script(
        topic
    )


    log(
        "AI script generated"
    )


    log(
        "Script saved in output/scripts"
    )



    # -------------------------
    # VOICE
    # -------------------------

    log(
        "Creating voice..."
    )


    create_voice(
        script_data["title"]
    )



    # -------------------------
    # THUMBNAIL
    # -------------------------

    log(
        "Creating thumbnail..."
    )


    create_thumbnail(
        script_data["thumbnail"]
    )



    # -------------------------
    # FUTURE SYSTEMS
    # -------------------------

    log(
    "Preparing Blender engine..."
)


try:

    from video.blender_render import render_scene

    render_scene()


    log(
        "Blender engine ready"
    )


except Exception as e:

    log(
        "Blender engine skipped: "
        + str(e)
    )

    log(
        "Preparing YouTube uploader..."
    )

    log(
        "Preparing analytics..."
    )


    log(
        "Video pipeline finished"
    )




def main():

    print("=" * 40)

    print(
        PROJECT_NAME
    )

    print("=" * 40)



    create_folders()


    settings = load_settings()


    log(
        "Channel: "
        + settings["channel_name"]
    )


    pipeline()




if __name__ == "__main__":

    main()
