from gtts import gTTS
from playsound import playsound
import os
import openai
import speech_recognition as sr

# initialize the recognizer
r = sr.Recognizer()

# use the microphone as source for input
with sr.Microphone() as source:
    # adjust for ambient noise
    r.adjust_for_ambient_noise(source)
    print("Speak now...")
    # listen for any duration of speech and convert to text
    audio = r.listen(source)

try:
    # recognize speech using Google Speech Recognition API
    input_audio = r.recognize_google(audio)
    # print("You said: ", text)

except sr.UnknownValueError:
    print("Oops! Unable to recognize speech...")
except sr.RequestError as e:
    print("Uh oh! Could not request results from Google Speech Recognition service; {0}".format(e))

# Load your API key from an environment variable or secret management service
openai.api_key = "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"
prompt = input_audio
completion = openai.Completion.create(model="text-davinci-003", prompt=prompt, temperature=0, max_tokens=4000)
response = completion.choices[0].text
print(response)

# Get the text to be spoken
text = response

# Set the language to English with American accent
language = 'en-us'

# Create a gTTS object and generate the speech
speech = gTTS(text=text, lang=language, slow=False)

# Save the speech as an MP3 file
speech.save("speech.mp3")

# Play the speech using the playsound library
playsound("speech.mp3")

# Delete the MP3 file
os.remove("speech.mp3")
