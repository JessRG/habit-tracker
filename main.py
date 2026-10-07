import requests
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

# Read configurations and API keys from .env and inject them into system environment variables
load_dotenv()

USER = os.getenv("USER", "")
TOKEN = os.getenv("TOKEN", "")
GRAPH_ID = os.getenv("GRAPH_ID", "")
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USER,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USER}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "Hr",
    "type": "float",
    "color": "kuro",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USER}/graphs/{GRAPH_ID}"

today = datetime.now()
day = today.strftime("%Y%m%d")
yesterday = today - timedelta(days=1)
day = yesterday.strftime("%Y%m%d")
str_day = "today" if day == today.strftime("%Y%m%d") else "yesterday"

pixel_data = {
    "date": day,
    "quantity": input(f"How many hours did you code {str_day}? "),
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)

pixel_update_endpoint = f"{pixela_endpoint}/{USER}/graphs/{GRAPH_ID}/{day}"

pixel_update_data = {
    "quantity": "8",
}

# response = requests.put(url=pixel_update_endpoint, json=pixel_update_data, headers=headers)
# print(response.text)

pixel_delete_endpoint = f"{pixela_endpoint}/{USER}/graphs/{GRAPH_ID}/{today}"

# response = requests.delete(url=pixel_delete_endpoint, headers=headers)
# print(response.text)