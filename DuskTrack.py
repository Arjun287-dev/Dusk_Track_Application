import requests
import streamlit as st
from datetime import datetime,timezone,timedelta

def get_coordinates(city_name):
    API_KEY = "4957901b5453a46183958e9be751a3d4"
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=5&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    if response.status_code != 200:
        print("Geocoding API not working.")
        return None
    return data[0]["name"]

def fetch_sunset_time(city_name):
    API_KEY = "4957901b5453a46183958e9be751a3d4"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    if response.status_code != 200:
        print("Sunset time was not fetched. Please enter valid city name.")
        return None
    sys_data = data["sys"].get("sunset")
    timezone_data = data.get("timezone",0)
    return sys_data,timezone_data

def utc_to_local_time(utc_timestamp,timezone_data):
    utc_time = datetime.fromtimestamp(utc_timestamp,tz=timezone.utc)
    local_time = utc_time + timedelta(seconds=timezone_data)
    return local_time.strftime("%I:%M:%S %p")

st.title("Sunset Time")
city = st.text_input("Enter the City Name")

if st.button("Get Sunset Time"):
    try:
        city_name = get_coordinates(city)
        try:
            sunset_time,timezone_data = fetch_sunset_time(city_name)
            try:
                formatted_time = utc_to_local_time(sunset_time,timezone_data)
                st.subheader(f"The Sunset Time in {city_name} : {formatted_time}")
            except:
                st.error("Couldn't fetch the sunset time")
        except:
            st.error("Invalid city name")
    except:
        st.error("Please enter valid city name")


        