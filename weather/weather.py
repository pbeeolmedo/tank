#!/usr/bin/env python
import pandas as pd
import requests

def weather_data(data_str):
    web_url = "http://www.bom.gov.au/fwo/IDN60801/IDN60801.94757.json"
    web_json = requests.get(web_url).json()
    return web_json['observations']['data'][0][data_str]
#print(type(web_json))

#print(type(web_json['observations']))
#print(web_json['observations']['header'])
#print(type(web_json['observations']['data'][0]))
temp_now = web_json['observations']['data'][0]['air_temp']
time_now = web_json['observations']['data'][0]["local_date_time_full"]
hum_now = web_json['observations']['data'][0]["rel_hum"]
rain_since_9am = web_json['observations']['data'][0]["rain_trace"]

print(f"Temp is {temp_now}˚C, Rel Hum is {hum_now}%, It has rained {rain_since_9am} mm since 9am - @ unix local time {time_now}")








