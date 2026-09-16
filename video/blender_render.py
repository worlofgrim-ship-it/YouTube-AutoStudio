import os
import subprocess


BLENDER_PATH = r"C:\Users\sebastiancr\Downloads\blender-5.2.2-windows-x64\blender-5.2.2-windows-x64\blender.exe"



def render_scene():

    print(
        "Starting Blender render pipeline..."
    )


    os.makedirs(
        "output/videos",
        exist_ok=True
    )


    if not os.path.exists(BLENDER_PATH):

        print(
            "Blender not found"
        )

        return



    script = (
        "video/blender_engine.py"
    )


    print(
        "Generating scene..."
    )


    subprocess.run(
        [
            BLENDER_PATH,
            "--background",
            "--python",
            script
        ]
    )


    blend_file = (
        "output/scenes/autostudio_scene.blend"
    )


    print(
        "Rendering MP4..."
    )


    subprocess.run(
        [
            BLENDER_PATH,
            "--background",
            blend_file,
            "--render-animation"
        ]
    )


    print(
        "Video render complete"
    )
