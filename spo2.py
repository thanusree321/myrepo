import sensordata as sensorlib

vital_thresholds = {
    "min_spo2": "90",
    "max_spo2": "100"
}


sensordata = {
    "patientUUID": "patienta6a93af5-0b0d-432f-af4c-156124a63e59",
    "deviceType": "checkme_O2",
    "spo2": 92,
    "battery": 100,
    "pi": 91,
    "pr": 93,
    "timestamp": 1665054345000
}

retval = sensorlib.validate_spo2_data(sensorinfo=sensordata, thresholds=vital_thresholds)
print(retval)


sensordata = {
    "patientUUID": "patienta6a93af5-0b0d-432f-af4c-156124a63e59",
    "deviceType": "checkme_O2",
    "spo2": 101,
    "battery": 100,
    "pi": 91,
    "pr": 93,
    "timestamp": 1665054345000
}

retval = sensorlib.validate_spo2_data(sensorinfo=sensordata, thresholds=vital_thresholds)
print(retval)


sensordata = {
    "patientUUID": "patienta6a93af5-0b0d-432f-af4c-156124a63e59",
    "deviceType": "checkme_O2",
    "spo2": 81,
    "battery": 100,
    "pi": 91,
    "pr": 93,
    "timestamp": 1665054345000
}

retval = sensorlib.validate_spo2_data(sensorinfo=sensordata, thresholds=vital_thresholds)
print(retval)


sensordata = {
    "patientUUID": "patienta6a93af5-0b0d-432f-af4c-156124a63e59",
    "deviceType": "checkme_O2",
    "spo2": 90,
    "battery": 100,
    "pi": 91,
    "pr": 93,
    "timestamp": 1665054345000
}

retval = sensorlib.validate_spo2_data(sensorinfo=sensordata, thresholds=vital_thresholds)
print(retval)


sensordata = {
    "patientUUID": "patienta6a93af5-0b0d-432f-af4c-156124a63e59",
    "deviceType": "checkme_O2",
    "spo2": 200,
    "battery": 100,
    "pi": 91,
    "pr": 93,
    "timestamp": 1665054345000
}

retval = sensorlib.validate_spo2_data(sensorinfo=sensordata, thresholds=vital_thresholds)
print(retval)


sensordata = {
    "patientUUID": "patienta6a93af5-0b0d-432f-af4c-156124a63e59",
    "deviceType": "checkme_O2",
    "spo2": 100,
    "battery": 100,
    "pi": 91,
    "pr": 93,
    "timestamp": 1665054345000
}

retval = sensorlib.validate_spo2_data(sensorinfo=sensordata, thresholds=vital_thresholds)
print(retval)