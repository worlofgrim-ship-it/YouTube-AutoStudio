import os
import json

print("="*40)
print("YouTube-AutoStudio v1.7 Setup")
print("="*40)


settings = {
    "channel_name": input("Channel name: "),
    "blender_path": input("Blender path: "),
    "ffmpeg_path": input("FFmpeg path: "),
    "youtube_upload": False
}


os.makedirs(
    "config",
    exist_ok=True
)


with open(
    "config/settings.json",
    "w"
) as f:
    json.dump(
        settings,
        f,
        indent=4
    )


print()
print("Setup complete!")
print("Run: python main.py")
