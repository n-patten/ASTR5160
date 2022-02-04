import random
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit #NP necessary imports

def line(m,b):
    x = np.random.uniform(low = 0, high = 10, size = (10,)) #NP generating 10 points
    y = m*x +b #NP recovering appropiate y-values
    scatter = np.random.normal(y, 0.5) #NP scattering
    return x, scatter, 0.5 #NP returning desired parameters, Task 1 complete

x, y, error = line(1,1) #NP using previously defined function to acquire scatter to fit a line to
def func(x, m, b):#NP defining a function to be used by curve_fit
    return m*x +b
popt, pcov = curve_fit(func, x, y)#NP fitting scatter to a line of best fit
print(popt)#NP printing slope and y-intercept of the fit, Task 2 complete

plt.errorbar(x, y, yerr = error, fmt = '.', label = 'data')#NP plotting scatter points
xnew = np.linspace(0,10,100)#NP generating array of x-coordinates in the range of 1-10
plt.plot(xnew, func(xnew, *popt), '--r',  label = 'fit') #NP plotting the fit
plt.plot(xnew, 1*xnew +1, 'g', label = 'original line') #NP plotting the original line
plt.xlabel('x-axis') #NP labelling axes
plt.ylabel('y-axis')
plt.legend() #NP Creating a legend to distinguish different lines, Task 3 complete

plt.savefig('partone.png') #NP Saving picture of graph
#NP defining x and y bounds aren't necessary because Python already determines appropiate bounds

def complete(m,b): #NP defining a new function that will do all of the above tasks in one stop, inputting only m and b and saving a picture of the resultant graph with all of the data plotted.
    x = np.random.uniform(low = 0, high = 10, size = (10,))
    y = m*x +b
    scatter = np.random.normal(y1, 0.5)
    def func(x, m, b):
        return m*x +b
    popt, pcov = curve_fit(func, x, scatter)
    plt.errorbar(x, scatter, yerr = 0.5, fmt = '.', label = 'data')
    xnew = linspace(0, 10, 100)
    plt.plot(xnew, func(xnew, *popt), '--r', label = 'fit')
    plt.plot(xnew, m*xnew +b, 'g', label = 'original line')
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.legend()
    plt.savefig('complete.png')
