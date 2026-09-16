import os


def create_thumbnail(topic):

    os.makedirs(
        "output/thumbnails",
        exist_ok=True
    )


    file = (
        "output/thumbnails/"
        + topic.replace(" ", "_")
        + ".txt"
    )


    with open(file, "w") as f:

        f.write(
            "Thumbnail idea:\n"
            + topic
        )


    print(
        "Thumbnail plan created"
    )
