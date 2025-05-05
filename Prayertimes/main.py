import requests
from time import sleep

ip = requests.get('https://api.ipify.org').text

with open("config.txt", "r", encoding="utf-8") as parameters_config:
    parameters = [line for line in parameters_config.readlines()]
    latitude = parameters[0].strip('\n').split('=')[1]
    longitude = parameters[1].strip('\n').split('=')[1]



link = "https://www.islamicfinder.us/index.php/api/prayer_times"
params = {
    "user_ip": ip,
    "latitude": f"{latitude}",
    "longitude": f"{longitude}",
    "method": '5'

}

response = requests.get(link, params=params)
# print(response.status_code)
data = response.json()
# print(data["results"])
fajr: str = data["results"]["Fajr"]
duha: str = data["results"]["Duha"]
duhr: str = data["results"]["Dhuhr"]
asr: str = data["results"]["Asr"]
maghrib: str = data["results"]["Maghrib"]
isha: str = data["results"]["Isha"]

print(f"AL-Fajr: {fajr.split('%')[0]}{fajr.split('%')[1].upper()}")
print(f"AL- DUHA: {duha.split('%')[0]}{duha.split('%')[1].upper()}")
print(f"Al-DUHR: {duhr.split('%')[0]}{duhr.split('%')[1].upper()}")
print(f"AL- ASR: {asr.split('%')[0]}{asr.split('%')[1].upper()}")
print(f"AL- MAGHRIB: {maghrib.split('%')[0]}{maghrib.split('%')[1].upper()}")
print(f"AL- ISHA: {isha.split('%')[0]}{isha.split('%')[1].upper()}")


keep_alive = True
while keep_alive:
    sleep(1000)