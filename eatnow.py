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
    # get day of week
    today = DT.today().weekday() + 1

    # get current time in PST
    now = datetime.datetime.now()
    time = str(nownow).split()[1]
    hour = int(time[:2]) - 8
    curr_time = f'{hour}{time[2:5]}'

    response = requests.get(f'{API_URL}&dayorder={today}')
    if response.status_code == 200:
        data = response.json()[0:5]
        # print(data)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('\nThanks for visiting.')
