# sensorsim.py
# Author: Sébastien Combéfis
# Version: March 7, 2020

import argparse
import json
import random
import time
import urllib.request

MIN_TEMP = -10
MAX_TEMP = 35
MIN_HUM = 35
MAX_HUM = 65
MAX_TANK = 50

def clamp(value, min, max):
    """Clamp a value between two bounds and round it to one decimal place."""
    if value < min:
        return min
    if value > max:
        return max
    return round(value, 1)

def getData():
    """Build message corresponding to the data collected from the sensors and update the data."""
    result = {'valid': random.randint(0, 10) != 0, 'data': data}
    if result['valid']:
        dtemp = random.randint(-10, 10) / 10
        data['temperature'] = clamp(data['temperature'] + dtemp, MIN_TEMP, MAX_TEMP)

        dhum = random.randint(-5, 5) / 10
        data['humidity'] = clamp(data['humidity'] + dhum, MIN_HUM, MAX_HUM)

        data['tank'] -= random.randint(0, 5)
        if data['tank'] < 0:
            data['tank'] = MAX_TANK
    else:
        del result['data']
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', help='URL where to send captured data', default='http://127.0.0.1:1880/api/measures')
    parser.add_argument('--interval', help='Data sending interval', type=int, default=5)
    args = parser.parse_args()

    data = {
        'temperature': 17.5,
        'humidity': 40.3,
        'tank': MAX_TANK
    }
    req = urllib.request.Request(args.url, method='POST', headers={'Content-Type': 'application/json'})

    print('Starting simulator...')
    while True:
        req.data = json.dumps(getData()).encode('utf8')
        try:
            with urllib.request.urlopen(req) as f:
                res = f.read().decode('utf-8')
                if f.status != 200:
                    raise Exception('Invalid status: ' + f.status)
                if res != '':
                    raise Exception('Invalid response body: ' + res)
            print('Data sent:', req.data)
        except Exception as e:
            print('Error:', e)
        time.sleep(args.interval)
