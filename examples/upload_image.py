from kexxu_editor_sdk.api.upload_image import upload_image
import requests

# Core Configuration
API_KEY = "your_actual_api_key_here"
IMAGE_PATH = "captures/frame_0102.jpg"

# -------------------------------------------------------------
# Example A: Minimal Image Upload
# -------------------------------------------------------------
try:
    print("Initiating standard upload...")
    response = upload_image(
        file_path=IMAGE_PATH,
        api_key=API_KEY,
        ai_object_id=1234,
        name="doorway_detection_01.jpg",
        image_group_name="main_entrance",
    )
    
    if response.status_code == 200:
        print("Upload successful!")
        print(f"Server Response: {response.text}")

except requests.exceptions.HTTPError as http_err:
    print(f"HTTP Error occurred: {http_err} - {http_err.response.text}")
except Exception as err:
    print(f"An unexpected error occurred: {err}")


# -------------------------------------------------------------
# Example B: Advanced Image Upload with extra options
# -------------------------------------------------------------
try:
    print("\nInitiating advanced staging upload...")
    response = upload_image(
        file_path=IMAGE_PATH,
        api_key=API_KEY,
        ai_object_id=1234,
        name="image_000473.jpg",
        image_group_name="factory_runs",
        image_group_subfolder="2026/run2", # Custom folder path '/' delimeted
        timestamp_ms=1783944317634, # Custom time this image was made
        host="https://beta-api.kexxu.com", # Point to alternate server
        device_type="MyCustomDevice" # Custom device signature
    )
    print(f"Staging Upload Status: {response.status_code}")

except Exception as err:
    print(f"Staging upload failed: {err}")
