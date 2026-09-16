import bpy
import os


def clear_scene():

    bpy.ops.object.select_all(
        action="SELECT"
    )

    bpy.ops.object.delete()



def setup_render():

    scene = bpy.context.scene


    # Fast Eevee renderer
    scene.render.engine = "BLENDER_EEVEE_NEXT" if "BLENDER_EEVEE_NEXT" in [
        item.identifier
        for item in bpy.types.RenderSettings.bl_rna.properties["engine"].enum_items
    ] else "BLENDER_EEVEE"


    # SPEED SETTINGS
    scene.render.resolution_x = 720
    scene.render.resolution_y = 1280
    scene.render.resolution_percentage = 50


    scene.render.fps = 30


    # Short length
    scene.frame_start = 1
    scene.frame_end = 150


    # Faster shadows/effects
    scene.eevee.taa_render_samples = 8 if hasattr(scene.eevee, "taa_render_samples") else 8


    scene.render.film_transparent = False



def create_planet():

    bpy.ops.mesh.primitive_uv_sphere_add(
        segments=32,
        ring_count=16,
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
        location=(0,-10,2)
    )


    camera = bpy.context.object

    bpy.context.scene.camera = camera



def create_light():

    bpy.ops.object.light_add(
        type="SUN",
        location=(5,5,5)
    )



def animate_camera():

    camera = bpy.context.scene.camera


    camera.location = (
        0,
        -10,
        2
    )


    camera.keyframe_insert(
        "location",
        frame=1
    )


    camera.location = (
        0,
        -6,
        2
    )


    camera.keyframe_insert(
        "location",
        frame=150
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
        "Creating FAST Shorts scene..."
    )


    clear_scene()

    setup_render()

    create_planet()

    create_camera()

    create_light()

    animate_camera()

    save_project()


    print(
        "Fast scene created"
    )



if __name__ == "__main__":
    generate_scene()
