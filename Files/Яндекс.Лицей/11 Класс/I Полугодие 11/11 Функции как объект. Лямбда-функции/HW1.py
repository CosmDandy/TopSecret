def same_by(haracteristic, objects):
    return len(set(map(haracteristic, objects))) == 1 if objects else True
