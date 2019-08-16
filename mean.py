import numpy as np
import pandas as pd

a=[]
n=int(input("Enter the number of elements:"))

for i in range(0,n):
  element=int(input("Enter element"+str(i+1)+":"))
  a.append(element)
  
x=pd.Series(a)

mean=x.mean()
median=x.median()
mode=x.mode()
std=x.std()
lower_conf_interval = x.mean() - 1.96*x.std()
upper_conf_interval = x.mean() + 1.96*x.std()

print("Mean",mean)
print("Median",median)
print("Mode",mode)
print("Standard Deviation",std)
print("Lower_conf_interval",lower_conf_interval)
print("Upper_conf_interval",upper_conf_interval)

 
