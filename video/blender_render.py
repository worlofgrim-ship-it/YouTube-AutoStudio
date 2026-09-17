import os
import subprocess


BLENDER_PATH = r"C:\Users\sebastiancr\Downloads\blender-5.2.2-windows-x64\blender-5.2.2-windows-x64\blender.exe"

FFMPEG_PATH = r"C:\Users\sebastiancr\Downloads\ffmpeg-9.0.1\ffmpeg-9.0.1\bin\ffmpeg.exe"


FRAME_FOLDER = r"C:\output\videos"

OUTPUT_VIDEO = r"output/videos/autostudio_short.mp4"



def run_blender(script):

    subprocess.run(
        [
            BLENDER_PATH,
            "--background",
            "--python",
            script
        ],
        check=True
    )



def create_scene():

    print(
        "Generating Blender scene..."
    )

    run_blender(
        "video/blender_engine.py"
    )



def render_frames():

    print(
        "Rendering frames..."
    )


    blend_file = os.path.abspath(
        "output/scenes/autostudio_scene.blend"
    )


    render_script = f"""

import bpy

bpy.ops.wm.open_mainfile(
filepath=r'{blend_file}'
)

bpy.context.scene.render.filepath=r'C:/output/videos/frame.mp4'

bpy.ops.render.render(
animation=True
)

"""


    with open(
        "video/render_animation.py",
        "w"
    ) as f:

        f.write(render_script)



    run_blender(
        "video/render_animation.py"
    )



def encode_video():

    print(
        "Encoding MP4..."
    )


    subprocess.run(
        [

            FFMPEG_PATH,

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

        ],
        check=True
    )



    print(
        "MP4 created"
    )



def cleanup():

    print(
        "Cleaning frames..."
    )


    for file in os.listdir(FRAME_FOLDER):

        if file.endswith(".png"):

            os.remove(
                os.path.join(
                    FRAME_FOLDER,
                    file
                )
            )



def render_scene():

    print(
        "Starting v1.6.6.1 full pipeline..."
    )


    create_scene()

    render_frames()

    encode_video()

    cleanup()


    print(
        "YouTube Short finished!"
    )
