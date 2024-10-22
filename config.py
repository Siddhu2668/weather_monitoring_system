API_KEY = "5ad84d342c74e14904f59c7ff00a5f5b"  # OpenWeatherMap API Key

CITIES = ["Delhi", "Mumbai", "Chennai", "Bangalore", "Kolkata", "Hyderabad"]
API_URL = "https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}"
UPDATE_INTERVAL = 300  # in seconds (5 minutes)
TEMP_THRESHOLD = 35  # Temperature alert threshold in Celsius
CONSECUTIVE_ALERTS = 2  # Number of consecutive threshold breaches before alert
