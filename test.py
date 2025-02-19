import obsws_python as obs

client = obs.ReqClient(host='10.0.0.3', port=4455, password='7Fm2xoPwhQVi5Cua')

# Fetch the OBS recording directory
response = client.get_record_directory()

# Extract and print the actual directory path
print("🎯 OBS Default Save Location:", response.record_directory)
