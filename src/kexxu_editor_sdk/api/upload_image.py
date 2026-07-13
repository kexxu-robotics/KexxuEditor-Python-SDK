import os
import time
from datetime import datetime, timezone
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

def upload_image(
    file_path: str,
    api_key: str,
    ai_object_id: int,
    name: str,
    image_group_name: str,
    image_group_subfolder: str = "",
    timestamp_ms: int = None,
    device_type: str = "user-upload",
    host: str = "[https://api.kexxu.com](https://api.kexxu.com)"
) -> requests.Response:
    """
    Uploads an image to the Kexxu API using exact multipart boundaries and defaults.
    """

    # default timestamp to now
    if timestamp_ms is None:
        timestamp_ms = int(time.time() * 1000)

    url = f"{host.rstrip('/')}/api/images/upload"
    params = {
        "type": device_type,
        "version": "1",
        "name": name,
        "imageGroupSubFolder": image_group_subfolder,
        "imageGroupName": image_group_name,
        "aiObjectId": str(ai_object_id)
    }

    filename = os.path.basename(file_path)
    
    with open(file_path, "rb") as f:
        m = MultipartEncoder(
            fields={'file': (filename, f, 'application/octet-stream')},
            boundary="KexxuMultiPartBoundary"
        )

        headers = {
            "Content-Type": m.content_type,
            "apikey": api_key
        }

        response = requests.post(url, params=params, headers=headers, data=m)
        response.raise_for_status()
        return response
