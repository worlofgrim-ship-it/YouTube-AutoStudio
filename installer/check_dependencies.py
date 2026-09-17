import shutil


def check(program):

    path = shutil.which(program)

    if path:
        print(program,"FOUND:",path)
        return True

    print(program,"MISSING")
    return False



print("Checking dependencies")

check("python")
check("ffmpeg")
check("blender")
