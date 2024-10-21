import text_to_speech
import speech_to_text
import datetime
import webbrowser
import weather

def actions(data):
    user_data = data.lower()

    if "what is your name" in user_data:
        response = "I don't have a name right now, I am a virtual machine made by my boss Melissa."
        text_to_speech.text_to_speech(response)
        return response
    
    elif "how are you" in user_data:
        response = "I am fine, thank you. How are you?"
        text_to_speech.text_to_speech(response)
        return response
    
    elif "good morning" in user_data:
        response = "Good Morning"
        text_to_speech.text_to_speech(response)
        return response
    
    elif "what is the time" in user_data:
        current_time = datetime.datetime.now()
        Time = f"{current_time.hour} Hour : {current_time.minute} Minute"
        text_to_speech.text_to_speech(Time)
        return Time
    
    elif "shut down" in user_data:
        response = "Shutting Down"
        text_to_speech.text_to_speech(response)
        return response
    
    elif "open youtube" in user_data:
        webbrowser.open("www.youtube.com")
        response = "Opening YouTube"
        text_to_speech.text_to_speech(response)
        return response
    
    elif "open facebook" in user_data:
        webbrowser.open("www.facebook.com")
        response = "Opening Facebook"
        text_to_speech.text_to_speech(response)
        return response
    
    elif "open instagram" in user_data:
        webbrowser.open("www.instagram.com")
        response = "Opening Instagram"
        text_to_speech.text_to_speech(response)
        return response
    
    elif "open twitter" in user_data:
        webbrowser.open("www.twitter.com")
        response = "Opening Twitter"
        text_to_speech.text_to_speech(response)
        return response
    
    elif "open google" in user_data:
        webbrowser.open("www.google.com")
        response = "Opening Google"
        text_to_speech.text_to_speech(response)
        return response
    
    elif "what is the weather" in user_data:
        weather_info = weather.get_weather("Kathmandu")    
        text_to_speech.text_to_speech(weather_info)
        return weather_info
    
    else:
        response = "Sorry, I did not get that"
        text_to_speech.text_to_speech(response)
        return response