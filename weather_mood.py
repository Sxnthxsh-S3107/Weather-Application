import requests

API_KEY = "69024b8f35cfddb3ead66dc2545b89f8"
city = input("Enter your city: ")

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
response = requests.get(url)
data = response.json()

if data.get("cod") != 200:
    print("❌ City not found. Please try again.")
else:
    weather = data["weather"][0]["main"]
    temperature = data["main"]["temp"]

    print(f"Weather in {city}: {weather}")
    print(f"Temperature: {temperature}°C")

    weather_moods = {
    "Clear": ("☀️", "Sun’s out! Perfect time to fry like an egg."),
    "Rain": ("🌧️", "Rainy vibes incoming. Umbrella = style + survival."),
    "Clouds": ("☁️", "Cloudy skies — moody, mysterious, and Netflix-approved."),
    "Snow": ("❄️", "Snowball fight mode: ON."),
    "Thunderstorm": ("🌩️", "Thunder outside? Nature's dubstep is playing."),
    "Mist": ("🌫️", "Mist mode: Pretend you’re in a horror movie. 👻"),
	}

# Default emoji and message
emoji, message = weather_moods.get(weather, ("🤷", "Weather’s acting weird. So should you."))

# Add personalized recommendations
recommendation = ""

if weather == "Rain":
    recommendation = "💡 Pro Tip: Carry an umbrella unless you're auditioning for a rain song."
elif weather == "Clear" and temperature > 32:
    recommendation = "🥵 It’s hot! Hydrate or evaporate."
elif weather == "Clear" and temperature < 20:
    recommendation = "🧥 It’s clear but chilly. Time for hoodie season!"
elif weather == "Clouds":
    recommendation = "😌 Good day for hot tea with bajji and staring out the window."
elif weather == "Thunderstorm":
    recommendation = "⚡ Avoid trees. And dramatic monologues."
elif weather == "Snow":
    recommendation = "☃️ Don't eat yellow snow."
elif weather == "Mist":
    recommendation = "🔦 Low visibility! Drive safe (or don’t drive at all)."

# Display all
print(f"{emoji} {message}")
print(f"{recommendation}")

