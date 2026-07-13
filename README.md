![Tests](https://github.com/kexxu-robotics/KexxuEditor-Python-SDK/actions/workflows/ci.yml/badge.svg)
[![Coverage](https://codecov.io/gh/kexxu-robotics/KexxuEditor-Python-SDK/branch/main/graph/badge.svg)](https://codecov.io/gh/kexxu-robotics/KexxuEditor-Python-SDK)


KexxuEditor Python SDK
===

For use with the Kexxu Cloud at [https://editor.kexxu.com](https://editor.kexxu.com).

Install with (python>=3.7):

```
pip install git+https://github.com/kexxu-robotics/KexxuEditor-Python-SDK.git
```

### Documentation at:

[kexxu-robotics.github.io/KexxuEditor-Python-SDK/](https://kexxu-robotics.github.io/KexxuEditor-Python-SDK/)


## Examples

In examples folder

### Basic upload image

On [https://editor.kexxu.com](https://editor.kexxu.com) create a project, open the project, select **create api key**, type upload.

Use the project id from the end of the url, something like `https://editor.kexxu.com/#/project/12345` where `12345` is the project id.

Then using Python:

```python

from kexxu_editor_sdk.api import upload_image
import requests

# Core Configuration
API_KEY = "your_actual_api_key_here"
PROJECT_ID = 12345
IMAGE_PATH = "captures/frame_0102.jpg"

# -------------------------------------------------------------
# Example A: Minimal Image Upload
# -------------------------------------------------------------
try:
    print("Initiating standard upload...")
    response = upload_image(
        file_path=IMAGE_PATH,
        api_key=API_KEY,
        ai_object_id=PROJECT_ID,
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
```
