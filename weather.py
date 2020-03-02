import requests

def weather_by_city(city_name):
    wether_url = "http://api.worldweatheronline.com/premium/v1/weather.ashx"
    params = {
        "key":"64837ac3976646e3ae444244200203",
        "q": city_name,
        "format": "json",
        "num_of_days": 1,
        "lang": "ru"
    }

    result = requests.get(wether_url,params=params)
    weather = result.json()
    if "data" in weather:
        if"current_condition" in weather["data"]:
            try:
                return weather["data"]["current_condition"][0]
            except(IndexError,TypeError):
                return False

    return False
if __name__== "__main__":
    w = weather_by_city("Moscow,Russia")
    print(w)    