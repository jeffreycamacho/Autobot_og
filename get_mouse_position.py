import pyautogui
import time

print("You have 5 seconds to move your mouse to the desired position.")
time.sleep(5)
print(f"The current mouse position is: {pyautogui.position()}")