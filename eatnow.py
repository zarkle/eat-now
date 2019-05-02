"""
A CLI for food trucks.
"""
import os, requests, json
from datetime import datetime as DT

# API_URL = 'https://data.sfgov.org/resource/jjew-r69b.json'
APP_TOKEN = os.getenv('APPTOKEN')
API_URL = f'https://data.sfgov.org/resource/jjew-r69b.json?$$app_token={APP_TOKEN}'


def main():
    """."""
    today = DT.today().weekday() + 1
    response = requests.get(f'{API_URL}&dayorder={today}')
    if response.status_code == 200:
        data = response.json()
        # print(data)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('\nThanks for visiting.')
