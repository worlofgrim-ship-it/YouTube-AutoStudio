import os


def render_scene():

    print(
        "Checking Blender engine..."
    )


    blender_file = (
        "video/blender_engine.py"
    )


    if os.path.exists(blender_file):

        print(
            "Blender scene generator found"
        )

        print(
            "Scene ready for rendering"
        )


    else:

        print(
            "Blender engine not found"
        )
