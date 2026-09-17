import os


def create_voice(script):

    os.makedirs(
        "output/voice",
        exist_ok=True
    )

    output = "output/voice/script.txt"


    # Handle AI script dictionary
    if isinstance(script, dict):

        if "script" in script:
            text = script["script"]

        elif "content" in script:
            text = script["content"]

        else:
            text = str(script)

    else:
        text = script


    with open(
        output,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(text)


    print("Voice script saved")

    return output
