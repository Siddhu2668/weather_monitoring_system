import matplotlib.pyplot as plt
from data_storage import calculate_daily_summary

def plot_daily_summary(city, date):
    summary = calculate_daily_summary(city, date)
    
    temps = [summary['avg_temp'], summary['max_temp'], summary['min_temp']]
    labels = ['Avg Temp', 'Max Temp', 'Min Temp']
    
    plt.bar(labels, temps)
    plt.title(f"Daily Summary for {city} on {date}")
    plt.xlabel('Metric')
    plt.ylabel('Temperature (°C)')
    plt.show()
