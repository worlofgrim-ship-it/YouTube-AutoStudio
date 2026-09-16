import subprocess
import os


def render_scene():

    script = (
        "video/blender_engine.py"
    )


    if os.path.exists(script):

        print(
            "Blender script detected"
        )


        # Blender will be connected here
        # in the next step

        print(
            "Scene generation ready"
        )


    else:

        print(
            "Missing Blender engine"
        )
