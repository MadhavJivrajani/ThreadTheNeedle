from os import system
import threading

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
from datetime import datetime as dt

import time

def extract_data(pid):
    system("sudo perf stat -o "+str(pid)+".txt -e dTLB-load-misses,iTLB-load-misses -I 1000 -p "+str(pid))

def process_data(pid):

    data = []
    time = []
    itlb_misses = []
    dtlb_misses = []
    time_dtlb = []
    time_itlb = []
    
    while(1):
        
        data = pd.read_csv(str(pid)+".txt", delimiter="\t")
        print("here")
        data = [data.values.tolist()[i][0].split() for i in range(data.shape[0])]
        data = data[1:]
        data = [i for i in data if len(i)==3 and i[-1]=='dTLB-load-misses']
        data = np.array(data)
        data = data[:, :2].tolist()
        data = [ [float(j.replace(',','')) for j in i] for i in data]
        
        print(data)
        
        data = np.array(data)
        
        time_dtlb = data[:, 0].tolist()
        dtlb_misses = data[:, 1].tolist()

        display_data(time_dtlb, dtlb_misses)

def display_data(x_data, y_data):

	plt.plot(np.array(x_data), np.array(y_data), color="blue")
	plt.xlabel("Time elapsed in seconds",fontsize=13)
	plt.ylabel("dTLB Misses",fontsize=13)
	
	plt.show()
	


if __name__ == '__main__':

    pid = input("Enter Process ID: ")

    extract_thread = threading.Thread(target=extract_data, args = (pid,)) 
    display_thread = threading.Thread(target=process_data, args = (pid,))

    extract_thread.start()
    display_thread.start()

    extract_thread.join()
    display_thread.join()

    print("DONE")   
           
