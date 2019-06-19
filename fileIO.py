
import os
import time


files = os.listdir("Python-Drill")

now = os.getcwd()

for file in files:
    modification_time = os.path.getmtime(file)
        

local_time = time.ctime(modification_time)
print("Last modification time: {}".format(local_time))








