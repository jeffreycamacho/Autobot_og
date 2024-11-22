import pyautogui
import time

def find_and_double_click(image_paths, confidence=0.7):
    """
    Locate an image on the screen from multiple options and double-click on it.
    
    Args:
    image_paths (list): A list of paths to the images to locate.
    confidence (float, optional): The confidence threshold for image recognition. Default is 0.7.
    
    Returns:
    tuple: The (x, y) coordinates of the image center if found, otherwise None.
    """
    for image_path in image_paths:
        try:
            location = pyautogui.locateOnScreen(image_path, confidence=confidence)
            if location:
                pyautogui.doubleClick(pyautogui.center(location))
                print(f"Found and double-clicked: {image_path}")
                return pyautogui.center(location)
            else:
                print(f"Image not found: {image_path}")
        except pyautogui.ImageNotFoundException:
            print(f"ImageNotFoundException for: {image_path}")
    return None

def find_and_click(image_paths, confidence=0.7):
    """
    Locate an image on the screen from multiple options and click on it.
    
    Args:
    image_paths (list): A list of paths to the images to locate.
    confidence (float, optional): The confidence threshold for image recognition. Default is 0.7.
    
    Returns:
    tuple: The (x, y) coordinates of the image center if found, otherwise None.
    """
    for image_path in image_paths:
        try:
            location = pyautogui.locateOnScreen(image_path, confidence=confidence)
            if location:
                pyautogui.click(pyautogui.center(location))
                print(f"Found and clicked: {image_path}")
                return pyautogui.center(location)
            else:
                print(f"Image not found: {image_path}")
        except pyautogui.ImageNotFoundException:
            print(f"ImageNotFoundException for: {image_path}")
    return None

def auto_reply_to_slack_thread(notification_images, reply_button_image, reply, delay=0.001, mouse_speed=0.002):
    """
    This function will detect a new Slack notification, double-click on it, move to the message area,
    hover over the message, double-click on the message, detect the reply button,
    click on it, wait for a small delay, type the reply, and then press enter to submit it.
    
    Args:
    notification_images (list): A list of paths to the images of Slack notifications.
    reply_button_image (str): The path to the image of the reply button.
    reply (str): The reply to type.
    delay (int, optional): Delay in seconds before performing the next action. Default is 0.008 seconds.
    mouse_speed (float, optional): Speed of the mouse movement. Default is 0.002 seconds.
    """
    global running
    while running:
        # Step 1: Detect and double-click any Slack notification
        notification_location = find_and_double_click(notification_images, confidence=0.7)
        if notification_location:
            print(f"Notification double-clicked at location: {notification_location}")

            start_time = time.time()
            
            # Step 2: Move to the specified message area coordinates immediately
            message_area_x = 814  # Updated x coordinate
            message_area_y = 1025  # Updated y coordinate
            pyautogui.moveTo(message_area_x, message_area_y, duration=mouse_speed)
            print(f"Hovering over message area at: ({message_area_x}, {message_area_y})")
            
            # Step 3: Double-click on the message area to ensure the reply button appears
            pyautogui.doubleClick()
            print("Double-clicked on the message area")

            # Step 4: Detect the reply button and click it
            if find_and_click([reply_button_image], confidence=0.7):
                print("Reply button clicked")

                # Step 5: Wait for a short delay to ensure the reply box is focused
                time.sleep(0.11)

                # Step 6: Type the reply
                pyautogui.typewrite(reply, interval=0.001)

                # Step 7: Press enter to submit the reply
                pyautogui.press('enter')
                print("Message sent, stopping the script.")

                # Stop the timer
                end_time = time.time()
                elapsed_time = end_time - start_time
                print(f"Time taken: {elapsed_time:.2f} seconds")

                # Stop the loop after sending the message
                running = False
                
        # Sleep for a short time before checking again
        time.sleep(0.001)  # Reduced delay for faster checking

# Paths to the images
notification_images_paths = ['slack_notification1.png', 'slack_notification2.png']
reply_button_image_path = 'reply_button.png'

# The reply you want to type
reply_text = "'"

# Flag to control the running state of the script
running = True

# Call the function to start monitoring and auto-replying with adjustable mouse speed
auto_reply_to_slack_thread(notification_images_paths, reply_button_image_path, reply_text, mouse_speed=0.005)