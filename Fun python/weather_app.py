#bd5e378503939ddaee76f12ad7a97608
import tkinter as tk
from tkinter import messagebox
import requests

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather App")

        # API key (replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key)
        self.api_key = 'bd5e378503939ddaee76f12ad7a97608'

        # Create UI elements
        self.location_label = tk.Label(root, text="Enter Location:")
        self.location_label.pack(pady=10)

        self.location_entry = tk.Entry(root)
        self.location_entry.pack(pady=10)

        self.get_weather_button = tk.Button(root, text="Get Weather", command=self.get_weather)
        self.get_weather_button.pack(pady=10)

        self.result_label = tk.Label(root, text="", font=("Helvetica", 14))
        self.result_label.pack(pady=10)

    def get_weather(self):
        location = self.location_entry.get()
        if not location:
            messagebox.showerror("Input Error", "Please enter a location.")
            return

        url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={self.api_key}&units=metric"
        
        try:
            response = requests.get(url)
            data = response.json()

            if response.status_code == 200:
                temperature = data['main']['temp']
                weather_description = data['weather'][0]['description']
                self.result_label.config(text=f"Temperature: {temperature}°C\nDescription: {weather_description.capitalize()}")
            else:
                messagebox.showerror("Error", data.get("message", "Location not found."))

        except requests.exceptions.RequestException as e:
            messagebox.showerror("Network Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()