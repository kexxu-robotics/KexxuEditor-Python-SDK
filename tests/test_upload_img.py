# Written by: Jurriaan Schreuder


import os
import unittest
from kexxu_editor_sdk.api.upload_image import upload_image

class TestKexxuUploaderLive(unittest.TestCase):

    def setUp(self):
        # 1. Grab the live API key from the environment
        self.api_key = os.getenv("KEXXU_API_KEY")
        self.ai_object_id = os.getenv("KEXXU_PROJECT_ID")
        
        # Fail early if the user forgot to export the environment variable
        if not self.api_key:
            self.fail("CRITICAL: KEXXU_API_KEY environment variable is not set.")

        # 2. Dynamically locate tests/data/airship.jpg relative to this test file
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.image_path = os.path.join(base_dir, "tests", "data", "airship.jpg")

        # Quick safety check to ensure your test asset is actually there
        if not os.path.exists(self.image_path):
            self.fail(f"Test image missing at: {self.image_path}. Please place 'airship.jpg' inside tests/data/")

    def test_live_image_upload(self):
        """Executes a real HTTP POST request against the live Kexxu endpoint."""
        print(f"\n[LIVE TEST] Uploading {self.image_path} to Kexxu production...")

        try:
            response = upload_image(
                file_path=self.image_path,
                api_key=self.api_key,
                name="airship_integration_test.jpg",
                image_group_name="ci_tests",
                ai_object_id=int(self.ai_object_id),
                host="https://api.kexxu.com"  # Real Endpoint
            )

            # Assertions based on standard HTTP success
            print(f"[LIVE TEST] Response status: {response.status_code}")
            print(f"[LIVE TEST] Server replied: {response.text}")
            
            self.assertEqual(response.status_code, 200, f"Expected 200 OK, got {response.status_code}")

        except Exception as e:
            self.fail(f"Live upload raised an unexpected exception: {e}")

if __name__ == "__main__":
    unittest.main()
