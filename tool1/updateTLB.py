from os import system
import threading
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
from datetime import datetime as dt
import time

extract_thread = -1
display_thread = -1
check = 0

def extract_data(pid):

    system("sudo perf stat -o "+str(pid)+".txt -e dTLB-load-misses,iTLB-load-misses,cpu-migrations,context-switches,page-faults -I 1000 -p "+str(pid))

def process_data(pid):

    try:
        system("rm "+pid+".txt")
    except:
        pass 

    import time
    global check

    time.sleep(1)
    
    while(check):


        try:
            data = pd.read_csv(str(pid)+".txt", delimiter="\t")
            data = [data.values.tolist()[i][0].split() for i in range(data.shape[0])]
            data = data[1:]

            datadTLB = [i for i in data if len(i)==3 and i[-1]=='dTLB-load-misses']
            dataiTLB = [i for i in data if len(i)==3 and i[-1]=='iTLB-load-misses']
            datacpu = [i for i in data if len(i)==3 and i[-1]=='cpu-migrations']
            datacontext = [i for i in data if len(i)==3 and i[-1]=='context-switches']
            datafaults = [i for i in data if len(i)==3 and i[-1]=='page-faults']

            datadTLB = np.array(datadTLB)
            print(datadTLB.shape)
            datadTLB = datadTLB[:, :2].tolist()
            datadTLB = [ [float(j.replace(',','')) for j in i] for i in datadTLB]

            dataiTLB = np.array(dataiTLB)
            dataiTLB = dataiTLB[:, :2].tolist()
            dataiTLB = [ [float(j.replace(',','')) for j in i] for i in dataiTLB]

            display_data(np.array(datadTLB), np.array(dataiTLB), datacpu, datacontext, datafaults)

        except Exception as e: 
            print(e)


def display_data(dtlb, itlb, datacpu, datacontext, datafaults):
    
    plt.plot(dtlb[:, 0],dtlb[:, 1] , color="blue")
    plt.plot(itlb[:, 0],itlb[:, 1], color="red")
    plt.title("CPU Migrations = " + datacpu[-1][1] + "\n Context Switches = " + datacontext[-1][1] + "\n Page Faults = " + datafaults[-1][1] + "\n", loc = "center", pad=-30, fontdict={'verticalalignment': 'baseline'})
    plt.legend(["dTLB Misses", "iTLB Misses"], loc = "upper right")
    plt.xlabel("Time elapsed in seconds",fontsize=13)
    plt.ylabel("dTLB / iTLB Misses",fontsize=13)

    plt.draw()
    plt.pause(0.1)

def start(pid):

    global check, extract_thread, display_thread
    check = 1


    extract_thread = threading.Thread(target=extract_data, args = (pid,)) 
    display_thread = threading.Thread(target=process_data, args = (pid,))

    extract_thread.start()
    display_thread.start()

    

def stop():
    global check, extract_thread, display_thread
    check = 0
    plt.close()
    extract_thread.join()
    display_thread.join()