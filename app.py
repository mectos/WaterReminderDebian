#!/usr/bin/python3

import subprocess
import time

while True:
    subprocess.call(args=['notify-send',
                          'DRINK WATER',
                          'Drink from the god damn bottle'])
    minutes = 5
    notify_time = 60 * minutes

    time.sleep(notify_time)
