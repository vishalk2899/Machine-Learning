import numpy as np
import pandas as pd

m=0
c=0
lr=0.0001
epoch=10000

dataset = pd.read_csv('aimarks2017.csv')
mse_marks = dataset.iloc[:, :-1].values
ese_marks = dataset.iloc[:, -1].values

n=len(mse_marks)

for i in range(epoch):
  y_pred = mse_marks*m + c
  dm=(-2/n)*sum(mse_marks*(ese_marks-y_pred))
  de=(-2/n)*sum(ese_marks-y_pred)
  m=m-lr*dm
  c=c-lr*de
print(m,c)
