import os


def setup_project():

    folders = [

        "output",

        "output/videos",

        "output/audio",

        "output/scripts",

        "output/thumbnails",

        "output/scenes",

        "logs",

        "config",

        "youtube"

    ]


    for folder in folders:

        os.makedirs(
            folder,
            exist_ok=True
        )


    print(
        "Folder structure verified"
    )
