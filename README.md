# Python Virtual Assistant

This project is a Python-based Virtual Assistant capable of performing various tasks through voice and text commands. The assistant can open websites, provide the current time, check the weather, and respond to user queries. It uses speech recognition and text-to-speech functionalities, along with a GUI for text input and interaction.

## Features

- Responds to basic queries like "What is your name?" and "How are you?"
- Opens popular websites like YouTube, Facebook, Instagram, Twitter, and Google
- Fetches current weather information for a specified city
- Provides the current time
- Supports both voice and text input
- Uses a graphical interface built with Tkinter

## Libraries Used

- **Tkinter**: For creating the graphical user interface (GUI)
- **Pillow**: For handling images in the GUI
- **SpeechRecognition**: For converting speech to text
- **Pyttsx3**: For converting text to speech
- **Webbrowser**: For opening websites
- **Requests**: For making API calls to fetch weather data
- **PyAudio**: For microphone input

## How It Works

1. **Speech Recognition**: The assistant listens for voice input, converts it to text using the `SpeechRecognition` library, and processes the commands.
2. **Text-to-Speech**: The assistant responds to user commands with speech using the `Pyttsx3` library.
3. **Weather Information**: The assistant can fetch real-time weather data from OpenWeatherMap using the city name provided in the command.
4. **Web Browsing**: It can open various websites like YouTube, Facebook, Instagram, etc., based on user commands.
5. **Graphical User Interface (GUI)**: Users can interact with the assistant through a Tkinter-based GUI by either speaking or typing commands.

## Project Structure

```bash
|-- action.py           # Handles actions based on user input
|-- weather.py          # Fetches weather information using OpenWeatherMap API
|-- speech_to_text.py   # Converts speech to text using SpeechRecognition
|-- text_to_speech.py   # Converts text to speech using Pyttsx3
|-- main.py             # Main script that runs the GUI
|-- image/              # Contains the image used in the GUI
|-- requirements.txt    # Lists the required libraries

## Usage

```bash
|-- You can interact with the virtual assistant either by speaking or typing into the input field.
|-- The assistant will respond with voice and text in the GUI.
|-- To shut down the assistant, simply say or type "Shut down."

## Future Improvements

```bash
|-- Add more functionalities like setting reminders, sending emails, and playing music.
|-- Improve the speech recognition accuracy by integrating advanced models.
|-- Enhance the GUI with more features and a modern design.


