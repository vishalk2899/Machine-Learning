import numpy as np
import pandas as pd

x_mse = [15,22,16,18,30]
y_ese = [55,68,62,65,72]

x = pd.Series(x_mse)
y = pd.Series(y_ese)

r = x.cov(y)/(x.std()*y.std())

beta1 = (r*y.std())/x.std()
beta0 = y.mean()-beta1*x.mean()
sum_xy = sum((x-x.mean())*(y-y.mean()))
std_x=np.std(x)


a = (x-x.mean())
b = y-y.mean()
c=a*a
d=b*b
e=a*b
f=c.sum()
g=d.sum()
h=f/5
i=g/5
j=np.std(x)


print("Coeff. of slope:",beta1)
print("Intercept:",beta0)
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)
print(j)
print(r)





