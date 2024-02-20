import json
import os
import requests

# check env vars
API_URL = ""
API_KEY = ""
BASE_URL = ""

if "VIDROVR_API_URL" in os.environ:
    API_URL = os.environ.get("VIDROVR_API_URL", "https://api.vidrovr.com")
else:
    API_URL = "https://api.vidrovr.com"

if "VIDROVR_API_KEY" in os.environ:
    API_KEY = os.environ["VIDROVR_API_KEY"]

if "VIDROVR_API_VERSION" in os.environ:
    BASE_URL = f"{API_URL}/{os.environ.get('VIDROVR_API_VERSION', 'v2')}"

HEADER = {"x-api-key": API_KEY}


class Client:

    """
    #
    # HTTP Get
    #
    """

    def get(url, header=None):
        # did a modified header get sent?
        if header is None:
            header = HEADER

        api_url = f"{BASE_URL}/{url}"

        try:
            response = requests.get(api_url, headers=header)

            response.raise_for_status()

            return json.loads(response.content)["data"] if response.content else None
        except requests.exceptions.RequestException as e:
            print(f"Request error: {e}")
            return None

    """
    #
    # HTTP Delete
    #
    """

    def delete(url, header=None):
        # did a modified header get sent?
        if header is None:
            header = HEADER

        api_url = f"{BASE_URL}/{url}"

        try:
            response = requests.delete(api_url, headers=header)

            response.raise_for_status()

            return json.loads(response.content)["data"] if response.content else None
        except requests.exceptions.RequestException as e:
            print(f"Request error: {e}")
            return None

    """
    #
    # HTTP Patch
    #
    """

    def patch(url, data=None):
        header = {"Accept": "application/json", "x-api-key": API_KEY}
        api_url = f"{BASE_URL}/{url}"

        try:
            response = requests.patch(api_url, headers=header, data=data)

            response.raise_for_status()

            return json.loads(response.content)["data"] if response.content else None
        except requests.exceptions.RequestException as e:
            print(f"Request error: {e}")
            return None

    """
    #
    # HTTP Post
    #
    """

    def post(url, data=None, files=None):
        api_url = f"{BASE_URL}/{url}"

        try:
            # are files being uploaded?
            if files is None:
                header = {"Accept": "application/json", "x-api-key": API_KEY}

                response = requests.post(api_url, headers=header, json=data)
            else:
                header = {"Content-Type": "multipart/form-data", "x-api-key": API_KEY}
                response = requests.post(
                    api_url, headers=header, json=data, files=files
                )

            response.raise_for_status()

            return json.loads(response.content)["data"] if response.content else None
        except requests.exceptions.RequestException as e:
            print(f"Request error: {e}")
            return None
