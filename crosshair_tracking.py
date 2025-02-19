import obsws_python as obs
from obsws_python import ReqClient
import time
import cv2
import os

#this is connecting via websocket
try:
    client = obs.ReqClient(host='10.0.0.3', port=4455, password='7Fm2xoPwhQVi5Cua')  #to make sure we are connected to the client
    print("Connected to OBS WebSockets successfully!")
except Exception as e:
    print(f"Failed to connect to OBS WebSockets: {e}")
    exit()

try:
    response = client.get_scene_list()
    if hasattr(response, "scenes"):
        scenes = [scene["sceneName"] for scene in response.scenes]  #just a check for if the scene is there
        print("Available Scenes:", scenes)
    else:
        print("No valid scene data received from OBS.")
        exit()
except Exception as e:
    print(f"Failed to fetch scene list: {e}")
    exit()

def capture_frame():
    """Captures a frame from OBS and ensures it is properly detected."""
    
    #note since obs was installed via windows, we have to use the windows path rather than the WSL path
    screenshot_path = "/mnt/c/Users/imar3/Videos/screenshot.png"

    print(f"📸 Attempting to load screenshot from: {screenshot_path}")

    #may not need this, just used to make sure there is time for the file to load
    time.sleep(1)

    #checking that the file is found
    if os.path.isfile(screenshot_path):
        print("Screenshot file found!")

        frame = cv2.imread(screenshot_path)

        #wanting to check file is loading correctly
        if frame is not None:
            print("Frame successfully loaded!")
            return frame
        else:
            print("Failed to load screenshot as an image.")
            return None
    else:
        print("Screenshot file not found. Check OBS logs.")
        return None


capture_frame()