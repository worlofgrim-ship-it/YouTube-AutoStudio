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

        default = {
            "channel_name": "My AI Channel",
            "upload_frequency": "daily",
            "video_type": "shorts",
            "style": "3D animated documentary"
        }

        with open(path, "w") as file:
            json.dump(default, file, indent=4)

        log("Created default settings")

        return default


    with open(path, "r") as file:
        settings = json.load(file)

    log("Settings loaded")

    return settings


def pipeline():

    log("Starting YouTube-AutoStudio")

    stages = [
        "Finding video idea",
        "Generating script",
        "Creating voice",
        "Building scenes",
        "Rendering video",
        "Generating thumbnail",
        "Uploading video",
        "Updating analytics"
    ]


    for stage in stages:
        log(f"[WAITING] {stage}")

    log("Pipeline complete")


def main():

    print("=" * 40)
    print(PROJECT_NAME)
    print("=" * 40)

    create_folders()

    settings = load_settings()

    log(
        f"Channel: {settings['channel_name']}"
    )

    pipeline()


if __name__ == "__main__":
    main()
