import obsws_python as obs
from obsws_python import ReqClient
import time
import cv2
import os

# ✅ Connect to OBS WebSocket
try:
    client = obs.ReqClient(host='10.0.0.3', port=4455, password='7Fm2xoPwhQVi5Cua')  # Update IP & password
    print("✅ Connected to OBS WebSockets successfully!")
except Exception as e:
    print(f"❌ Failed to connect to OBS WebSockets: {e}")
    exit()

try:
    response = client.get_scene_list()
    if hasattr(response, "scenes"):
        scenes = [scene["sceneName"] for scene in response.scenes]  # Extract scene names
        print("🖥️ Available Scenes:", scenes)
    else:
        print("❌ No valid scene data received from OBS.")
        exit()
except Exception as e:
    print(f"❌ Failed to fetch scene list: {e}")
    exit()

def capture_frame():
    """Captures a frame from OBS and saves it as an image."""
    try:
        screenshot_path = "/tmp/screenshot.png"  # Ensure directory exists

        response = client.save_source_screenshot(
            name="CS2",  
            img_format="png",
            file_path=screenshot_path,  
            width=1920,  
            height=1080,  
            quality=-1  
        )

        print("📸 Screenshot response:", response)

        # ✅ Check if response contains useful data
        if response:
            print(f"📸 Screenshot saved: {screenshot_path}")
        else:
            print("❌ No response received from OBS WebSocket.")

        # ✅ Verify if screenshot was saved
        if os.path.exists(screenshot_path):
            frame = cv2.imread(screenshot_path)
            if frame is not None:
                print("✅ Frame successfully loaded!")
                return frame
            else:
                print("❌ Failed to load screenshot as an image.")
                return None
        else:
            print("❌ Screenshot file not found. Check OBS logs.")
            return None

    except Exception as e:
        print(f"❌ Failed to capture frame: {e}")
        return None


capture_frame()