import sensordata as sensorlib

vital_thresholds = {
    "min_hr": "60",
    "max_hr": "100",
    "min_rr": "20",
    "max_rr": "25"
}


sensordata = {
    "patientUUID": "patienta6a93af5-0b0d-432f-af4c-156124a63e59",
    "gwBattery": 96,
    "data": {"deviceID": "00:02:00:01:00:04", "extras": {"HR": 62, "RR": 23, "battery": 96, "ecg": []}},
    "deviceType": "vv330",
    "timestamp": 1665054501000
}

retval = sensorlib.validate_ecg_data(sensorinfo=sensordata, thresholds=vital_thresholds)
print(retval)


sensordata = {
    "patientUUID": "patienta6a93af5-0b0d-432f-af4c-156124a63e59",
    "gwBattery": 96,
    "data": {"deviceID": "00:02:00:01:00:04", "extras": {"HR": 101, "RR": 27, "battery": 96, "ecg": []}},
    "deviceType": "vv330",
    "timestamp": 1665054501000
}

retval = sensorlib.validate_ecg_data(sensorinfo=sensordata, thresholds=vital_thresholds)
print(retval)


sensordata = {
    "patientUUID": "patienta6a93af5-0b0d-432f-af4c-156124a63e59",
    "gwBattery": 96,
    "data": {"deviceID": "00:02:00:01:00:04", "extras": {"HR": 55, "RR": 18, "battery": 96, "ecg": []}},
    "deviceType": "vv330",
    "timestamp": 1665054501000
}

retval = sensorlib.validate_ecg_data(sensorinfo=sensordata, thresholds=vital_thresholds)
print(retval)


sensordata = {
    "patientUUID": "patienta6a93af5-0b0d-432f-af4c-156124a63e59",
    "gwBattery": 96,
    "data": {"deviceID": "00:02:00:01:00:04", "extras": {"HR": 60, "RR": 20, "battery": 96, "ecg": []}},
    "deviceType": "vv330",
    "timestamp": 1665054501000
}

retval = sensorlib.validate_ecg_data(sensorinfo=sensordata, thresholds=vital_thresholds)
print(retval)


sensordata = {
    "patientUUID": "patienta6a93af5-0b0d-432f-af4c-156124a63e59",
    "gwBattery": 96,
    "data": {"deviceID": "00:02:00:01:00:04", "extras": {"HR": 150, "RR": 30, "battery": 96, "ecg": []}},
    "deviceType": "vv330",
    "timestamp": 1665054501000
}

retval = sensorlib.validate_ecg_data(sensorinfo=sensordata, thresholds=vital_thresholds)
print(retval)


sensordata = {
    "patientUUID": "patienta6a93af5-0b0d-432f-af4c-156124a63e59",
    "gwBattery": 96,
    "data": {"deviceID": "00:02:00:01:00:04", "extras": {"HR": 100, "RR": 25, "battery": 96, "ecg": []}},
    "deviceType": "vv330",
    "timestamp": 1665054501000
}

retval = sensorlib.validate_ecg_data(sensorinfo=sensordata, thresholds=vital_thresholds)
print(retval)