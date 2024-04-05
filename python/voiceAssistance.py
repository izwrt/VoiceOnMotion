import speech_recognition as sr
import pyttsx3
import os

# Initialize speech recognition and text-to-speech engines
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to recognize speech
def recognize_speech(prompt, timeout=5):
    with sr.Microphone() as source:
        print(prompt)
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        try:
            audio = recognizer.listen(source, timeout=timeout)  # Timeout set to 5 seconds
            print("Audio:", audio)
            text = recognizer.recognize_google(audio)
            print(f"{prompt.capitalize()} recognized:", text)
            return text.lower()
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that.")
            return None
        except sr.RequestError:
            print("Sorry, I couldn't request results; please check your internet connection.")
            return None
        except sr.WaitTimeoutError:
            print(f"Timeout occurred while listening for {prompt}.")
            return None

# Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to prompt user for information and store it
def get_user_info(name):
    speak(f"Nice to meet you, {name}! Can you tell me your location?")
    location = recognize_speech("Listening for location...")
    if location:
        print("Location recognized:", location)
        speak("Got it. Now, can you tell me your hobbies?")
        hobbies = recognize_speech("Listening for hobbies...")
        if hobbies:
            print("Hobbies recognized:", hobbies)
            # Store user information in a separate file
            file_name = f"{name.lower().replace(' ', '_')}_info.txt"
            with open(file_name, "w") as file:
                file.write(f"Name: {name}\n")
                file.write(f"Location: {location}\n")
                file.write(f"Hobbies: {hobbies}\n")
            speak("Thank you for providing your information!")
        else:
            print("Failed to recognize hobbies.")
            speak("Sorry, I didn't catch that. Can you repeat your hobbies?")
    else:
        print("Failed to recognize location.")
        speak("Sorry, I didn't catch that. Can you repeat your location?")

# Function to check if user is recognized
def recognize_user():
    speak("Welcome back! Can you please tell me your name?")
    name = recognize_speech("Listening for name...")
    if name:
        file_name = f"{name.lower().replace(' ', '_')}_info.txt"
        if os.path.exists(file_name):
            speak("Nice to see you again, " + name + "!")
            return name, file_name
        else:
            get_user_info(name)
            return name, file_name
    return None, None


# Main function
def main():
    user_name, user_file = recognize_user()
    if user_name:
        print("User recognized:", user_name)
        while True:
            if os.path.exists(user_file):
                speak(f"{user_name}, what would you like to know about yourself?")
            else:
                speak(f"Do you have any questions about yourself, {user_name}?")
            response = recognize_speech("Listening for response...")
            if response:
                if "yes" in response:
                    speak("What would you like to know?")
                    query = recognize_speech("Listening for query...")
                    if query:
                        with open(user_file, "r") as file:
                            found = False
                            for line in file:
                                if query.lower() in line.lower():
                                    speak(line.strip())
                                    found = True
                                    break
                            if not found:
                                speak("I'm sorry, I couldn't find the information you requested.")
                                speak("Would you like to provide this information?")
                                response = recognize_speech("Listening for response...")
                                if response and "yes" in response:
                                    speak(f"Sure, please tell me about your {query}.")
                                    info = recognize_speech("Listening for information...")
                                    if info:
                                        with open(user_file, "a") as file:
                                            file.write(f"{query.capitalize()}: {info}\n")
                                        speak("Thank you! I've added this information to your file.")
                else:
                    speak("Okay, let me know if you have any other questions.")
                    break
    else:
        print("Failed to recognize user.")


if __name__ == "__main__":
    main()
