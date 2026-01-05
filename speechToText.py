
import speech_recognition as sr
import pyttsx3


# Function to convert text to speech
def speak(text):
    engine = pyttsx3.init()  # Initialize the TTS engine
    engine.say(text)         # Queue the text to be spoken
    engine.runAndWait()      # Process the queued commands


# Function to capture speech and convert it to text
def speech_to_text():
    recognizer = sr.Recognizer()       # Initialize the recognizer

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.2)     # Adjust for ambient noise
        print("Listening...")
        audio = recognizer.listen(source)             # Capture the audio

    try:
        text = recognizer.recognize_google(audio).lower()            # Convert speech to text using Google API
        print("You said:", text)
        speak(text)

    except sr.UnknownValueError:
        print("Sorry, could not understand the audio")

    except sr.RequestError as e:
        print(f"API error: {e}")


if __name__ == "__main__":
    while True:
        speech_to_text()

# speech recognition and text-to-speech conversion
import speech_recognition as sr
import pyttsx3


# Function to convert text to speech
def speak(text):
    engine = pyttsx3.init()  # Initialize the TTS engine
    engine.say(text)         # Queue the text to be spoken
    engine.runAndWait()      # Process the queued commands


# Function to capture speech and convert it to text
def speech_to_text():
    recognizer = sr.Recognizer()       # Initialize the recognizer

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.2)     # Adjust for ambient noise
        print("Listening...")
        audio = recognizer.listen(source)             # Capture the audio

    try:
        text = recognizer.recognize_google(audio).lower()            # Convert speech to text using Google API
        print("You said:", text)
        speak(text)

    except sr.UnknownValueError:
        print("Sorry, could not understand the audio")

    except sr.RequestError as e:
        print(f"API error: {e}")


if __name__ == "__main__":
    while True:
        speech_to_text()
