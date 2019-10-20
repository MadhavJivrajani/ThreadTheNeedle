from os import system
import threading

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
from datetime import datetime as dt

import time

global info
info = {}

def extract_data(pid,refreshRate):

    system("top -H -p "+pid+" -d "+refreshRate+" -b | grep "+pid+" >> "+pid+refreshRate+".txt")

def process_data(pid,refreshRate):

    global info

    while (1):

        f = open(pid+refreshRate+".txt")
        data = f.readlines()
        data = [i.strip() for i in data[:len(data)-1]]
        time = [i.split()[-2] for i in data]
        cores = [int(i.split()[-1]) for i in data]
        df = {"cores":pd.Series(np.array(cores)),"time":pd.Series(np.array(time))}
        df = pd.DataFrame(df)
        freq_change = {}
        start = df['time'][0]
        for i in range(1,len(df)):
            if df['cores'][i-1]!=df['cores'][i]:
                freq_change[(start,df['time'][i])] = df['cores'][i-1]
                start = df['time'][i]
        start_time = [dt.strptime(i[0],"%M:%S.%f") for i in list(freq_change.keys())]
        end_time = [dt.strptime(i[1],"%M:%S.%f") for i in list(freq_change.keys())]
        deltas = [(end_time[i]-start_time[i]).microseconds for i in range(len(start_time))]
        core_time = {"core":pd.Series(np.array(list(freq_change.values()))),"time":pd.Series(np.array(deltas))}
        core_time = pd.DataFrame(core_time)
        core_time.tail()
        def to_milli(example):
            return example/1000
        core_time['time'] = core_time['time'].apply(to_milli)
        
        print(core_time)

        for i in range(4):
            if i in info:
                for j in range(len(core_time)):
                    if i==core_time['core'][j]:
                        info[i] += core_time['time'][j]
            else:
                info[i] = 0              	

        for j in range(len(core_time)):
            for i in range(4):
                if i==core_time['core'][j]:
                    info[i] += core_time['time'][j]
        print(info)
        display_data(pid,refreshRate)

def display_data(pid,refreshRate):

	global info

	x = np.arange(len(info.keys()))
	plt.bar(x, np.array(list(info.values())), color = 'blue')
	plt.xlabel("Core IDs",fontsize=10)
	plt.ylabel("Count in milliseconds",fontsize=10)
	plt.draw()

	plt.pause(0.1)


if __name__ == '__main__':

    pid = input("Enter Process ID: ")
    refreshRate = input("Enter Refresh Rate: ")

    extract_thread = threading.Thread(target=extract_data, args = (pid,refreshRate)) 
    display_thread = threading.Thread(target=process_data, args = (pid,refreshRate))

    extract_thread.start()
    time.sleep(4)
    display_thread.start()

    extract_thread.join()
    display_thread.join()

    print("DONE")
