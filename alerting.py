from config import TEMP_THRESHOLD, CONSECUTIVE_ALERTS

consecutive_breaches = {}

def check_thresholds(city, data):
    global consecutive_breaches
    temp = data['temp']

    if temp > TEMP_THRESHOLD:
        consecutive_breaches[city] = consecutive_breaches.get(city, 0) + 1
        if consecutive_breaches[city] >= CONSECUTIVE_ALERTS:
            print(f"ALERT: {city} temperature exceeds {TEMP_THRESHOLD}°C for {consecutive_breaches[city]} consecutive updates. Current Temp: {temp:.2f}°C")
    else:
        consecutive_breaches[city] = 0
