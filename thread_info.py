from os import system
import threading
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
from datetime import datetime as dt

import time

def extract_data(pid):
    system("top -H -p "+pid+" -d 0.5 -b >> migrations.txt")

def get_hops(tid):
    top_thread = open("migrations.txt")
    thread_data = top_thread.readlines()

    thread_data = [i.strip() for i in thread_data]

    thread_data = [i for i in thread_data if len(i) > 0]

    thread_data = [i for i in thread_data if i.split()[0]!="PID"]

    time = [i.split()[3] for i in thread_data]
    cores = [int(i.split()[-1]) for i in thread_data]
    ids = [int(i.split()[0]) for i in thread_data]

    df = {"cores":pd.Series(np.array(cores)),"time":pd.Series(np.array(time)),"ids":pd.Series(np.array(ids))}   
    df = pd.DataFrame(df)

    freq_change = {}
    start = df['time'][0]
    for i in range(1,len(df)):
        if df['cores'][i-1]!=df['cores'][i]:
            freq_change[(start,df['time'][i])] = df['cores'][i-1]
            start = df['time'][i]

    return len(set(df[df["ids"]==int(tid)]["cores"].values))

def hops_per_tid(pid):
    system("ps -To pid,tid,pcpu,tty,time,comm -p "+pid+" > thread.txt")
    data = open("thread.txt")
    data = data.readlines()
    data = [i.strip() for i in data]
    cols = data[0].split()
    data = data[1:]
    data[0].split()
    tids = [i.split()[1] for i in data]
    pcpu = [i.split()[2] for i in data]
    comm = [" ".join(i.split()[5:]) for i in data]
    print(tids)
    print(pcpu)
    print(comm)
    hops = []
    for tid in tids:
        hops.append(get_hops(tid))

    print("HOPS:\n",hops)
    
    df = {"TID":pd.Series(np.array(tids)), "PCPU":pd.Series(np.array(pcpu)), "COMMAND":pd.Series(np.array(comm)), "HOPS":pd.Series(np.array(hops))}
    df = pd.DataFrame(df)
    df.sort_values(by=['HOPS'], inplace=True)

    print(df)



if __name__ == '__main__':

    pid = input("Enter Process ID: ")
    # refreshRate = input("Enter Refresh Rate: ")

    run_top = threading.Thread(target=extract_data, args = (pid,)) 
    hop_per_tid = threading.Thread(target=hops_per_tid, args = (pid,))

    run_top.start()
    time.sleep(2)
    hop_per_tid.start()

    run_top.join()
    hop_per_tid.join()

    print("DONE")
