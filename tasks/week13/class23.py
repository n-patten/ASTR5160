import numpy as np
import matplotlib.pyplot as plt
from astropy.table import Table
# NP Necessary imports

data = Table.read('/d/scratch/ASTR5160/week13/line.data', format = 'ascii')
# NP Reading in data
print(data)
# NP Printing data

mean1 = np.mean(data['col1'])
var1 = np.var(data['col1'])
print('mean: ' +str(mean1))
print('var: ' +str(var1))

mean2 = np.mean(data['col2'])
var2 = np.var(data['col2'])
print('mean: ' +str(mean2))
print('var: ' +str(var2))

mean3 = np.mean(data['col3'])
var3 = np.var(data['col3'])
print('mean: ' +str(mean3))
print('var: ' +str(var3))

mean4 = np.mean(data['col4'])
var4 = np.var(data['col4'])
print('mean: ' +str(mean4))
print('var: ' +str(var4))

mean5 = np.mean(data['col5'])
var5 = np.var(data['col5'])
print('mean: ' +str(mean5))
print('var: ' +str(var5))

mean6 = np.mean(data['col6'])
var6 = np.var(data['col6'])
print('mean: ' +str(mean6))
print('var: ' +str(var6))

mean7 = np.mean(data['col7'])
var7 = np.var(data['col7'])
print('mean: ' +str(mean7))
print('var: ' +str(var7))

mean8 = np.mean(data['col8'])
var8 = np.var(data['col8'])
print('mean: ' +str(mean8))
print('var: ' +str(var8))

mean9 = np.mean(data['col9'])
var9 = np.var(data['col9'])
print('mean: ' +str(mean9))
print('var: ' +str(var9))

mean10 = np.mean(data['col10'])
var10 = np.var(data['col10'])
print('mean: ' +str(mean10))
print('var: ' +str(var10))
# NP Defining all the means and variances

f = plt.figure()
f.set_figwidth(8)
f.set_figheight(6)
# NP Making figure larger
plt.scatter(np.linspace(0.5, 0.5, 20), data['col1'], color = 'red', label = 'data')
plt.scatter(np.linspace(1.5, 1.5, 20), data['col2'], color = 'red')
plt.scatter(np.linspace(2.5, 2.5, 20), data['col3'], color = 'red')
plt.scatter(np.linspace(3.5, 3.5, 20), data['col4'], color = 'red')
plt.scatter(np.linspace(4.5, 4.5, 20), data['col5'], color = 'red')
plt.scatter(np.linspace(5.5, 5.5, 20), data['col6'], color = 'red')
plt.scatter(np.linspace(6.5, 6.5, 20), data['col7'], color = 'red')
plt.scatter(np.linspace(7.5, 7.5, 20), data['col8'], color = 'red')
plt.scatter(np.linspace(8.5, 8.5, 20), data['col9'], color = 'red')
plt.scatter(np.linspace(9.5, 9.5, 20), data['col10'], color = 'red')
# NP Scattering data at midpoint for each bin
x = np.linspace(0, 10, 100)
yfit = 5 + 3*x
# NP Defining my estimation of the line of best fit
plt.plot(x, yfit, 'b', label = 'fit')
# NP Plotting fitted liune
plt.legend()
# NP Creating legend
plt.xlabel('x bin')
plt.ylabel('Measurement')
# NP Labelin axes

X2 = (mean1-5-3*(0.5))**2/var1\
    +(mean2-5-3*(1.5))**2/var2\
    +(mean3-5-3*(2.5))**2/var3\
    +(mean4-5-3*(3.5))**2/var4\
    +(mean5-5-3*(4.5))**2/var5\
    +(mean6-5-3*(5.5))**2/var6\
    +(mean7-5-3*(6.5))**2/var7\
    +(mean8-5-3*(7.5))**2/var8\
    +(mean9-5-3*(8.5))**2/var9\
    +(mean10-5-3*(9.5))**2/var10
print('X^2: ' +str(X2))
# Calculating and printing chi^2

plt.show()
# NP Showing plot
