import requests as req
import matplotlib.pyplot as plt
import pandas as pd
import os

#current
def current_weather(name):
    base_url_current = "https://api.weatherapi.com/v1/current.json?q="
    URL = f"{base_url_current}{name}&key=2f64fab5490c4d2f97263016251802"
    response = req.get(URL)
    
    if response.status_code == 200:
        data = response.json()
        city_name = data['location']['name']
        country = data['location']['country']
        temperature_c = data['current']['temp_c']
        temperature_f = data['current']['temp_f']
        condition = data['current']['condition']['text']
        print("Here are your results:\nkaraj")
        print(f"🌍 {city_name} in {country} 🌍\n 🌡 {temperature_c}°C {temperature_f}°F🌡\n -Condition is: {condition}")
        print("-" * 30)
        return {
            "City": city_name,
            "Country": country,
            "Temperature (°C)": temperature_c,
            "Temperature (°F)": temperature_f,
            "Condition": condition
        }
    else:
        print("Your request could not be satisfied 😬😵")
        return None

#forecast
def forecast_weather(name):
    base_url_forecast = "https://api.weatherapi.com/v1/forecast.json?q="
    URL = f"{base_url_forecast}{name}&days=5&alerts=no&aqi=no&key=2f64fab5490c4d2f97263016251802"
    response = req.get(URL)
    
    if response.status_code == 200:
        data = response.json()
        if "forecast" in data:
            forecast_days = data['forecast']['forecastday']
            dates = []
            max_temps = []
            min_temps = []
            humidity = []
            conditions = []
            
            for day in forecast_days:
                date = day['date']
                max_temp_c = day['day']['maxtemp_c']
                min_temp_c = day['day']['mintemp_c']
                avg_humidity = day['day']['avghumidity']
                condition = day['day']['condition']['text']
                
                dates.append(date)
                max_temps.append(max_temp_c)
                min_temps.append(min_temp_c)
                humidity.append(avg_humidity)
                conditions.append(condition)
                
                print(f"📆 Date: {date}")
                print(f"🔵 Temperature °C ➡ MIN: {min_temp_c} MAX: {max_temp_c}")
                print(f"🟢 Humidity: {avg_humidity}%")
                print(f"🌦 Condition: {condition}")
                print("-" * 30)
            
            
            plt.figure(figsize=(8, 5))
            plt.plot(dates, max_temps, marker="o", linestyle="-", color="red", label="Max Temp(°C)")
            plt.plot(dates, min_temps, marker="o", linestyle="--", color="blue", label="Min Temp(°C)")
            plt.xlabel("Date")
            plt.ylabel("Temperature (°C)")
            plt.title(f"Temperature forecast in {name} (next 5 days)")
            plt.xticks(rotation=45)
            plt.legend()
            plt.grid(True)
            plt.show()

            
            return {
                "City": name,
                "Dates": dates,
                "Max Temp(°C)": max_temps,
                "Min Temp(°C)": min_temps,
                "Humidity (%)": humidity,
                "Condition": conditions
            }
    else:
        print("Your request could not be satisfied 😬😵")
        return None

# save function
def save_data_to_excel(data, file_path="weather_data.xlsx"):
    try:
        df = pd.DataFrame(data)
        df.to_excel(file_path, index=False, engine="openpyxl")
        print(f"✅ Data successfully saved to '{os.path.abspath(file_path)}'!")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

# Main
print ('welcome to weather prediction project executed by Kian Heidari & Pouya Bayramalidoost')
name = input("😎 Enter your desired city name: ")
current_data = current_weather(name)
forecast_data = forecast_weather(name)

save =str(input("would you like to recieve an excel file of the presented data?(yes/no): "))
if save == "yes":
     if forecast_data:
        save_data_to_excel(forecast_data,"weather_forecast.xlsx")
     print("Thank you for your Time :)")
else:
     print("Thank you for your Time :)")