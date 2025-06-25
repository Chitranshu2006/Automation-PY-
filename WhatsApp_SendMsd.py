import pywhatkit as kit
import speech_recognition as sr
import pyttsx3

# Initialize the speech engine
engine = pyttsx3.init()

# Set properties before using the engine
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to define the input by listining to the user
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.")
            return None

# Define the phone number and message
def message_time (p_no , message , hour , minute):
    kit.sendwhatmsg(p_no, message, hour, minute)

def message_now (p_no , message):
    kit.sendwhatmsg_instantly(p_no, message)

def type_message ():
    speak ("Please type the requirement: ")
    x = input("Enter tha data: ")
    return x

def speak_message ():
    speak ("Please say the requirement: ")
    x = listen()
    return x

def set_data ():
    speak ("Enter 1 for typing the phone number or 2 for speaking the phone number : ")
    choice = int(input("Enter 1 for typing the phone number or 2 for speaking the phone number : "))
    if choice == 1 :
        phone_number = type_message ()
    else :
        phone_number = speak_message ()
        
    speak ("Enter 1 for typing the message or 2 for speaking the message : ")
    choice = int(input("Enter 1 for typing the message or 2 for speaking the message : "))
    if choice == 1 :
        message = type_message ()
    else :
        message = speak_message ()
    
    speak ("Do you want to specy the the time")      
    specify_time = input("Enter yes or no: ")
    if specify_time == "yes":
        speak ("Enter 1 for typing the hour or 2 for speaking the hour ")
        choice = int(input("Enter 1 for typing the hour or 2 for speaking the hour : "))
        if choice == 1 :
            hour = int(type_message ())
        else :
            hour = int(speak_message ())
            
        speak ("Enter 1 for typing the minute or 2 for speaking the mintue ")
        choice = int( input("Enter 1 for typing the minute or 2 for speaking the mintue : "))
        if choice == 1 :
            minute = int(type_message ())
        else :
            minute = int(speak_message ()) 
    else:
        hour = 0
        minute = 0
        
    return phone_number, message, hour, minute
    
def main():
    phone_number, message, hour, minute = set_data()
    try:
        if hour != 0 and minute != 0:
            message_time(phone_number, message, hour, minute)
        else:
            message_now(phone_number, message)
        speak("Message sent successfully!")
        print("Message sent successfully!")
        
    except Exception as e:
        print(f"An error occurred: {e}")\
    
    
    
# Main program loop   
ans = True
speak("Welcome to WhatsApp Automation")            
while ans == True:
    main()
    speak ("Do you want to send another message?")
    ans = input("Enter yes or no: ")
    if ans.lower() == "yes":
        ans = True
    else:
        ans = False
