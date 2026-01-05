import streamlit as st
import speech_recognition as sr
import pyttsx3


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def speech_to_text():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        st.info("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.3)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        return text

    except sr.UnknownValueError:
        return "Sorry, could not understand."

    except sr.RequestError as e:
        return f"API error: {e}"


# ---------------- STREAMLIT UI ---------------- #

st.set_page_config(page_title="Speech to Text", layout="centered")
st.title("🎙️ Speech to Text App")

if st.button("Start Listening"):
    result = speech_to_text()
    st.success(f"You said: {result}")
    speak(result)
