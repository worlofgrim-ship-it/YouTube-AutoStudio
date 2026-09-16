import os
import shutil
import subprocess


def find_blender():

    possible_paths = [

        "blender",

        r"C:\Program Files\Blender Foundation\Blender 4.5\blender.exe",

        r"C:\Program Files\Blender Foundation\Blender 4.4\blender.exe",

        r"C:\Program Files\Blender Foundation\Blender 4.3\blender.exe"

    ]


    for path in possible_paths:

        if shutil.which(path) or os.path.exists(path):

            return path


    return None



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


    blender = find_blender()



    if blender is None:

        print(
            "Blender not installed."
        )

        print(
            "Scene generator prepared but render skipped."
        )

        return



    script = (
        "video/blender_engine.py"
    )


    blend_file = (
        "output/scenes/autostudio_scene.blend"
    )



    print(
        "Blender found:"
        ,
        blender
    )



    print(
        "Generating Blender project..."
    )



    command = [

        blender,

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
            "Blender scene generated"
        )



    except Exception as error:

        print(
            "Blender error:",
            error
        )



    print(
        "Render pipeline finished"
    )
