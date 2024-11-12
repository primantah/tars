import openai  # type: ignore
import pyttsx3  # type: ignore
import speech_recognition as sr  # type: ignore
import os

# Directly set the OpenAI API key
openai.api_key = "...."

# Initialize pyttsx3 TTS engine
engine = pyttsx3.init()
recognizer = sr.Recognizer()

# Set TTS voice properties for a robotic tone
engine.setProperty('rate', 150)  # Lower speed
engine.setProperty('volume', 0.9)  # Volume level
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Choose a deeper or more robotic voice if available

def TARS_respond(prompt):
    """
    Function to get response from OpenAI's GPT model using ChatCompletion.
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=150,
        temperature=0.7
    )
    message = response.choices[0].message['content'].strip()
    
    return message

def listen_to_user():
    """
    Function to listen to the user's voice and convert it to text.
    """
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1.5)  # Longer ambient noise adjustment
        audio = recognizer.listen(source)
        
        try:
            print("Recognizing...")
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            # Correct misinterpreted words
            if "car" in text.lower():
                text = text.replace("car", "TARS")
            return text
        except sr.UnknownValueError:
            print("Sorry, I didn't understand that.")
            return None
        except sr.RequestError:
            print("Sorry, I'm having trouble accessing the speech recognition service.")
            return None

# Chat loop
print("Hello! I'm TARS. How can I assist you today?")
while True:
    print("Say something or type 'exit' to end the session.")
    user_input = listen_to_user()  # Listen to voice input

    # Allow typing 'exit' to quit as an alternative
    if user_input is None:
        continue  # If voice wasn't recognized, continue to listen

    if user_input.lower() in ["exit", "quit", "bye"]:
        print("TARS: Goodbye!")
        engine.say("Goodbye!")
        engine.runAndWait()
        break
    
    response = TARS_respond(user_input)
    print("TARS:", response)

    # Make TARS speak the response
    engine.say(response)
    engine.runAndWait()
