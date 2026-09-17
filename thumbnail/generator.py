import os



def create_thumbnail(text):

    os.makedirs(
        "output/thumbnails",
        exist_ok=True
    )


    filename = (
        text
        .replace(" ","_")
        [:80]
    )


    path = (
        "output/thumbnails/"
        + filename
        + ".txt"
    )


    with open(
        path,
        "w",
        encoding="utf8"
    ) as file:

        file.write(
            """
YouTube Thumbnail Plan

Main Subject:
{}


Style:
- Cinematic
- High contrast
- Big text
- Viral YouTube style

""".format(text)
        )


    print(
        "Thumbnail created:",
        path
    )
