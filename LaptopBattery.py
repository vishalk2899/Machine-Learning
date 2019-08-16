import pandas as pd
import numpy as np

x1,y1 = np.loadtxt("trainingdata.txt",delimiter=',',unpack=True)
x=pd.Series(x1)
y=pd.Series(y1)

r=x.cov(y)/(x.std()*y.std())

beta1 = (r*y.std())/x.std()
beta0 = y.mean()- beta1*x.mean()

b=float(input())
time= beta0 - beta1*b
print(time)
