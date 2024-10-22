import time
import requests
from weather_data import process_weather_data
from data_storage import store_weather_data
from alerting import check_thresholds
from config import API_KEY, CITIES, API_URL, UPDATE_INTERVAL

def fetch_weather_data(city):
    try:
        url = API_URL.format(city=city, key=API_KEY)
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to fetch data for {city}: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error fetching data for {city}: {e}")
        return None

if __name__ == "__main__":
    while True:
        for city in CITIES:
            data = fetch_weather_data(city)
            if data:
                processed_data = process_weather_data(data)
                store_weather_data(city, processed_data)
                check_thresholds(city, processed_data)
        time.sleep(UPDATE_INTERVAL)
