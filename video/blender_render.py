import os
import subprocess


BLENDER_PATH = r"C:\Users\sebastiancr\Downloads\blender-5.2.2-windows-x64\blender-5.2.2-windows-x64\blender.exe"



def render_scene():

    print(
        "Starting Blender render pipeline..."
    )


    os.makedirs(
        "output/scenes",
        exist_ok=True
    )

    os.makedirs(
        "output/videos",
        exist_ok=True
    )


    if not os.path.exists(BLENDER_PATH):

        print(
            "Portable Blender not found:"
        )

        print(
            BLENDER_PATH
        )

        print(
            "Scene generation skipped."
        )

        return



    print(
        "Blender found:"
    )

    print(
        BLENDER_PATH
    )


    script = (
        "video/blender_engine.py"
    )


    if not os.path.exists(script):

        print(
            "Blender engine script missing"
        )

        return



    print(
        "Running Blender scene generator..."
    )


    command = [

        BLENDER_PATH,

        "--background",

        "--python",

        script

    ]


    try:

        subprocess.run(
            command,
            check=True
        )


        print(
            "Blender scene generated successfully"
        )


    except Exception as error:

        print(
            "Blender error:"
        )

        print(error)



    print(
        "Blender pipeline finished"
    )
