import os
import shutil


def find_blender():

    locations = [

        shutil.which("blender"),

        r"C:\Program Files\Blender Foundation\Blender\blender.exe",

        r"C:\Program Files\Blender Foundation\Blender 5.2\blender.exe"

    ]


    for path in locations:

        if path and os.path.exists(path):

            return path


    return ""



def find_ffmpeg():

    locations = [

        shutil.which("ffmpeg"),

        r"C:\ffmpeg\bin\ffmpeg.exe",

        r"C:\Users\Public\ffmpeg\bin\ffmpeg.exe"

    ]


    for path in locations:

        if path and os.path.exists(path):

            return path


    return ""



def check_system(settings):


    print()

    print("System Check")

    print("----------------")


    blender = find_blender()

    ffmpeg = find_ffmpeg()


    if blender:

        print("✓ Blender")

        settings["blender_path"] = blender

    else:

        print("✗ Blender missing")



    if ffmpeg:

        print("✓ FFmpeg")

        settings["ffmpeg_path"] = ffmpeg

    else:

        print("✗ FFmpeg missing")



    print("✓ Python")

    print("✓ Files")


    print()


    return settings
