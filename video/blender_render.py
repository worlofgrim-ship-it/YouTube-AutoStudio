import os
import subprocess
import shutil


SCENE_FILE = "output/scenes/autostudio_scene.blend"

FRAME_FOLDER = r"C:\output\videos"

OUTPUT_VIDEO = "output/videos/autostudio_short.mp4"



# ---------------------------------
# Logging
# ---------------------------------

def log(text):

    print(text)



# ---------------------------------
# Find programs
# ---------------------------------

def find_blender(settings):

    path = settings.get(
        "blender_path",
        ""
    )


    if path and os.path.exists(path):

        return path


    found = shutil.which(
        "blender"
    )


    if found:

        return found


    return None




def find_ffmpeg(settings):

    path = settings.get(
        "ffmpeg_path",
        ""
    )


    if path and os.path.exists(path):

        return path


    found = shutil.which(
        "ffmpeg"
    )


    if found:

        return found


    return None



# ---------------------------------
# Blender Scene Creation
# ---------------------------------

def create_scene(blender):


    log(
        "Generating Blender scene..."
    )


    script = "blender/create_scene.py"


    if not os.path.exists(script):

        log(
            "Scene generator missing"
        )

        return False



    subprocess.run(

        [

            blender,

            "--background",

            "--python",

            script

        ],

        check=True

    )


    log(
        "Scene created"
    )


    return True



# ---------------------------------
# Render Frames
# ---------------------------------

def render_frames(blender):


    log(
        "Rendering frames..."
    )


    os.makedirs(
        FRAME_FOLDER,
        exist_ok=True
    )



    subprocess.run(

        [

            blender,

            "--background",

            SCENE_FILE,

            "--render-output",

            FRAME_FOLDER + r"\frame.mp4",

            "--animation"

        ],

        check=True

    )


    log(
        "Frames complete"
    )



# ---------------------------------
# Encode MP4
# ---------------------------------

def encode_video(ffmpeg):


    log(
        "Encoding MP4..."
    )


    os.makedirs(

        "output/videos",

        exist_ok=True

    )


    subprocess.run(

        [

            ffmpeg,

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


    log(
        "MP4 created"
    )



# ---------------------------------
# Main Render Function
# ---------------------------------

def render_scene(settings={}):


    blender = find_blender(
        settings
    )


    ffmpeg = find_ffmpeg(
        settings
    )



    if not blender:

        raise Exception(
            "Blender not found"
        )


    if not ffmpeg:

        raise Exception(
            "FFmpeg not found"
        )



    log(
        "Starting Blender pipeline..."
    )



    if not os.path.exists(
        SCENE_FILE
    ):

        create_scene(
            blender
        )



    render_frames(
        blender
    )



    encode_video(
        ffmpeg
    )


    log(
        "YouTube Short finished!"
    )
