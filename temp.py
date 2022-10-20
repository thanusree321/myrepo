import sensordata as sensorlib

vital_thresholds = {
        "min_temp": "97",
        "max_temp": "100"
}


sensordata = {
        "patientUUID": "patienta6a93af5-0b0d-432f-af4c-156124a63e59",
        "deviceType": "Temperature",
        "battery": 98,
        "value": 97.73,
        "deviceId": "00:02:00:01:00:02",
        "timestamp": 1665054306000
}

retval = sensorlib.validate_temp_data(sensorinfo=sensordata, thresholds=vital_thresholds)
print(retval)


sensordata = {
        "patientUUID": "patienta6a93af5-0b0d-432f-af4c-156124a63e59",
        "deviceType": "Temperature",
        "battery": 98,
        "value": 102.73,
        "deviceId": "00:02:00:01:00:02",
        "timestamp": 1665054306000
}

retval = sensorlib.validate_sensor_data(sensorinfo=sensordata, thresholds=vital_thresholds)
print(retval)


sensordata = {
        "patientUUID": "patienta6a93af5-0b0d-432f-af4c-156124a63e59",
        "deviceType": "Temperature",
        "battery": 98,
        "value": 96,
        "deviceId": "00:02:00:01:00:02",
        "timestamp": 1665054306000
}

retval = sensorlib.validate_sensor_data(sensorinfo=sensordata, thresholds=vital_thresholds)
print(retval)


sensordata = {
        "patientUUID": "patienta6a93af5-0b0d-432f-af4c-156124a63e59",
        "deviceType": "Temperature",
        "battery": 98,
        "value": 97.23,
        "deviceId": "00:02:00:01:00:02",
        "timestamp": 1665054306000
}

retval = sensorlib.validate_sensor_data(sensorinfo=sensordata, thresholds=vital_thresholds)
print(retval)


sensordata = {
        "patientUUID": "patienta6a93af5-0b0d-432f-af4c-156124a63e59",
        "deviceType": "Temperature",
        "battery": 98,
        "value": 150.23,
        "deviceId": "00:02:00:01:00:02",
        "timestamp": 1665054306000
}

retval = sensorlib.validate_sensor_data(sensorinfo=sensordata, thresholds=vital_thresholds)
print(retval)


sensordata = {
        "patientUUID": "patienta6a93af5-0b0d-432f-af4c-156124a63e59",
        "deviceType": "Temperature",
        "battery": 98,
        "value": 97,
        "deviceId": "00:02:00:01:00:02",
        "timestamp": 1665054306000
}

retval = sensorlib.validate_sensor_data(sensorinfo=sensordata, thresholds=vital_thresholds)
print(retval)