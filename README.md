# TARS Chatbot - Voice-Activated Assistant

This project is a **voice-activated chatbot** inspired by TARS from *Interstellar*. Using OpenAI's GPT model, it listens to user input via speech, generates text-based responses, and uses text-to-speech to reply with a voice resembling TARS' robotic tone.

## Features

- **Voice Recognition**: Utilizes `speech_recognition` to capture spoken commands and convert them to text.
- **AI-Powered Responses**: Leverages OpenAI's GPT model to generate intelligent, context-aware responses.
- **Text-to-Speech Output**: Uses `pyttsx3` to vocalize responses in a robotic tone inspired by TARS.
- **Customizable Voice Settings**: Adjustable TTS properties for rate, volume, and voice selection to emulate TARS' unique character.

## Requirements

- Python 3.6 or later
- `openai`: For AI-generated responses
- `pyttsx3`: For text-to-speech synthesis
- `speech_recognition`: For voice input and recognition

Install the required libraries using:
```bash
pip install openai pyttsx3 speechrecognition

## How It Works

- **Initialization**: The program sets up TTS properties for a slow, robotic voice.
- **Listening**: It continuously listens for user input via the microphone, with ambient noise adjustment to improve accuracy.
- **Response Generation**: The captured text is sent to OpenAI's GPT model to generate a response.
- **Voice Output**: TTS vocalizes the response, creating an interactive, conversational experience.

## Usage

1. Ensure your OpenAI API key is set directly in the code or via environment variables.
2. Run the script in a Python environment.
3. Speak into the microphone to ask questions or have a conversation with TARS.
4. Say "exit," "quit," or "bye" to end the session.

## Code Overview

- **TARS_respond(prompt)**: Sends the user's input to OpenAI's GPT model and retrieves a response.
- **listen_to_user()**: Listens for voice input, processes ambient noise, and returns recognized text.
- **Chat Loop**: Continuously listens for input, generates responses, and uses TTS to speak the responses.

## Notes

- **Voice Customization**: Adjust `pyttsx3` settings in the code to further refine TARS' tone. The default settings are configured for a slower, deeper voice to match TARS.
- **Preloaded Responses**: Optionally, you can add iconic lines from TARS in *Interstellar* for occasional responses, especially when humor cues are detected.

---

Enjoy your TARS-inspired voice assistant!
