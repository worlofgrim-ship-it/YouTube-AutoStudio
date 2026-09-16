import os
import json
import datetime


PROJECT_NAME = "YouTube-AutoStudio"


def log(message):

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    os.makedirs("logs", exist_ok=True)

    with open("logs/runtime.log", "a", encoding="utf-8") as file:
        file.write(f"[{timestamp}] {message}\n")

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
        os.makedirs(folder, exist_ok=True)

    log("Folder structure verified")


def load_settings():

    path = "config/settings.json"

    if not os.path.exists(path):

        settings = {
            "channel_name": "Nundas",
            "video_type": "youtube_shorts",
            "style": "3D animated documentary"
        }

        with open(path, "w") as file:
            json.dump(settings, file, indent=4)

        return settings


    with open(path, "r") as file:
        return json.load(file)



def pipeline():

    from ideas.trend_finder import find_topic
    from script.generator import generate_script
    from voice.tts import create_voice
    from thumbnail.generator import create_thumbnail


    log("Finding video idea...")

    topic = find_topic()

    log(f"Topic found: {topic}")


    log("Generating script...")

    script = generate_script(topic)


    filename = (
        topic
        .lower()
        .replace(" ", "_")
        .replace("?", "")
        + ".txt"
    )


    script_path = "output/scripts/" + filename


    with open(script_path, "w", encoding="utf-8") as file:
        file.write(script)


    log(f"Script saved: {script_path}")


    log("Creating voice...")

    create_voice(script)


    log("Creating thumbnail...")

    create_thumbnail(topic)


    log("Video pipeline finished")



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


    pipeline()



if __name__ == "__main__":
    main()
