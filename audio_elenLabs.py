import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_ELevenLabs = os.environ.get("API_KEY_ELEVENLABS")

from elevenlabs import save
from elevenlabs.client import ElevenLabs

client = ElevenLabs(
    api_key=API_ELevenLabs,  # Defaults to ELEVEN_API_KEY
)

audio = client.generate(
    text="Hola amigo Juan Pérez",
    voice="Adam",
    model="eleven_multilingual_v2",
)
save(audio, "my-file.mp3")
