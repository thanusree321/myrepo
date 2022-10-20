import sensordata as sensorlib

vital_thresholds = {
    "weight_min": "150",
    "weight_max": "200"
}


sensordata = {
    "patientUUID": "patienta6a93af5-0b0d-432f-af4c-156124a63e59",
    "deviceType": "BodyFatScale",
    "weight": 151,
    "timestamp": 1665054472000
}

retval = sensorlib.validate_digitalscale_data(sensorinfo=sensordata, thresholds=vital_thresholds)
print(retval)


sensordata = {
    "patientUUID": "patienta6a93af5-0b0d-432f-af4c-156124a63e59",
    "deviceType": "BodyFatScale",
    "weight": 201,
    "timestamp": 1665054472000
}

retval = sensorlib.validate_digitalscale_data(sensorinfo=sensordata, thresholds=vital_thresholds)
print(retval)


sensordata = {
    "patientUUID": "patienta6a93af5-0b0d-432f-af4c-156124a63e59",
    "deviceType": "BodyFatScale",
    "weight": 149,
    "timestamp": 1665054472000
}

retval = sensorlib.validate_digitalscale_data(sensorinfo=sensordata, thresholds=vital_thresholds)
print(retval)


sensordata = {
    "patientUUID": "patienta6a93af5-0b0d-432f-af4c-156124a63e59",
    "deviceType": "BodyFatScale",
    "weight": 150,
    "timestamp": 1665054472000
}

retval = sensorlib.validate_digitalscale_data(sensorinfo=sensordata, thresholds=vital_thresholds)
print(retval)

sensordata = {
    "patientUUID": "patienta6a93af5-0b0d-432f-af4c-156124a63e59",
    "deviceType": "BodyFatScale",
    "weight": 300,
    "timestamp": 1665054472000
}

retval = sensorlib.validate_digitalscale_data(sensorinfo=sensordata, thresholds=vital_thresholds)
print(retval)


sensordata = {
    "patientUUID": "patienta6a93af5-0b0d-432f-af4c-156124a63e59",
    "deviceType": "BodyFatScale",
    "weight": 200,
    "timestamp": 1665054472000
}

retval = sensorlib.validate_digitalscale_data(sensorinfo=sensordata, thresholds=vital_thresholds)
print(retval)