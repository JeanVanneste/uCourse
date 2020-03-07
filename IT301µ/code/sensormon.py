# sensormon.py
# Author: Sébastien Combéfis
# Version: March 7, 2020

import argparse
import json
import time
import urllib.request


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', help='URL where to listen to captured data', default='http://127.0.0.1:1880/api/measures')
    parser.add_argument('--interval', help='Data checking interval', type=int, default=5)
    args = parser.parse_args()

    req = urllib.request.Request(args.url, method='GET', headers={'Accept': 'application/json'})

    print('Starting monitor...')
    while True:
        try:
            with urllib.request.urlopen(req) as f:
                res = f.read().decode('utf-8')
                if f.status != 200:
                    raise Exception('Invalid status: ' + f.status)
                print('Data retrieved:', json.loads(res))
        except Exception as e:
            print('Error:', e)
        time.sleep(args.interval)
