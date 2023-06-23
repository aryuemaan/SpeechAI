#!/usr/bin/env python
# coding: utf-8

# In[2]:


##### Original plot of cosine for 40,000 points
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

############ generating the data  ##############
Xo_1 = np.linspace(-2, 4, num=300) ### generation of samples
Xo_2 = np.linspace(-2, 5, num=300) ### generation of samples

Xo_k1, Xo_k2 = np.meshgrid(Xo_1, Xo_2)

xxo1 = Xo_k1.ravel()
xxo2 = Xo_k2.ravel()

yo = np.cos((xxo1**2)/4 + (xxo2**2)/6)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.scatter(xxo2, xxo1, yo, color='black')
plt.show()   ############### plot of original data


# In[3]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

X_1 = np.linspace(-2, 4, num=15) ### generation of samples
X_2 = np.linspace(-2, 4, num=15) ### generation of samples

X_k1, X_k2 = np.meshgrid(X_1, X_2)

xx1 = X_k1.ravel()
xx2 = X_k2.ravel()

y = np.cos((xx1**2)/4 + (xx2**2)/2)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.scatter(xx2, xx1, y, color='black')
plt.show()   ############### plot of original data


# In[5]:


X = np.vstack([xx1, xx2]).T
print(np.shape(X))
Y = y.T

from sklearn.neural_network import MLPRegressor
from sklearn.datasets import make_regression
regr = MLPRegressor(hidden_layer_sizes=(20,15), activation = 'tanh', random_state=1, max_iter=5000).fit(X, Y)
# yc = regr.predict(X_test)
# print(yc)

############# Plotting for new points
Xt_1 = np.linspace(-7, 6, num=100) ### generation of samples
Xt_2 = np.linspace(-4, 6, num=200) ### generation of samples

Xt_k1, Xt_k2 = np.meshgrid(Xt_1, Xt_2)
xxt1 = Xt_k1.ravel()
xxt2 = Xt_k2.ravel()
X_test = np.vstack([xxt1, xxt2]).T
yc = regr.predict(X_test)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.scatter(xxt2, xxt1, yc, color='black')
plt.show()


# In[ ]:




