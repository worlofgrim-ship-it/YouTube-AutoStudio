import shutil


def check_program(name):

    result = shutil.which(name)

    if result:
        print(name,"OK")
        return True

    print(name,"missing")
    return False



def check():

    check_program("python")
    check_program("ffmpeg")
