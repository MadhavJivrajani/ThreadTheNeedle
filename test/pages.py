from os import system
import threading

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
from datetime import datetime as dt

import time

def extract_data(pid, interval):
    system("sudo perf stat -o "+str(pid)+".txt -e dTLB-load-misses,iTLB-load-misses -I 1000 -p 31512 -a sleep "+interval)

def process_data(pid, interval):
    data = []
    time = []
    itlb_misses = []
    dtlb_misses = []
    time_dtlb = []
    time_itlb = []
    #while(1):
    extract_data(pid, interval)
    perf = open(str(pid)+".txt","r")
    perf.seek(0)
    data_pid = perf.readlines()
    data_pid = [i.strip() for i in data_pid]
    data_pid = data_pid[2:]

    time_pid = [float(data_pid[i].split()[0]) for i in range(1,len(data_pid))]

    dtlb_misses_pid = [int("".join(data_pid[i].split()[1].split(","))) for i in range(1, len(data_pid), 2)]
    itlb_misses_pid = [int("".join(data_pid[i].split()[1].split(","))) for i in range(2, len(data_pid), 2)]

    time_dtlb_pid = [time_pid[i] for i in range(0,len(time_pid),2)]
    time_itlb_pid = [time_pid[i] for i in range(1,len(time_pid),2)]

    #FIX FOR <not counted> CASE
    for i in data_pid[1:]:
        data.append(i)

    for i in time_pid:
        time.append(i)

    for i in dtlb_misses_pid:
        dtlb_misses.append(i)

    for i in itlb_misses_pid:
        itlb_misses.append(i)

    for i in time_dtlb_pid:
        time_dtlb.append(i)

    for i in time_itlb_pid:
        time_itlb.append(i)

    perf.close()

    display_data(time_dtlb, dtlb_misses)

def display_data(x_data, y_data):

	plt.plot(np.array(x_data), np.array(y_data), color="blue")
	plt.xlabel("Time elapsed in seconds",fontsize=13)
	plt.ylabel("dTLB Misses",fontsize=13)
	plt.show()

	#plt.pause(0.1)

if __name__ == '__main__':

    pid = input("Enter Process ID: ")

    interval = input("Over how long do you want to measure it: ")

    process_data(pid, interval)

    # extract_thread = threading.Thread(target=extract_data, args = (pid,)) 
    # display_thread = threading.Thread(target=process_data, args = (pid,))

    # extract_thread.start()
    # time.sleep(4)
    # display_thread.start()

    # extract_thread.join()
    # display_thread.join()

    print("DONE")   
           




