import bpy
import os


def clear_scene():

    bpy.ops.object.select_all(
        action="SELECT"
    )

    bpy.ops.object.delete()



def setup_render():

    scene = bpy.context.scene

    scene.render.engine = "BLENDER_EEVEE_NEXT"

    scene.render.resolution_x = 1080
    scene.render.resolution_y = 1920

    scene.render.resolution_percentage = 50

    scene.render.fps = 30

    scene.render.image_settings.file_format = "FFMPEG"

    scene.render.ffmpeg.format = "MPEG4"

    scene.render.filepath = (
        "output/videos/autostudio_short.mp4"
    )



def create_planet():

    bpy.ops.mesh.primitive_uv_sphere_add(
        segments=64,
        ring_count=32,
        location=(0,0,0)
    )


    planet = bpy.context.object

    planet.name = "AutoStudio Planet"


    material = bpy.data.materials.new(
        "Planet Material"
    )


    material.diffuse_color = (
        0.05,
        0.3,
        1,
        1
    )


    planet.data.materials.append(
        material
    )



def create_camera():

    bpy.ops.object.camera_add(
        location=(0,-12,3)
    )


    camera = bpy.context.object

    camera.name = "AutoStudio Camera"


    bpy.context.scene.camera = camera


    camera.rotation_euler = (
        1.45,
        0,
        0
    )



def create_light():

    bpy.ops.object.light_add(
        type="SUN",
        location=(5,5,5)
    )


    light = bpy.context.object

    light.name = "Sun"



def animate_camera():

    camera = bpy.context.scene.camera


    camera.location = (
        0,
        -12,
        3
    )


    camera.keyframe_insert(
        "location",
        frame=1
    )


    camera.location = (
        0,
        -5,
        2
    )


    camera.keyframe_insert(
        "location",
        frame=120
    )



def save_project():

    os.makedirs(
        "output/scenes",
        exist_ok=True
    )


    bpy.ops.wm.save_as_mainfile(
        filepath=
        "output/scenes/autostudio_scene.blend"
    )



def generate_scene():

    print(
        "Creating Shorts scene..."
    )


    clear_scene()

    setup_render()

    create_planet()

    create_camera()

    create_light()

    animate_camera()

    save_project()


    print(
        "Shorts scene created"
    )



if __name__ == "__main__":

    generate_scene()
