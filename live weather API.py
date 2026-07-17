import requests
# API Endpoint
url = "https://api.open-meteo.com/v1/forecast"
#Parameters
params = {
    "latitude": 23.1984,
    "longitude": 77.0952,
    "current_weather": True
}
#send GET Request
response = requests.get(url, params=params)
#check status
print("status code:",response.status_code)
#Convert Json Response
data = response.json()
#Print Full Json
print("\nFull Response:")
print(data)
#Extract Weather Information
weather = data["current_weather"]
print("\ncurrent Weather Details")
print("Temperature:", weather["temperature"],"°C")
print("Wind Direction:",weather["winddirection"])
print("Weather Code:", weather["weathercode"])
print("Wind Speed:", weather["windspeed"],"km/h")
import matplotlib.pyplot as plt

weather = data["current_weather"]

labels = ["Temperature", "Wind Direction", "Weather Code", "Wind Speed"]
values = [
    weather["temperature"],
    weather["winddirection"],
    weather["weathercode"],
    weather["windspeed"]
]

colors = ["red", "blue", "green", "orange"]

plt.figure(figsize=(8,5))
bars = plt.bar(labels, values, color=colors)

plt.title("Current Weather Details", fontsize=15)
plt.xlabel("Parameters")
plt.ylabel("Values")

# Add values on bars
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width()/2,
        height,
        f"{height}",
        ha="center",
        va="bottom",
        fontsize=10
    )

plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()