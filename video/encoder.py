import subprocess
import json



def encode_video():

    with open(
        "config/settings.json"
    ) as f:

        settings=json.load(f)



    ffmpeg=settings[
        "ffmpeg_path"
    ]


    command=[

        ffmpeg,

        "-framerate",
        "30",

        "-i",

        "C:/output/videos/frame.mp4%04d.png",

        "-c:v",

        "libx264",

        "-pix_fmt",

        "yuv420p",

        "output/videos/autostudio_short.mp4"

    ]


    subprocess.run(
        command,
        check=True
    )


    print(
        "MP4 created"
    )
