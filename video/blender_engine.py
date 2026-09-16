import bpy
import math
import os



def clear_scene():

    bpy.ops.object.select_all(
        action="SELECT"
    )

    bpy.ops.object.delete()



def create_world():

    world = bpy.context.scene.world


    world.color = (
        0,
        0,
        0
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

        location=(8,-8,4)

    )


    camera = bpy.context.object


    camera.name = (
        "AutoStudio Camera"
    )


    bpy.context.scene.camera = camera



def create_light():

    bpy.ops.object.light_add(

        type="SUN",

        location=(5,5,5)

    )


    light = bpy.context.object


    light.name = "Sun"



def animate():

    camera = bpy.context.scene.camera


    bpy.context.scene.frame_start = 1

    bpy.context.scene.frame_end = 120



    camera.location = (

        8,

        -8,

        4

    )


    camera.keyframe_insert(

        "location",

        frame=1

    )



    camera.location = (

        3,

        -3,

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
        "Creating 3D scene..."
    )


    clear_scene()

    create_world()

    create_planet()

    create_camera()

    create_light()

    animate()

    save_project()



    print(
        "Saved Blender project"
    )



if __name__ == "__main__":

    generate_scene()
