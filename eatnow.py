"""
A CLI for food trucks.
"""
import requests, json

url = 'https://data.sfgov.org/resource/jjew-r69b.json'

def main():
    """."""
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
    print(data)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('\nThanks for visiting.')
