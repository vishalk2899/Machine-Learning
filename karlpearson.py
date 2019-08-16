import numpy as np
import pandas as pd

physics_marks = [15,12,8,8,7,7,7,6,5,3]
history_marks = [10,25,17,11,13,17,20,13,9,15]

x=pd.Series(physics_marks)
y=pd.Series(history_marks)

r=x.cov(y)/(x.std()*y.std())

print("Karl Pearson's Correlation Coefficient is: ",r)




