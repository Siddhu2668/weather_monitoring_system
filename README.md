﻿# weather_monitoring_system
# Real-Time Data Processing System for Weather Monitoring

## Overview

This application fetches real-time weather data from the OpenWeatherMap API for six metro cities in India. It processes and stores the data, generates daily summaries, and triggers alerts based on configurable thresholds. The system also supports visualizations of daily weather summaries.

Project Structure:

weather_monitoring_system/
│
├── config.py                   # Configuration settings
├── main.py                     # Main script to fetch and process weather data
├── weather_data.py             # Data processing utilities
├── data_storage.py             # Data storage using SQLite
├── alerting.py                 # Handles alerts for threshold breaches
├── visualization.py            # Visualization utilities using Matplotlib
├── requirements.txt            # List of dependencies
├── test_cases.py               # Unit tests for the system
└── README.md                   # Documentation


### Features:
1. Fetches real-time weather data from OpenWeatherMap for Indian metros.
2. Converts temperatures from Kelvin to Celsius.
3. Stores data in an SQLite database.
4. Calculates daily summaries (average, max, min temperature).
5. Sends alerts when user-defined temperature thresholds are breached.
6. Visualizes weather data using Matplotlib.

## Prerequisites

- Python 3.8+
- [OpenWeatherMap API Key](https://openweathermap.org/)

## Project Structure

- **config.py**: Contains configuration settings like API key, cities, and thresholds.
- **main.py**: Fetches weather data and processes it continuously.
- **weather_data.py**: Handles weather data parsing and temperature conversion.
- **data_storage.py**: Stores weather data in SQLite and provides daily summary calculations.
- **alerting.py**: Checks for breaches in user-defined temperature thresholds.
- **visualization.py**: Generates bar charts for daily weather summaries.
- **test_cases.py**: Unit tests for various components.
- **requirements.txt**: List of Python libraries required for the project.

Design Choices
1. Modular Architecture: The application is divided into modules (weather_data.py, data_storage.py, alerting.py, visualization.py) for separation of concerns, making it easier to maintain and extend.

2. SQLite Database: Chosen for its simplicity and because it requires no additional setup, making the application lightweight and portable.

3. Configuration File (config.py): Centralizes all configurable parameters, such as API keys, cities, intervals, and thresholds, allowing easy customization.

4. Exception Handling: Implemented basic error handling to ensure the application continues running smoothly even if some API calls fail.

5. Data Persistence: Storing data in a database allows for historical data analysis and is essential for calculating rollups and aggregates.

6. Visualization with Matplotlib: Provides a simple way to generate plots for data analysis.

7. Testing: Included test_cases.py for unit testing critical functions to ensure correctness.

8. Extensibility: Designed to be easily extendable for future enhancements, like adding more weather parameters or integrating with forecasting APIs.


## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Siddhu2668/weather_monitoring_system.git
cd weather_monitoring_system

2. Create a Python Virtual Environment (Optional)
It is recommended to use a virtual environment for managing dependencies.
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install Dependencies
Install the required Python packages using:
pip install -r requirements.txt


4. Set Up Your OpenWeatherMap API Key
You need to provide your OpenWeatherMap API key in config.py:
API_KEY = "your_api_key_here"  # Replace with your OpenWeatherMap API key
5. Run the Application
Start fetching real-time weather data and monitoring:
python main.py

6. Visualize Weather Data
After gathering data for a day, you can visualize the weather summaries using the following command:
python -c 'from visualization import plot_daily_summary; plot_daily_summary("Delhi", "2024-01-01")'

7. Run the Test Suite
Execute the test cases to validate the functionality:
python test_cases.py


