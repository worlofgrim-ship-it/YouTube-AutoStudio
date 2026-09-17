import os
import json


PROJECT_NAME = "YouTube-AutoStudio v1.7.1"


# ==============================
# Logging
# ==============================

def log(message):

    print(message)



# ==============================
# Folder Setup
# ==============================

def create_folders():

    folders = [

        "output",

        "output/videos",

        "output/audio",

        "output/scripts",

        "output/thumbnails",

        "output/scenes",

        "logs",

        "config",

        "youtube"

    ]


    for folder in folders:

        os.makedirs(
            folder,
            exist_ok=True
        )


    log(
        "Folder structure verified"
    )



# ==============================
# Settings
# ==============================

def load_settings():

    path = "config/settings.json"


    if os.path.exists(path):

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



    os.makedirs(
        "config",
        exist_ok=True
    )



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
        "Default settings created"
    )


    return settings




def save_settings(settings):


    with open(
        "config/settings.json",
        "w",
        encoding="utf-8"
    ) as file:


        json.dump(
            settings,
            file,
            indent=4
        )



# ==============================
# Pipeline
# ==============================

def pipeline(settings):


    from ideas.trend_finder import find_topic
    from script.generator import generate_script
    from voice.tts import create_voice
    from thumbnail.generator import create_thumbnail
    from video.blender_render import render_scene



    log(
        "Finding video idea..."
    )


    topic = find_topic()


    log(
        "Topic found: " + topic
    )



    log(
        "Generating script..."
    )


    script = generate_script(
        topic
    )


    log(
        "Script generated"
    )



    log(
        "Creating voice..."
    )


    try:

        create_voice(
            script
        )


        log(
            "Voice created"
        )


    except Exception as error:


        log(
            "Voice error: " 
            + str(error)
        )



    log(
        "Creating thumbnail..."
    )


    try:

        create_thumbnail(
            script["thumbnail"]
        )


        log(
            "Thumbnail created"
        )


    except Exception as error:


        log(
            "Thumbnail error: "
            + str(error)
        )



    log(
        "Starting Blender..."
    )


    try:


        render_scene(
            settings
        )


        log(
            "Blender render complete"
        )


    except TypeError:


        # compatibility with older renderer

        render_scene()


        log(
            "Blender render complete"
        )


    except Exception as error:


        log(
            "Blender error: "
            + str(error)
        )



    log("Uploading to YouTube...")


from uploader.youtube_upload import upload_video


upload_video(

    script["title"],

    script["description"]

)


log("Upload complete")


    if settings["youtube"]["enabled"]:


        try:

            from youtube.uploader import upload_video

            upload_video(
                settings
            )


        except Exception as error:


            log(
                "Upload error: "
                + str(error)
            )


    else:

        log(
            "YouTube upload disabled"
        )



    log(
        "Preparing analytics..."
    )



    log(
        "Pipeline complete"
    )



# ==============================
# Main
# ==============================

def main():


    print("=" * 40)

    print(PROJECT_NAME)

    print("=" * 40)



    create_folders()



    settings = load_settings()



    log(
        "Channel: "
        + settings["channel_name"]
    )



    # System detector

    try:

        from system.detector import check_system


        settings = check_system(
            settings
        )


        save_settings(
            settings
        )


    except Exception as error:


        log(
            "System check skipped: "
            + str(error)
        )



    print()



    pipeline(
        settings
    )





if __name__ == "__main__":

    main()
