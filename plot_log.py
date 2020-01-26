#!/usr/bin/env python

import time
import datetime
from matplotlib import pyplot as plt

log_file = "/Users/pablo/Documents/tanklog.txt"

t = []
tank_level = []

def unix_time(text_time):
    day,month,year,t = text_time
    month_dict = {"Jan":1,"Feb":2}
    month_int = month_dict[month]
    t = t.split(":")
    return datetime.datetime(int(year),month_int,int(day),int(t[0]),int(t[1]),int(t[2])).timestamp()

trial_t = ["03 Jan 2020 08:41:46"]
trial_t = trial_t[0].split()
print(trial_t)
t_0 = unix_time(trial_t)
print(t_0)

with open(log_file,"r") as log:
    for index,line in enumerate(log):
        
        # if index % 2 == 0: continue
        if line == "\n": continue
        line = line.split(",")[1]
        #print(line.split())
        tank_level.append(line.split()[6][:-1])
        t.append(unix_time(line.split()[0:4])-t_0)
        #print(index)

#print(t,tank_level)

#show_last = 22000
#t,tank_level =t[-show_last:],tank_level[-show_last:]

t_final = t[-1]
t = [(x - t_final)/60 for x in t]
#tank_level = [5000*y for y in tank_level]
plt.plot(t,tank_level,"r-")
plt.show()
