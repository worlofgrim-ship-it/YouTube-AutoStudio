import random
import os
import json



def generate_titles(topic):

    templates = [

        f"What If {topic}? The Result Is Insane",

        f"Scientists Asked: {topic}",

        f"This Would Happen If {topic}",

        f"The Truth About {topic}"

    ]


    titles = random.sample(
        templates,
        3
    )


    data = {

        "titles": titles,

        "chosen": titles[0],

        "description":
        f"Exploring the science behind {topic}.",

        "tags":
        [
            "science",
            "space",
            "facts",
            "what if"
        ]

    }


    os.makedirs(
        "output/titles",
        exist_ok=True
    )


    with open(
        "output/titles/title.json",
        "w",
        encoding="utf8"
    ) as f:

        json.dump(
            data,
            f,
            indent=4
        )


    return data
