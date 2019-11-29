from os import system
import threading
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
from datetime import datetime as dt
import time


topThread = -1

def extract_data(pid):
    system("top -H -p "+pid+" -d 0.1 -n 50 -b > migrations.txt")


def start(pid):
    topThread = threading.Thread(target=extract_data, args = (pid,)) 
    topThread.start()

def stop():
    topThread.stop()
