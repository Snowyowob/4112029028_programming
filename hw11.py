import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#1
a = np.array([1,2,3,4,5,6])
a_reshape = a.reshape((3,2))
print(a_reshape)
b = np.array([1,3,5,7,2,4,6,8])
for n in range(8):
    for i in range(7):
        if b[i] > b[i+1]:
            tb = b[i]
            b[i] = b[i+1]
            b[i+1] = tb
print(f"Max={b[7]},Min={b[0]}")
#2
grammer_dict = {'grammer':["python","java","go",np.NaN,"python","c","c++"],'score':[1.0,np.NaN,np.NaN,4.0,5.0,7.0,8.0]}
df = pd.DataFrame(grammer_dict)
df.columns = ['grammer','popularity']
df['popularity'].mean()
#3
x = np.linspace(0,10,100)
y = np.sin(x)
plt.plot(x,y)
plt.title('line chart')
plt.show()

data = np.random.randn(1000)
y = np.random.randn(1000)
plt.bar(data,y)
plt.ylim(0,4)
plt.show()
