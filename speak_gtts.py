from gtts import gTTS
from logger import logging
import sounddevice as sd
import soundfile as sf
import asyncio
from utils import timing

@timing
async def speak(text, speed=1):
    await voice2text(text)
    await play_sound_sounddevice(speed=speed)




async def play_sound_sounddevice(file="temp.mp3", speed=1.5):
    try:
        # Load the audio file
        data, sample_rate = sf.read(file)
        logging.info("Read sound file")
        # Adjust playback speed (e.g., 1.5x faster)
        new_sample_rate = int(sample_rate * speed)

        # Play the adjusted audio
        logging.info(f"Played sound {sd.play(data, samplerate=new_sample_rate)}")
        await sd.wait()
    except Exception as e:
        logging.error(e)


async def voice2text(text):
    try:
        tts = gTTS(text=text, lang='en')
        if tts is not None:
            await tts.save("temp.mp3")
            logging.info("Saved text to voice in file temp.mp3")
    except Exception as e:
        logging.error(e)

if __name__ == '__main__':
    asyncio.run(speak("This is a test of the sound system", speed=3))