#Package->libraby-> collection of modules 
#Module->python file conatin function etc..

import os
import shutil

print(os.getcwd())

#write python script to find disk usage
total,use,free = shutil.disk_usage("/") #get value in byte
print("total space is ",total // 2**30," In GB") # converted byte to GB
print("use space is ",use // 2**30)
print("free space is ",free // 2**30)

#Fstring
print(f"free space is : {free // 2**30} is GB") #added dynamic value inside text
