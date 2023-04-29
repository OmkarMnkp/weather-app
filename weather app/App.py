
#created by OMKAR MANKAPE

from tkinter import*
from ttkbootstrap import *
import requests
from ttkbootstrap import Style

API_KEY = "6288f9d71b5cfa6d5cb8f3f3dba4a0e6"

# URL to get weather data from OpenWeatherMap
URL = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}"

class Weather:
    def __init__(self,m):
        self.m = m
        
        self.m.title("WEATHER APP") 
        self.m.geometry("400x415")
      
        self.m.label_weather = Label(self.m,text="CURRENT WEATHER",bootstyle = "primary,info",font="comicsansms 20 bold",padding=6)
        self.m.label_weather.place(x=10,y=10)
        
        self.m.weather_img = PhotoImage(file="weather-app.png")
        self.m.label_weather = Label(self.m,image=m.weather_img)
        self.m.label_weather.place(x=200,y=70)

        self.m.el = Label(self.m,text="ENTER LOCATION",bootstyle = "primary,info",font="comicsansms 12 bold",padding=4)
        self.m.el.place(x=200,y=210)

        self.location_entry = Entry(self.m)
        self.location_entry.place(x=210,y=250)

        self.m.button = Button(self.m,text="CLICK",command=self.getweather,bootstyle = "primary,outline")
        self.m.button.place(x=250,y=290)

        self.result_label = tk.Label(self.m, text="")
        self.result_label.place(x=200,y=330)

        self.m.weather_img1 = PhotoImage(file="sun.png")
        self.m.label_weather1 = Label(self.m,image=m.weather_img1)
        self.m.label_weather1.place(x=20,y=70)

        self.m.weather_img2 = PhotoImage(file="sun (1).png")
        self.m.label_weather2 = Label(self.m,image=m.weather_img2)
        self.m.label_weather2.place(x=20,y=140)

        self.m.weather_img3 = PhotoImage(file="rain.png")
        self.m.label_weather3 = Label(self.m,image=m.weather_img3)
        self.m.label_weather3.place(x=20,y=230)

        self.m.weather_img4 = PhotoImage(file="storm.png")
        self.m.label_weather4 = Label(self.m,image=m.weather_img4)
        self.m.label_weather4.place(x=20,y=310)

        self.m.info = Label(self.m,text="20 TO 35 C ",bootstyle = "primary,info",font="comicsansms 11 bold",padding=4)
        self.m.info.place(x=95,y=90)

        self.m.info = Label(self.m,text="15TO 25 C ",bootstyle = "primary,info",font="comicsansms 11 bold",padding=4)
        self.m.info.place(x=95,y=170)

        self.m.info = Label(self.m,text="10 TO 25 C ",bootstyle = "primary,info",font="comicsansms 11 bold",padding=4)
        self.m.info.place(x=95,y=250)

        self.m.info = Label(self.m,text="9 TO 27 C ",bootstyle = "primary,info",font="comicsansms 11 bold",padding=4)
        self.m.info.place(x=95,y=330)

        self.m.bottom= Label(self.m,text=" mentioned temperature range is depend on the loaction and \nseason.",bootstyle = "primary,info",font="comicsansms 10 bold",padding=4)
        self.m.bottom.place(x=0,y=370)

    def getweather(self):
       
        location = self.location_entry.get()

        # Retrieve weather data for the location using the OpenWeatherMap API
        response = requests.get(URL.format(location, API_KEY))
        data = response.json()

        # Parse the data to get the temperature and description
        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]

        # Update the result label with the temperature and description
        self.result_label.config(text=f"Temperature: {temp}°C\nDescription: {desc}",foreground="RoyalBlue1",font="comicsansms 12 bold")


if __name__ == "__main__":
    root = tk.Tk()
    app = Weather(root)
    style = Style(theme="morph")
    root.mainloop()