import os
import json


print("=" * 40)
print("YouTube-AutoStudio v1.7 Setup")
print("=" * 40)


settings = {}


settings["channel_name"] = input(
    "Channel name: "
)


settings["blender_path"] = input(
    "Path to Blender.exe: "
)


settings["ffmpeg_path"] = input(
    "Path to ffmpeg.exe: "
)


settings["youtube_upload"] = False


settings["video_type"] = "youtube_shorts"


settings["style"] = (
    "3D animated science documentary"
)


settings["target_length_seconds"] = 45


settings["fps"] = 30


settings["resolution_x"] = 1080


settings["resolution_y"] = 1920



os.makedirs(
    "config",
    exist_ok=True
)


with open(
    "config/settings.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        settings,
        f,
        indent=4
    )


print()
print("Setup finished!")
print("Run:")
print("python main.py")
