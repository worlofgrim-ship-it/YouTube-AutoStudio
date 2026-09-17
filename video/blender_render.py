import os
import subprocess
import json



def load_settings():

    with open(
        "config/settings.json",
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)



def render_scene(settings=None):


    if settings is None:

        settings = load_settings()



    blender = settings[
        "blender_path"
    ]


    scene = (
        "output/scenes/"
        "autostudio_scene.blend"
    )


    if not os.path.exists(scene):

        raise Exception(
            "Blend file missing"
        )


    command = [

        blender,

        "--background",

        scene,

        "--render-animation"

    ]


    print(
        "Starting Blender render..."
    )


    subprocess.run(
        command,
        check=True
    )


    print(
        "Render finished"
    )
