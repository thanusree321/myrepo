import sensordata as sensorlib

vital_thresholds = {
        "bps_min": "110",
        "bps_max": "130",
        "bpd_min": "65",
        "bpd_max": "85"
}


sensordata = {
    "patientUUID": "patienta3652eea-3d27-4f0f-8d32-81db01b01cbd",
    "deviceType": "BP",
    "battery": 95,
    "data": {"deviceID": "00:02:00:02:00:06", "extras": {"sys": 111, "dia": 67, "heartRate": 79}},
    "timestamp": 1665054435000
}

retval = sensorlib.validate_ihealth_data(sensorinfo=sensordata, thresholds=vital_thresholds)
print(retval)


sensordata = {
    "patientUUID": "patienta3652eea-3d27-4f0f-8d32-81db01b01cbd",
    "deviceType": "BP",
    "battery": 95,
    "data": {"deviceID": "00:02:00:02:00:06", "extras": {"sys": 134, "dia": 87, "heartRate": 79}},
    "timestamp": 1665054435000
}

retval = sensorlib.validate_ihealth_data(sensorinfo=sensordata, thresholds=vital_thresholds)
print(retval)


sensordata = {
    "patientUUID": "patienta3652eea-3d27-4f0f-8d32-81db01b01cbd",
    "deviceType": "BP",
    "battery": 95,
    "data": {"deviceID": "00:02:00:02:00:06","extras": {"sys": 100, "dia": 60, "heartRate": 79}},
    "timestamp": 1665054435000
}

retval = sensorlib.validate_ihealth_data(sensorinfo=sensordata, thresholds=vital_thresholds)
print(retval)


sensordata = {
    "patientUUID": "patienta3652eea-3d27-4f0f-8d32-81db01b01cbd",
    "deviceType": "BP",
    "battery": 95,
    "data": {"deviceID": "00:02:00:02:00:06", "extras": {"sys": 110, "dia": 65, "heartRate": 79}},
    "timestamp": 1665054435000
}

retval = sensorlib.validate_ihealth_data(sensorinfo=sensordata, thresholds=vital_thresholds)
print(retval)


sensordata = {
    "patientUUID": "patienta3652eea-3d27-4f0f-8d32-81db01b01cbd",
    "deviceType": "BP",
    "battery": 95,
    "data": {"deviceID": "00:02:00:02:00:06", "extras": {"sys": 200, "dia": 100, "heartRate": 79}},
    "timestamp": 1665054435000
}

retval = sensorlib.validate_ihealth_data(sensorinfo=sensordata, thresholds=vital_thresholds)
print(retval)


sensordata = {
    "patientUUID": "patienta3652eea-3d27-4f0f-8d32-81db01b01cbd",
    "deviceType": "BP",
    "battery": 95,
    "data": {"deviceID": "00:02:00:02:00:06", "extras": {"sys": 130, "dia": 85, "heartRate": 79}},
    "timestamp": 1665054435000
}

retval = sensorlib.validate_ihealth_data(sensorinfo=sensordata, thresholds=vital_thresholds)
print(retval)

