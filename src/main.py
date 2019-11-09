import api
import os

if __name__ == "__main__":
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] == "1"
    service = api.get_authenticated_service()
