def adjust_daily_temps(daily_temps):
    list_converted = [list(dag) for dag in daily_temps]

    list_converted[4][1] = 10.0

    daily_temps = tuple([tuple(dag) for dag in list_converted])

    return daily_temps

