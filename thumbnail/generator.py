import os
import re


def create_thumbnail(topic):

    os.makedirs(
        "output/thumbnails",
        exist_ok=True
    )

    # Remove characters Windows does not allow in filenames
    safe_name = re.sub(
        r'[<>:"/\\|?*]',
        '',
        topic
    )

    safe_name = safe_name.replace(" ", "_")


    file = (
        "output/thumbnails/"
        + safe_name
        + ".txt"
    )


    with open(file, "w", encoding="utf-8") as f:

        f.write(
            "Thumbnail idea:\n\n"
            + topic
        )


    print(
        "Thumbnail created:",
        file
    )
