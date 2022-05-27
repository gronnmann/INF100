weather_stations_1 = {
    "Bergen": {
        "Wind speed": 3.6,
        "Wind direction": "northeast",
        "Precipitation": 5.2,
        "Device": "WeatherMaster500"
    },
    "Trondheim": {
        "Wind speed": 8.2,
        "Wind direction": "northwest",
        "Precipitation": 0.2,
        "Device": "ClimateDiscoverer3000"
    },
    "Svalbard": {
        "Wind speed": 7.5,
        "Wind direction": "southwest",
        "Precipitation": 1.1,
        "Device": "WeatherFinder5.0"
    },
}

weather_stations_2 = {
    "Bergen": {
        "Wind speed": "---",
        "Wind direction": "northeast",
        "Precipitation": 5.2,
        "Device": "WeatherMaster500"
    },
    "Trondheim": {
        "Wind speed": 8.2,
        "Wind direction": "down",
        "Precipitation": 0.2,
        "Device": "ClimateDiscoverer3000"
    },
    "Svalbard": {
        "Wind speed": 7.5,
        "Precipitation": 1.1,
        "Device": "WeatherFinder5.0"
    },
}


def stations_check(stations: dict):
    for station_name, station_data in stations.items():
        station_pass = True

        if not test_1_elements(station_name, station_data):
            station_pass = False

        if not test_2_windspeed(station_data):
            station_pass = False
            print(f"{station_name}: Invalid wind speed")

        if not test_3_wind_direction(station_data):
            station_pass = False
            print(f"{station_name}: Invalid wind direction")

        if not test_4_precipitation(station_data):
            station_pass = False
            print(f"{station_name}: Invalid precipitation")

        if not test_5_device_empty(station_data):
            station_pass = False
            print(f"{station_name}: Device information empty")

        if station_pass:
            print(f"{station_name}: OK")


def test_positive_float(to_test: str):
    try:
        actually_float = float(to_test)

        if actually_float >= 0:
            return True

    except ValueError:
        return False

    return False


required_elements = ["Wind speed", "Wind direction", "Precipitation", "Device"]


def test_1_elements(station_name: str, station_data: dict):
    to_return = True

    for element in required_elements:
        if element not in station_data.keys():
            print(f"{station_name}: Missing {element}")
            to_return = False

    return to_return


def test_2_windspeed(station_data: dict):
    wind_speed_raw = station_data.get("Wind speed", "NaN")

    return test_positive_float(wind_speed_raw)


allowed_wind_directions = ["north", "south", "east", "west", "northeast", "northwest", "southeast", "southwest"]


def test_3_wind_direction(station_data: dict):
    if station_data.get("Wind direction") in allowed_wind_directions:
        return True

    return False


def test_4_precipitation(station_data: dict):
    precititation = station_data.get("Precipitation", "NaN")

    return test_positive_float(precititation)


def test_5_device_empty(station_data: dict):
    device = station_data.get("Device")

    if not device:
        return False

    return True


if __name__ == "__main__":

    dict_to_test = {
        "weather_stations_1": weather_stations_1,
        "weather_stations_2": weather_stations_2,
    }

    for dict_name, dict_obj in dict_to_test.items():
        print(f"La oss teste værdata {dict_name}")
        stations_check(dict_obj)
        print()
