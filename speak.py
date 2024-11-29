
from elevenlabs import play
from elevenlabs.client import ElevenLabs, Voice, VoiceSettings
from dotenv import load_dotenv
from logger import logging
import os

load_dotenv()
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")

async def speak(text: str):
    try:
        client = ElevenLabs(
            api_key=ELEVENLABS_API_KEY
        )

        audio = client.generate(
            text=text,
            voice=Voice(
                voice_id="onwK4e9ZLuTAKqWW03F9",
                settings=VoiceSettings(
                    stability=0.5,
                    similarity_boost=0.75,
                    style=0.0,
                    use_speaker_boost=False,
                ),
            ),
            model="eleven_turbo_v2_5",
        )

        # Check if play returns a coroutine
        if audio is not None:
            await play(audio)
        else:
            logging.info("No text was recorded")

    except Exception as e:
        logging.error(f"Error in speak function: {e}")