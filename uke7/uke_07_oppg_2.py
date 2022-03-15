def update_weather(weather_string):
    weather_split = weather_string.split(" ")

    return tuple(map(float, weather_split))


def wednesday_weather(weather_tuple):
    return weather_tuple[2]
