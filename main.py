import os
import json
import datetime


PROJECT_NAME = "YouTube-AutoStudio"
SETTINGS_FILE = "config/settings.json"



def log(message):

    print(message)

    os.makedirs("logs", exist_ok=True)

    with open(
        "logs/latest.log",
        "a",
        encoding="utf-8"
    ) as file:

        file.write(
            f"[{datetime.datetime.now()}] {message}\n"
        )



def create_folders():

    folders = [

        "output/videos",
        "output/scripts",
        "output/thumbnails",
        "output/scenes",
        "output/audio",

        "logs",

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



def first_time_setup():

    print("\nFirst time setup\n")


    channel = input(
        "Channel name: "
    )


    blender = input(
        "Blender executable path: "
    )


    ffmpeg = input(
        "FFmpeg executable path: "
    )


    settings = {

        "channel_name": channel,

        "blender_path": blender,

        "ffmpeg_path": ffmpeg,

        "youtube_upload": False,

        "fps":30,

        "resolution":"360x640"

    }


    with open(
        SETTINGS_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            settings,
            file,
            indent=4
        )


    print(
        "Setup complete!"
    )


    return settings




def load_settings():

    os.makedirs(
        "config",
        exist_ok=True
    )


    if not os.path.exists(
        SETTINGS_FILE
    ):

        return first_time_setup()



    with open(
        SETTINGS_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        settings=json.load(file)



    log(
        "Settings loaded"
    )


    return settings




def pipeline(settings):


    try:

        from ideas.trend_finder import find_topic

        from script.generator import generate_script

        from voice.tts import create_voice

        from thumbnail.generator import create_thumbnail

        from video.blender_render import render_scene



    except Exception as error:

        log(
            "Module error: "
            + str(error)
        )

        return




    log(
        "Finding video idea..."
    )


    topic=find_topic()


    log(
        "Topic: "
        + topic
    )



    log(
        "Generating script..."
    )


    script=generate_script(
        topic
    )


    log(
        "Script generated"
    )



    log(
        "Creating voice..."
    )


    create_voice(
        script
    )



    log(
        "Creating thumbnail..."
    )


    create_thumbnail(
        script["thumbnail"]
    )



    log(
        "Starting Blender..."
    )


    render_scene(
        settings
    )


    log(
        "Video render finished"
    )



if settings.get("youtube_upload"):

    log(
        "Uploading to YouTube..."
    )

    from youtube.uploader import upload_video


    upload_video(
        video_file="output/videos/autostudio_short.mp4",
        title=topic,
        description=script["description"],
        thumbnail="output/thumbnails/thumbnail.png"
    )



    log(
        "ALL COMPLETE"
    )





def main():


    print("="*40)

    print(PROJECT_NAME)

    print("="*40)



    create_folders()



    settings=load_settings()



    log(
        "Channel: "
        + settings["channel_name"]
    )



    pipeline(
        settings
    )




if __name__=="__main__":

    main()
