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
x = np.linspace(0, 10, 100)
m = np.linspace(2.5, 3.5, 11)
b = np.linspace(0, 10, 11)
for slope in m:
    for inter in b:
        yfit = slope*x +inter
        plt.plot(x, yfit, 'b', label = 'fit')
# NP Plotting several lines to fit the data with different slopes and
# NP intercepts
plt.plot(np.linspace(0.5, 0.5, 20), data['col1'], 'or')
plt.plot(np.linspace(1.5, 1.5, 20), data['col2'], 'or')
plt.plot(np.linspace(2.5, 2.5, 20), data['col3'], 'or')
plt.plot(np.linspace(3.5, 3.5, 20), data['col4'], 'or')
plt.plot(np.linspace(4.5, 4.5, 20), data['col5'], 'or')
plt.plot(np.linspace(5.5, 5.5, 20), data['col6'], 'or')
plt.plot(np.linspace(6.5, 6.5, 20), data['col7'], 'or')
plt.plot(np.linspace(7.5, 7.5, 20), data['col8'], 'or')
plt.plot(np.linspace(8.5, 8.5, 20), data['col9'], 'or')
plt.plot(np.linspace(9.5, 9.5, 20), data['col10'], 'or')
# NP Plotting data
plt.xlabel('x bin')
plt.ylabel('Measurement')
# NP Labeling axes
plt.show()
# Displaying graph

X2mb = []
for i in m:
    row = []
    for inter in b:
        X2 = (mean1-inter-i*(0.5))**2/var1\
            +(mean2-inter-i*(1.5))**2/var2\
            +(mean3-inter-i*(2.5))**2/var3\
            +(mean4-inter-i*(3.5))**2/var4\
            +(mean5-inter-i*(4.5))**2/var5\
            +(mean6-inter-i*(5.5))**2/var6\
            +(mean7-inter-i*(6.5))**2/var7\
            +(mean8-inter-i*(7.5))**2/var8\
            +(mean9-inter-i*(8.5))**2/var9\
            +(mean10-inter-i*(9.5))**2/var10
        print('m = ' +str(i) +', b = ' +str(inter) +', X^2: ' +str(X2))
        row.append(X2)
    X2mb.append(row)
# Calculating and printing chi^2 for all slope and intercept values

print('Best fit slope: ' +str(m[np.where(X2mb == np.min(X2mb))[0]].item()))
print('Best fit intercept: '+ str(b[np.where(X2mb == np.min(X2mb))[1]].item()))

# NP Displaying best fit parameters based on minimum chi squared
