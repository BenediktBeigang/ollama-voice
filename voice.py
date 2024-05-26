from elevenlabs import play
from elevenlabs.client import ElevenLabs
import json

with open("credentials.json") as f:
  credentials = json.load(f)
  api_key = credentials["elevenlabs_api_key"]
  client = ElevenLabs(
    api_key=api_key,
  )
  
response = client.voices.get_all()
audio = client.generate(text="Hello there!", voice=response.voices[0])
print(response.voices)

audio = client.generate(
  text="Hello I'm Marvin, a disillusioned robot not be able to eat at the restaurant at the end of the universe, because my creator build me without a dijestive-system!",
  voice="Marvin",
  model="eleven_multilingual_v2"
)
play(audio)