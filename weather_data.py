def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def process_weather_data(data):
    temp = kelvin_to_celsius(data['main']['temp'])
    feels_like = kelvin_to_celsius(data['main']['feels_like'])
    condition = data['weather'][0]['main']
    timestamp = data['dt']

    return {
        'temp': temp,
        'feels_like': feels_like,
        'condition': condition,
        'timestamp': timestamp
    }
