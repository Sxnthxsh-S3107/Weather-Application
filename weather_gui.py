import requests
import tkinter as tk
from tkinter import messagebox

# Your OpenWeather API Key
API_KEY = "69024b8f35cfddb3ead66dc2545b89f8"

# Weather emojis and messages
weather_moods = {
    "Clear": ("☀️", "Sun’s out! Perfect time to fry like an egg."),
    "Rain": ("🌧️", "Rainy vibes incoming. Umbrella = style + survival."),
    "Clouds": ("☁️", "Cloudy skies — moody, mysterious, and Netflix-approved."),
    "Snow": ("❄️", "Snowball fight mode: ON."),
    "Thunderstorm": ("🌩️", "Thunder outside? Nature's dubstep is playing."),
    "Mist": ("🌫️", "Mist mode: Pretend you’re in a horror movie. 👻"),
}

def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showerror("Oops!", "Please enter a city name!")
        return

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    
    try:
        response = requests.get(url)
        data = response.json()

        if data.get("cod") != 200:
            result_label.config(text="❌ City not found. Try again.")
            return

        weather = data["weather"][0]["main"]
        temp = data["main"]["temp"]

        emoji, message = weather_moods.get(weather, ("🤷", "Weather’s acting weird. So should you."))

        # Recommendations
        recommendation = ""
        if weather == "Rain":
            recommendation = "💡 Pro Tip: Carry an umbrella unless you're auditioning for a rain song."
        elif weather == "Clear" and temp > 32:
            recommendation = "🥵 It’s hot! Hydrate or evaporate."
        elif weather == "Clear" and temp < 20:
            recommendation = "🧥 It’s clear but chilly. Time for hoodie season!"
        elif weather == "Clouds":
            recommendation = "😌 Good day for hot tea with bajji and staring out the window."
        elif weather == "Thunderstorm":
            recommendation = "⚡ Avoid trees. And dramatic monologues."
        elif weather == "Snow":
            recommendation = "☃️ Don't eat yellow snow."
        elif weather == "Mist":
            recommendation = "🔦 Low visibility! Drive safe (or don’t drive at all)."

        final_output = f"📍 {city.title()}\n🌡 {temp}°C\n{emoji} {message}\n{recommendation}"
        result_label.config(text=final_output)

    except Exception as e:
        result_label.config(text="Error fetching data 😵")


# GUI Setup
window = tk.Tk()
window.title("Weather & Mood App 🌦️")
window.geometry("400x300")
window.config(bg="#e0f7fa")

# Input
tk.Label(window, text="Enter city name:", bg="#e0f7fa").pack(pady=10)
city_entry = tk.Entry(window, font=("Arial", 14))
city_entry.pack()

# Button
tk.Button(window, text="Get Weather", command=get_weather, bg="#81d4fa", font=("Arial", 12)).pack(pady=10)

# Result
result_label = tk.Label(window, text="", wraplength=350, bg="#e0f7fa", font=("Arial", 12))
result_label.pack(pady=10)

window.mainloop()
