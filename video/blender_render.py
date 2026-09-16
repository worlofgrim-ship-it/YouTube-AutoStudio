import os
import subprocess


BLENDER_PATH = r"C:\Users\sebastiancr\Downloads\blender-5.2.2-windows-x64\blender-5.2.2-windows-x64\blender.exe"



def render_scene():

    print(
        "FAST Blender render mode"
    )


    os.makedirs(
        "output/videos",
        exist_ok=True
    )


    subprocess.run(
        [
            BLENDER_PATH,
            "--background",
            "--python",
            "video/blender_engine.py"
        ]
    )


    blend_file = os.path.abspath(
        "output/scenes/autostudio_scene.blend"
    )


    render_script = f"""

import bpy

bpy.ops.wm.open_mainfile(
filepath=r'{blend_file}'
)

scene=bpy.context.scene

scene.render.resolution_percentage=50

scene.render.filepath=r'output/videos/frame.mp4'

bpy.ops.render.render(
animation=True
)

"""


    with open(
        "video/fast_render.py",
        "w"
    ) as f:

        f.write(
            render_script
        )


    subprocess.run(
        [
            BLENDER_PATH,
            "--background",
            "--python",
            "video/fast_render.py"
        ]
    )


    print(
        "FAST render complete"
    )
