def calibration_readout(wind_speed):
    updated = []

    for num, speed in enumerate(wind_speed):
        if num % 12 == 0:
            updated.append( ("Calibration hour", speed))
        else:
            updated.append(speed)

    return updated