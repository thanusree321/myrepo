def validate_sensor_data(sensorinfo, thresholds):
    """Validate sensor data and return alert information"""
    if "deviceType" not in sensorinfo:
        return []

    if sensorinfo["deviceType"].lower() == "temperature":
        return validate_temp_data(sensorinfo=sensorinfo, thresholds=thresholds)
    elif sensorinfo["deviceType"].lower() == "bp":
        return validate_ihealth_data(sensorinfo=sensorinfo, thresholds=thresholds)
    elif sensorinfo["deviceType"].lower() == "bodyfatscale":
        return validate_digitalscale_data(sensorinfo=sensorinfo, thresholds=thresholds)
    elif sensorinfo["deviceType"].lower() == "vv330":
        return validate_ecg_data(sensorinfo=sensorinfo, thresholds=thresholds)
    elif sensorinfo["deviceType"].lower() == "checkme_02":
        return validate_spo2_data(sensorinfo=sensorinfo, thresholds=thresholds)

    return []

def validate_temp_data(sensorinfo, thresholds):
    # Check temperature details
    value = float(sensorinfo["value"])
    minthr = float(thresholds["min_temp"])
    maxthr = float(thresholds["max_temp"])

    alerts = []
    if value < minthr:
        return [{"type": "temperature", "message": "Low Temperature %s" % value, "pid": sensorinfo["patientUUID"],
                     "timestamp": sensorinfo["timestamp"]}]

    if value > maxthr:
        return [{"type": "temperature", "message": "High Temperature %s" % value, "pid": sensorinfo["patientUUID"],
                     "timestamp": sensorinfo["timestamp"]}]

    return alerts

def validate_ihealth_data(sensorinfo, thresholds):
    # Check bp details
    bpsval = float(sensorinfo["data"]["extras"]["sys"])
    bpdval = float(sensorinfo["data"]["extras"]["dia"])
    minbps = float(thresholds["bps_min"])
    maxbps = float(thresholds["bps_max"])
    minbpd = float(thresholds["bpd_min"])
    maxbpd = float(thresholds["bpd_max"])

    alerts = []
    if bpsval < minbps:
        alerts.append({"type": "bps", "message": "Low bps %s" % bpsval, "pid": sensorinfo["patientUUID"],
                       "timestamp": sensorinfo["timestamp"]})

    if bpsval > maxbps:
        alerts.append({"type": "bps", "message": "High bps %s" % bpsval, "pid": sensorinfo["patientUUID"],
                       "timestamp": sensorinfo["timestamp"]})

    if bpdval < minbpd:
        alerts.append({"type": "bpd", "message": "Low bpd %s" % bpdval, "pid": sensorinfo["patientUUID"],
                       "timestamp": sensorinfo["timestamp"]})

    if bpdval > maxbpd:
        alerts.append({"type": "bpd", "message": "High bpd %s" % bpdval, "pid": sensorinfo["patientUUID"],
                       "timestamp": sensorinfo["timestamp"]})

    return alerts

def validate_digitalscale_data(sensorinfo, thresholds):
    # Check digital scale details
    weightval = float(sensorinfo["weight"])
    weightmin = float(thresholds["weight_min"])
    weightmax = float(thresholds["weight_max"])

    alerts = []
    if weightval < weightmin:
        return [{"type": "bodyfatscale", "message": "Low weight %s" % weightval, "pid": sensorinfo["patientUUID"],
                 "timestamp": sensorinfo["timestamp"]}]

    if weightval > weightmax:
        return [{"type": "bodyfatscale", "message": "High weight %s" % weightval, "pid": sensorinfo["patientUUID"],
                 "timestamp": sensorinfo["timestamp"]}]

    return alerts

def validate_ecg_data(sensorinfo, thresholds):
    # Check ecg details
    hrval = float(sensorinfo["data"]["extras"]["HR"])
    rrval = float(sensorinfo["data"]["extras"]["RR"])
    minhr = float(thresholds["min_hr"])
    maxhr = float(thresholds["max_hr"])
    minrr = float(thresholds["min_rr"])
    maxrr = float(thresholds["max_rr"])

    alerts = []
    if hrval < minhr:
        return [{"type": "vv330", "message": "Low hr %s" % hrval, "pid": sensorinfo["patientUUID"],
                 "timestamp": sensorinfo["timestamp"]}]

    if hrval > maxhr:
        return [{"type": "vv330", "message": "High hr %s" % hrval, "pid": sensorinfo["patientUUID"],
                 "timestamp": sensorinfo["timestamp"]}]

    if rrval < minrr:
        return [{"type": "vv330", "message": "Low rr %s" % rrval, "pid": sensorinfo["patientUUID"],
                 "timestamp": sensorinfo["timestamp"]}]

    if rrval > maxrr:
        return [{"type": "vv330", "message": "High rr %s" % rrval, "pid": sensorinfo["patientUUID"],
                 "timestamp": sensorinfo["timestamp"]}]

    return alerts

def validate_spo2_data(sensorinfo, thresholds):
    # Check spo2 details
    spo2val = float(sensorinfo["spo2"])
    minspo2 = float(thresholds["min_spo2"])
    maxspo2 = float(thresholds["max_spo2"])

    alerts = []
    if spo2val < minspo2:
        return [{"type": "checkme_02", "message": "Low spo2 %s" % spo2val, "pid": sensorinfo["patientUUID"],
                 "timestamp": sensorinfo["timestamp"]}]

    if spo2val > maxspo2:
        return [{"type": "checkme_02", "message": "High spo2 %s" % spo2val, "pid": sensorinfo["patientUUID"],
                 "timestamp": sensorinfo["timestamp"]}]

    return alerts












