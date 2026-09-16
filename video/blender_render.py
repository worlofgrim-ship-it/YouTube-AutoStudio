import os
import subprocess


BLENDER_PATH = r"C:\Users\sebastiancr\Downloads\blender-5.2.2-windows-x64\blender-5.2.2-windows-x64\blender.exe"



def run_blender_script(script):

    subprocess.run(
        [
            BLENDER_PATH,
            "--background",
            "--python",
            script
        ],
        check=True
    )



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



    scene_script = (
        "video/blender_engine.py"
    )


    print(
        "Generating scene..."
    )


    run_blender_script(
        scene_script
    )


    blend_file = (
        os.path.abspath(
            "output/scenes/autostudio_scene.blend"
        )
    )


    if not os.path.exists(blend_file):

        print(
            "Blend file missing"
        )

        return



    print(
        "Rendering animation..."
    )


    render_script = """
import bpy

bpy.ops.wm.open_mainfile(
    filepath=r'""" + blend_file + """'
)

bpy.context.scene.render.filepath = r'output/videos/autostudio_short.mp4'

bpy.ops.render.render(
    animation=True
)
"""


    temp_script = (
        "video/render_animation.py"
    )


    with open(
        temp_script,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(
            render_script
        )


    run_blender_script(
        temp_script
    )


    print(
        "Video render complete"
    )
