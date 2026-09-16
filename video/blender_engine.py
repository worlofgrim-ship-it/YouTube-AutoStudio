import bpy
import math



def clear_scene():

    bpy.ops.object.select_all(
        action="SELECT"
    )

    bpy.ops.object.delete()



def create_planet():

    bpy.ops.mesh.primitive_uv_sphere_add(
        segments=64,
        ring_count=32,
        location=(0,0,0)
    )


    planet = bpy.context.object

    planet.name = "Planet"



    material = bpy.data.materials.new(
        "Planet Material"
    )


    material.diffuse_color = (
        0.1,
        0.5,
        1,
        1
    )


    planet.data.materials.append(
        material
    )



def create_camera():

    bpy.ops.object.camera_add(
        location=(10,-10,5)
    )


    camera = bpy.context.object

    camera.name = "Main Camera"


    bpy.context.scene.camera = camera



def create_light():

    bpy.ops.object.light_add(
        type="SUN",
        location=(5,5,5)
    )


    light = bpy.context.object

    light.name = "Sun"



def animate_camera():

    camera = bpy.context.scene.camera


    bpy.context.scene.frame_start = 1

    bpy.context.scene.frame_end = 120


    camera.location = (
        10,
        -10,
        5
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



def generate_scene():

    print(
        "Generating 3D scene"
    )


    clear_scene()

    create_planet()

    create_camera()

    create_light()

    animate_camera()


    print(
        "3D scene complete"
    )



if __name__ == "__main__":

    generate_scene()
