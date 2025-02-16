import psutil
import time
import obsws_python as obs

OBS_HOST = "10.0.0.3"
OBS_PORT = 4455
OBS_PASSWORD = "7Fm2xoPwhQVi5Cua"

client = obs.ReqClient(host=OBS_HOST, port=OBS_PORT, password=OBS_PASSWORD)

def is_cs2_running():
    """Check if CS2 process is running."""
    for process in psutil.process_iter(attrs=['name']):
        if process.info['name'] == "cs2.exe":
            return True
    return False

while True:
    if is_cs2_running():
        print("CS2 detected! Starting OBS recording...")
        client.start_record()
        break
    time.sleep(5)  # Check every 5 seconds

