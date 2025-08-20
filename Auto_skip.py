import pyautogui
import time
import os

class YouTubeAdSkipper:
    def __init__(self, image_path):
        self.running = False
        self.skip_button_image = image_path

    def find_and_click_skip_button(self):
        try:
            # The confidence level can be adjusted based on the quality of your screenshot.
            # A lower number (e.g., 0.7) is more forgiving but can lead to false positives.
            # A higher number (e.g., 0.9) is more precise but might miss the button.
            button_location = pyautogui.locateOnScreen(self.skip_button_image, confidence=0.8)

            if button_location:
                # Get the center coordinates of the found image
                center_x, center_y = pyautogui.center(button_location)
                # Click the button
                pyautogui.click(center_x, center_y)
                return True
            else:
                return False

        except pyautogui.ImageNotFoundException:
            # This is a common exception when the image is not found, so we just return False.
            return False
        except Exception as e:
            # Handle any other unexpected errors
            return False

    def run(self):
        # Check if the provided image path is valid before starting the loop.
        if not os.path.exists(self.skip_button_image):
            print(f"Error: The image file '{self.skip_button_image}' was not found.")
            print("Please ensure you have entered the correct, full path to the image.")
            return

        self.running = True
        print("YouTube Ad Skipper is running. Press Ctrl+C to stop.")

        while self.running:
            try:
                self.find_and_click_skip_button()
                # Wait for 1 second before checking for the button again.
                time.sleep(1)

            except KeyboardInterrupt:
                # Stop the loop when the user presses Ctrl+C.
                print("Stopping...")
                self.running = False
            except Exception as e:
                # In case of an unexpected error, wait a bit and try again.
                time.sleep(2)

def main():
    # Prompt the user to enter the full path to their image file.
    # image_path = input("Please enter the full path to your 'Skip Ads.png' file: ")
    image_path = r"C:\Users\HP\Desktop\vs\Learning Automation\Skip Ads.png"
    
    # Create an instance of the class with the user-provided path.
    skipper = YouTubeAdSkipper(image_path)
    skipper.run()

if __name__ == "__main__":
    main()
