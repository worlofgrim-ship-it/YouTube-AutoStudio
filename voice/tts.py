import edge_tts
import asyncio
import os


OUTPUT = "output/audio/narration.mp3"


VOICE = "en-US-GuyNeural"



async def generate_voice(text):

    os.makedirs(
        "output/audio",
        exist_ok=True
    )


    communicate = edge_tts.Communicate(
        text,
        VOICE
    )


    await communicate.save(
        OUTPUT
    )


    print(
        "Voice created:",
        OUTPUT
    )



def create_voice(script):

    if isinstance(script, dict):

        text = script.get(
            "narration",
            ""
        )

    else:

        text = script


    asyncio.run(
        generate_voice(text)
    )
