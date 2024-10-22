import sqlite3
from datetime import datetime

# Create or connect to SQLite database
conn = sqlite3.connect('weather_data.db')
cur = conn.cursor()

# Create a table if it doesn't exist
cur.execute('''
CREATE TABLE IF NOT EXISTS weather (
    city TEXT,
    temp REAL,
    feels_like REAL,
    condition TEXT,
    timestamp INTEGER
)
''')
conn.commit()

def store_weather_data(city, data):
    cur.execute('''
    INSERT INTO weather (city, temp, feels_like, condition, timestamp)
    VALUES (?, ?, ?, ?, ?)
    ''', (city, data['temp'], data['feels_like'], data['condition'], data['timestamp']))
    conn.commit()

def calculate_daily_summary(city, date):
    start_of_day = int(datetime.strptime(date, '%Y-%m-%d').timestamp())
    end_of_day = start_of_day + 86400

    cur.execute('''
    SELECT AVG(temp), MAX(temp), MIN(temp), condition
    FROM weather
    WHERE city = ? AND timestamp BETWEEN ? AND ?
    ''', (city, start_of_day, end_of_day))

    summary = cur.fetchone()
    return {
        'avg_temp': summary[0],
        'max_temp': summary[1],
        'min_temp': summary[2],
        'dominant_condition': summary[3]
    }
