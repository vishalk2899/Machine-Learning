import numpy as np
import pandas as pd

x_mse= [15,12,8,8,7,7,7,6,5,3]
y_ese = [10,25,17,11,13,17,20,13,9,15]
y_predict=[]

x = pd.Series(x_mse)
y = pd.Series(y_ese)

r = x.cov(y)/(x.std()*y.std())

beta1 = (r*y.std())/x.std()
beta0 = y.mean()-beta1*x.mean()

mean_x = np.mean(x)

y_pred = beta1*x + beta0

y_predict.append(y_pred)


n=int(input("Number of History scores to be predited: "))

for i in range(n):
  i=int(input("Enter the Physics scores: "))
  x_mse.append(i)
  y_pred = beta1*i + beta0
  print('%.f'%y_pred)
  y_predict.append(y_pred) 
