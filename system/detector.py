import os


def check_file(path,name):

    if path and os.path.exists(path):

        print(
            "✓",
            name,
            "found"
        )

        return True


    print(
        "✗",
        name,
        "missing"
    )

    return False



def check_system(settings):


    print()

    print("Checking system...")

    print("-----------------")


    check_file(
        settings.get("blender_path"),
        "Blender"
    )


    check_file(
        settings.get("ffmpeg_path"),
        "FFmpeg"
    )


    print(
        "✓ Python"
    )


    print(
        "✓ Project files"
    )


    print()
