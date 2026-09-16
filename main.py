import os
import json
import datetime



PROJECT_NAME = "YouTube-AutoStudio"



def log(message):

    print(message)



def create_folders():

    folders = [

        "output/videos",
        "output/scripts",
        "output/thumbnails",
        "output/scenes",

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



def load_settings():

    path = "config/settings.json"


    if os.path.exists(path):

        with open(
            path,
            "r"
        ) as file:

            return json.load(file)



    return {

        "channel_name":
        "Nundas"

    }



def pipeline():

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
        "Topic found: "
        + topic
    )



    log(
        "Generating script..."
    )


    script = generate_script(
        topic
    )


    log(
        "AI script generated"
    )



    log(
        "Creating voice..."
    )


    create_voice(
        topic
    )



    log(
        "Creating thumbnail..."
    )


    create_thumbnail(
        script["thumbnail"]
    )



    log(
        "Starting Blender renderer..."
    )


   try:

    render_scene()

    log(
        "Blender render complete"
    )


except Exception as error:

    log(
        "Blender failed: "
        + str(error)
    )



    log(
        "Preparing uploader..."
    )


    log(
        "Preparing analytics..."
    )


    log(
        "Pipeline complete"
    )



def main():

    print("="*40)

    print(
        PROJECT_NAME
    )

    print("="*40)


    create_folders()


    settings = load_settings()


    log(
        "Channel: "
        + settings["channel_name"]
    )


    pipeline()



if __name__ == "__main__":

    main()
