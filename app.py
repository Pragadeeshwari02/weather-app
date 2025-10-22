import requests
import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv(dotenv_path="key.env")

page_bg_img ='''
<style>
.stApp {
  background-image: url("https://img.freepik.com/free-vector/sky-background-video-conferencing_23-2148623068.jpg");
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  background-attachment: fixed;
}
</style>'''
st.markdown(page_bg_img, unsafe_allow_html=True)
st.markdown("<h1 style='color: Black;'>🌦️ Weather App</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='color: Black;'>Enter city name:</h2>", unsafe_allow_html=True)
city = st.text_input("Enter City", label_visibility="collapsed")
button = st.button("Get Weather")

def get_weather_data(city):
        api_key = os.getenv("WEATHER_API_KEY")
        base_url = f"http://api.weatherstack.com/current?access_key={api_key}&query={city}"
        response = requests.get(base_url)
        return response.json()

if button:
        data = get_weather_data(city)
        if "current" in data:
            st.markdown(f"<h3 style='color: Black;'>Weather in {city}:</h3>", unsafe_allow_html=True)
            st.markdown(f"<h4 style='color:Black;'> 🌡️Temperature: {data['current']['temperature']}°C</h4>", unsafe_allow_html=True)
            st.markdown(f"<h4 style='color:Black;'> 🌥️Weather Description: {data['current']['weather_descriptions'][0]}</h3>", unsafe_allow_html=True)
            st.image(data['current']['weather_icons'][0])
        else:
            st.markdown("<h3 style='color: Black;'>City not found</h3>", unsafe_allow_html=True)
st.markdown("<h5 style='color: Black;'>Developed by Pragathi</h5>", unsafe_allow_html=True)    