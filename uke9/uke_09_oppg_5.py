weather_stations = {  # dict henta fra oppgaveteksten
    "Bergen" : {
        "Wind speed": 3.6,
        "Wind direction": "northeast",
        "Precipitation": 5.2,
        "Device": "WeatherMaster500"
    },
    "Trondheim" : {
        "Wind speed": 8.2,
        "Wind direction": "northwest",
        "Precipitation": 0.2,
        "Device": "ClimateDiscoverer3000"
    },
    "Svalbard" : {
        "Wind speed": 7.5,
        "Wind direction": "southwest",
        "Precipitation": 1.1,
        "Device": "WeatherFinder5.0"
    },
}


for place, weather_info in weather_stations.items():
    print(f"The weather in {place}:")
    print(f"The wind speed is {weather_info.get('Wind speed')} m/s in the {weather_info.get('Wind direction')} direction and the precipitation is {weather_info.get('Precipitation')} mm.")
    print(f"The measurement was done using the {weather_info.get('Device')} weather station.")
    print()
