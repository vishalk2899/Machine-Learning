import numpy as np
import pandas as pd

Physics_score = [15,12,8,8,7,7,7,6,5,3]
History_score = [10,25,17,11,13,17,20,13,9,15]

x = pd.Series(Physics_score)
y = pd.Series(History_score)

r = x.cov(y)/(x.std()*y.std())

beta1 = (r*y.std())/x.std()

print("The slope of line of regressoin is:","%.3f"%beta1)


