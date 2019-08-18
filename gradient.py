import numpy as np

m=0
c=0
lr=0.0001
epoch=10000

x1,y1 = np.loadtxt("aimarks2017.txt",delimiter=',',unpack=True)
mse_marks=pd.Series(x1)
ese_marks=pd.Series(y1)


n=len(mse_marks)

for i in range(epoch):
  y_pred = mse_marks*m + c
  dm=(-2/n)*sum(mse_marks*(ese_marks-y_pred))
  de=(-2/n)*sum(ese_marks-y_pred)
  m=m-lr*dm
  c=c-lr*de
print(m,c)
