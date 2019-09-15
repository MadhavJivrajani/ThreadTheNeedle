import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
from datetime import datetime as dt

f = open("data_2ms.txt")
data = f.readlines()
data.insert(0,"\n")
data = [data[i] for i in range(4,len(data),5)]

data = [i.strip() for i in data]


core_id = [int(i[-1]) for i in data]
time = [i.split()[-3] for i in data]


print("Core 0: ",core_id.count(0))
print("Core 1: ",core_id.count(1))
print("Core 2: ",core_id.count(2))
print("Core 3: ",core_id.count(3))


df = {"core_id":pd.Series(np.array(core_id)),"time":pd.Series(np.array(time))}
df = pd.DataFrame(df)

freq_change = {}
for i in range(1,len(df)):
    if df['core_id'][i-1]!=df['core_id'][i]:
        freq_change[(df['time'][i-1],df['time'][i])] = [df['core_id'][i-1],df['core_id'][i]]

dt_time = [dt.strptime(i,"%M:%S.%f") for i in time] #time differences.

deltas = {} #dictionary with key containing the time taken for each migration and the value as a list containing core IDs
            #of the core pre-switch and post-switch. 
k=0

for i in freq_change:
    deltas[(k,(dt.strptime(i[1],"%M:%S.%f")-dt.strptime(i[0],"%M:%S.%f")).microseconds)] = freq_change[i]
    k+=1


final_times = np.array([i[1] for i in deltas]) #array contatining time taken for each migration. 

cores_cummulative = []
for i in list(deltas.values()):
    cores_cummulative.append(i[0])
    cores_cummulative.append(i[1])
for i in cores_cummulative:
    print(i,end=",")

