#!/usr/bin/env python

import time



for i in range(10):
    with open('./log.txt', 'a+') as log:
        log.write(f"{i=}\n")

    time.sleep(1)

    

