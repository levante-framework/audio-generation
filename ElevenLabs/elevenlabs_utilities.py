import os
from elevenlabs import play
from elevenlabs.client import ElevenLabs 
import pprint 

client = ElevenLabs( 
    api_key=os.getenv('elevenlabs_test'),  # enter your API key here 
) 

def list_voices(lang_code):

    # ElevenLabs doesn't have es-CO
    if lang_code == 'es-CO':
        modified_language_code = 'es'
    else:
        modified_language_code = lang_code

    response = client.voices.get_shared(
        page_size=100,  # Adjust as needed, max 100
        category='professional',  # Optional filter
        gender='Female',    # Optional filter
        age=None,       # Optional filter
        accent=None,    # Optional filter
        language=modified_language_code, 
        search=None,    # Optional search term
        use_cases='conversational',  # Optional filter
        featured=None,  # Optional filter
        sort=None,       # Optional sorting criteria
        #model="eleven_multilingual_v2",
    )
    voice_list = response.voices

    # Create a dictionary with voice names as keys and voice IDs as values
    voice_dict = {voice.name: voice.voice_id for voice in voice_list}
    return voice_dict

def play_audio(text): #, voice):
    # Generate audio from text
    # The tricky part is that we need the voice_id, not the voice name!
    # we could build a dictionary?
    audio = client.generate(text=text, voice='v3V1d2rk6528UrLKRuy8') # voice=voice)
    #audio = client.generate(text=text, voice='Susi') # voice=voice)

    # Play the generated audio
    play(audio)

voice_dict = list_voices('de')
play_audio("Ouch")

#with open("voices.txt", "w", encoding="utf-8") as file: 
#    file.write(formatted_voices) 
#print("Voice information has been written to voices.txt") 
#print(f"Number of voices: {len(response.voices)}") 