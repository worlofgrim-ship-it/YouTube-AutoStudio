import os
import subprocess
import shutil


BLENDER_PATH = r"C:\Users\sebastiancr\Downloads\blender-5.2.2-windows-x64\blender-5.2.2-windows-x64\blender.exe"


FRAME_FOLDER = r"C:\output\videos"


OUTPUT_VIDEO = r"output/videos/autostudio_short.mp4"



def encode_video():

    print("Encoding frames into MP4...")


    command = [

        "ffmpeg",

        "-y",

        "-framerate",
        "30",

        "-i",
        FRAME_FOLDER + r"\frame.mp4%04d.png",

        "-c:v",
        "libx264",

        "-pix_fmt",
        "yuv420p",

        OUTPUT_VIDEO
    ]


    subprocess.run(
        command,
        check=True
    )


    print(
        "MP4 created:"
    )

    print(
        OUTPUT_VIDEO
    )



def cleanup_frames():

    print(
        "Cleaning temporary frames..."
    )


    for file in os.listdir(FRAME_FOLDER):

        if file.endswith(".png"):

            os.remove(
                os.path.join(
                    FRAME_FOLDER,
                    file
                )
            )


    print(
        "Frame cleanup complete"
    )



def render_scene():

    print(
        "Starting v1.6.6 video pipeline..."
    )


    os.makedirs(
        "output/videos",
        exist_ok=True
    )


    blend_file = (
        "output/scenes/autostudio_scene.blend"
    )


    if not os.path.exists(blend_file):

        print(
            "Blend file missing"
        )

        return



    print(
        "Rendering frames already complete."
    )


    encode_video()


    cleanup_frames()


    print(
        "YouTube Short ready!"
    )
