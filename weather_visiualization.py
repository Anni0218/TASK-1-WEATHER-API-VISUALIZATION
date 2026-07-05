import requests
import matplotlib.pyplot as plt

API_KEY = "YOUR_API_KEY"
CITY = "Jamshedpur"

url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

if response.status_code == 200:
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    pressure = data["main"]["pressure"]

    labels = ["Temperature (°C)", "Humidity (%)", "Pressure (hPa)"]
    values = [temperature, humidity, pressure]

    plt.figure(figsize=(8,5))
    plt.bar(labels, values)
    plt.title(f"Weather Data for {CITY}")
    plt.ylabel("Values")

    plt.savefig("weather_chart.png")
    plt.show()

    print("Chart saved successfully!")

else:
    print("Error:", data)