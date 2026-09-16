import json
import os


def generate_script(topic):

    data = {

        "title": topic,

        "hook":
        f"Imagine waking up tomorrow and discovering that {topic.lower()}",


        "description":
        "A fast-paced documentary style video explaining a mysterious possibility.",


        "scenes": [

            {
                "time": "0-5 seconds",
                "visual": "A dramatic cinematic opening shot showing the topic.",
                "voice":
                f"Imagine if {topic.lower()}."
            },

            {
                "time": "5-20 seconds",
                "visual":
                "A 3D animated explanation with realistic environments.",
                "voice":
                "Scientists have studied this possibility and discovered fascinating results."
            },

            {
                "time": "20-40 seconds",
                "visual":
                "Show the effects happening around the world.",
                "voice":
                "The consequences would change everything we know."
            },

            {
                "time": "40-60 seconds",
                "visual":
                "End with a cinematic space shot.",
                "voice":
                "The universe still holds countless mysteries."
            }

        ],


        "thumbnail":
        f"Epic cinematic thumbnail showing {topic}",


        "tags":
        [
            "science",
            "space",
            "facts",
            "documentary",
            "shorts"
        ]

    }


    os.makedirs(
        "output/scripts",
        exist_ok=True
    )


    filename = (
        topic
        .lower()
        .replace(" ", "_")
        .replace("?", "")
        + ".json"
    )


    path = (
        "output/scripts/"
        + filename
    )


    with open(
        path,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            data,
            file,
            indent=4
        )


    return data
