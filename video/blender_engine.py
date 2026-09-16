import bpy


def clear_scene():

    bpy.ops.object.select_all(
        action="SELECT"
    )

    bpy.ops.object.delete()



def create_black_hole():

    bpy.ops.mesh.primitive_uv_sphere_add(
        segments=128,
        ring_count=64,
        location=(0, 0, 0)
    )

    black_hole = bpy.context.object

    black_hole.name = "Black Hole"

    black_hole.scale = (
        3,
        3,
        3
    )


    material = bpy.data.materials.new(
        "Black Hole Material"
    )

    material.diffuse_color = (
        0,
        0,
        0,
        1
    )

    black_hole.data.materials.append(
        material
    )



def create_earth():

    bpy.ops.mesh.primitive_uv_sphere_add(
        segments=64,
        ring_count=32,
        location=(8, 0, 0)
    )

    earth = bpy.context.object

    earth.name = "Earth"


    material = bpy.data.materials.new(
        "Earth Material"
    )

    material.diffuse_color = (
        0.05,
        0.3,
        1,
        1
    )

    earth.data.materials.append(
        material
    )



def create_camera():

    bpy.ops.object.camera_add(
        location=(15, -15, 8)
    )

    camera = bpy.context.object

    camera.name = "Cinematic Camera"

    bpy.context.scene.camera = camera



def create_light():

    bpy.ops.object.light_add(
        type="POINT",
        location=(5, -5, 10)
    )

    light = bpy.context.object

    light.name = "Space Light"

    light.data.energy = 2000



def animate_camera():

    camera = bpy.context.scene.camera


    bpy.context.scene.frame_start = 1

    bpy.context.scene.frame_end = 240


    camera.location = (
        15,
        -15,
        8
    )

    camera.keyframe_insert(
        "location",
        frame=1
    )


    camera.location = (
        5,
        -5,
        3
    )

    camera.keyframe_insert(
        "location",
        frame=240
    )



def generate_scene():

    print(
        "Generating Blender scene..."
    )

    clear_scene()

    create_black_hole()

    create_earth()

    create_camera()

    create_light()

    animate_camera()


    print(
        "Blender scene generated successfully"
    )



if __name__ == "__main__":

    generate_scene()
