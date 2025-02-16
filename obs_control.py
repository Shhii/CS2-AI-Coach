import obsws_python as obs
import time

# OBS WebSocket Settings (Update if needed)
OBS_HOST = "10.0.0.3"  # Replace with the IP that worked in wscat
OBS_PORT = 4455
OBS_PASSWORD = "7Fm2xoPwhQVi5Cua"  # Replace with your actual OBS WebSocket password

# Connect to OBS WebSockets
try:
    client = obs.ReqClient(host=OBS_HOST, port=OBS_PORT, password=OBS_PASSWORD)
    print("✅ Connected to OBS WebSockets successfully!")

    # Check if recording is already running
    recording_status = client.get_record_status()
    
    if recording_status.output_active:
        print("⏹ Stopping existing recording...")
        client.stop_record()
    else:
        print("▶️ Starting new recording...")
        client.start_record()

    # Optional: Let recording run for a few seconds
    time.sleep(5)  # Adjust time as needed

    # Stop recording after delay (optional)
    print("⏹ Stopping recording after delay...")
    client.stop_record()

except Exception as e:
    print(f"❌ Error: {e}")
