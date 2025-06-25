# # import pywhatkit as kit
# # import time
# # import pyautogui
# # from pynput.keyboard import Key, Controller

# # keyboard = Controller()

# # def send_whatsapp_message(phone_no, message):
# #     """
# #     Send WhatsApp message instantly with proper error handling and tab management
# #     """
# #     try:
# #         kit.sendwhatmsg_instantly(phone_no, message, wait_time=15)
# #         time.sleep(5)  # Wait for page to load
        
# #         # Press Enter to send
# #         pyautogui.press('enter')
# #         time.sleep(0.5)
        
# #         # Close the tab
# #         keyboard.press(Key.ctrl)
# #         keyboard.press('w')
# #         keyboard.release('w')
# #         keyboard.release(Key.ctrl)
        
# #         return True
# #     except Exception as e:
# #         print(f"Error sending message: {e}")
# #         return False

# # def get_message():
# #     """Get message from user"""
# #     while True:
# #         message = input("Enter the Message: ").strip()
# #         if message:
# #             return message
# #         print("Message cannot be empty!")

# # def get_phone_number():
# #     """Get valid phone number from user"""
# #     while True:
# #         try:
# #             number = input("Enter the Phone number (with country code, e.g., +911234567890): ").strip()
# #             if not number.startswith('+'):
# #                 print("Please include country code (e.g., +91)")
# #                 continue
# #             # Simple validation - you might want to add more
# #             if len(number) < 10:
# #                 print("Phone number too short!")
# #                 continue
# #             return number
# #         except Exception as e:
# #             print(f"Invalid input: {e}")
# #             get_phone_number()
            

# # def get_time_input():
# #     """Get time from user if they want to schedule"""
# #     while True:
# #         choice = input("Do you want to schedule the message? (yes/no): ").lower()
# #         if choice in ['yes', 'no']:
# #             if choice == 'yes':
# #                 while True:
# #                     try:
# #                         hour = int(input("Enter hour (24-hour format): "))
# #                         if 0 <= hour <= 23:
# #                             break
# #                         print("Hour must be between 0-23")
# #                     except ValueError:
# #                         print("Please enter a valid number")
                
# #                 while True:
# #                     try:
# #                         minute = int(input("Enter minute: "))
# #                         if 0 <= minute <= 59:
# #                             break
# #                         print("Minute must be between 0-59")
# #                     except ValueError:
# #                         print("Please enter a valid number")
                
# #                 return hour, minute
# #             else:
# #                 return None, None

# # def get_repeat_count():
# #     """Get how many times to send the message"""
# #     while True:
# #         try:
# #             count = int(input("How many times to send the message? (1-100): "))
# #             if 1 <= count <= 100:
# #                 return count
# #             print("Please enter between 1-100")
# #         except :
# #             print("Please enter a valid number")

# # def main():
# #     print("WhatsApp Message Sender")
# #     print("Note: Please ensure you're logged in to WhatsApp Web in your default browser")
# #     print("Keep the browser open but don't touch your keyboard/mouse during sending\n")
    
# #     phone_number = get_phone_number()
# #     message = get_message()
# #     hour, minute = get_time_input()
# #     repeat_count = get_repeat_count()
    
# #     success_count = 0
# #     for i in range(repeat_count):
# #         print(f"\nAttempt {i+1} of {repeat_count}")
        
# #         try:
# #             if hour is not None and minute is not None:
# #                 # For scheduled messages
# #                 kit.sendwhatmsg(phone_number, message, hour, minute)
# #             else:
# #                 # For instant messages
# #                 if not send_whatsapp_message(phone_number, message):
# #                     continue
            
# #             success_count += 1
# #             print("Message sent successfully!")
            
# #             # Small delay between messages
# #             if i < repeat_count - 1:
# #                 time.sleep(2)
                
# #         except Exception as e:
# #             print(f"Failed to send message: {e}")
    
# #     print(f"\nSummary: Sent {success_count}/{repeat_count} messages successfully")
    
# #     if input("\nSend more messages? (yes/no): ").lower() == 'yes':
# #         main()

# # if __name__ == "__main__":
# #     main()

import pywhatkit as kit
import time
import pyautogui

def open_chat(phone_no):
    try:
        # Open WhatsApp chat instantly
        kit.sendwhatmsg_instantly(phone_no, "", wait_time=15, tab_close=False)
        time.sleep(5)  # Wait for the chat to open
        return True
    except Exception as e:
        print(f"Error opening chat: {e}")
        return False

def send_message_from_open_chat(message):
    try:
        pyautogui.write(message)
        time.sleep(0.5)
        pyautogui.press('enter')
        return True
    except Exception as e:
        print(f"Error sending message: {e}")
        return False

def main():
    phone_number = input("Enter phone number with country code (e.g. +911234567890): ").strip()
    if not open_chat(phone_number):
        return

    repeat_count = int(input("How many messages to send? "))
    message = input("Enter the message: ")

    for i in range(repeat_count):
        print(f"Sending message {i+1} of {repeat_count}")
        if not send_message_from_open_chat(message):
            break
        time.sleep(1)  # Delay between messages

    print("All messages sent!")

if __name__ == "__main__":
    main()

