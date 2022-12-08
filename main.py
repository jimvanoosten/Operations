import os 
import numpy as np 
import matplotlib.pyplot as plt
os.chdir('C:/Users/jimvanoosten/.spyder-py3/Operations')
cwd = os.getcwd()
print(cwd)

print("hello world")

x = np.random.randint(8, size=(4, 4))
print(x)

y = np.random.randint(6, size=(4, 4))
print(y)

plt.plot(x, y)