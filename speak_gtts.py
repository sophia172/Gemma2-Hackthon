from gtts import gTTS
from logger import logging
import sounddevice as sd
import soundfile as sf

from utils import timing

@timing
def speak(text, speed=1):
    voice2text(text)
    play_sound_sounddevice(speed=speed)


def play_sound_sounddevice(file="temp.mp3", speed=1.5):
    try:
        # Load the audio file
        data, sample_rate = sf.read(file)
        logging.info("Read sound file")
        # Adjust playback speed (e.g., 1.5x faster)
        new_sample_rate = int(sample_rate * speed)

        # Play the adjusted audio
        sd.play(data, samplerate=new_sample_rate)
        logging.info("Played sound")
        sd.wait()
    except Exception as e:
        logging.error(e)

@timing
def voice2text(text):
    try:
        tts = gTTS(text=text, lang='en')
        tts.save("temp.mp3")
        logging.info("Saved text to voice in file temp.mp3")
    except Exception as e:
        logging.error(e)

if __name__ == '__main__':
    speak("This is a test of the sound system", speed=3)