import numpy as np
import matplotlib.pyplot as plt
from numpy.random import random #Necessary imports

ra = 2*np.pi*(random(10000)-0.5) #Generating 10.000 random RA points from -pi to pi
dec = np.arcsin(1.-random(10000)*2.) #Generating 10.000 random Dec points from -pi to pi
plt.plot(ra,dec,'.') #Plotting results
plt.savefig('/d/www/nikhil/public_html/cartesiansphere.png') #Saving graph
#Graph has a concentration of points near the equator of the sphere as predicted. In cartesian coordinates, the poles of a sphere are stretched as seen in the plot. Task 1 complete.

fig = plt.figure()
ax = fig.add_subplot(111, projection = "aitoff")
ax.scatter(ra, dec, marker = 'o', color = 'g', s = 0.7, alpha = 0.5) #Creating Aitoff Projection
xlab = ['14h', '16h', '18h', '20h', '22h', '0h', '2h', '4h', '6h', '8h', '10h'] #Creating x-label of hours instead of degrees
ax.set_xticklabels(xlab, weight = 800)
ax.grid(color = 'b', linestyle = 'dashed', linewidth = 2) #Creating a thick, blue, dashed axis
plt.savefig('/d/www/nikhil/public_html/cartesiansphere.png') #Saving plot
#
#Creating Lambert projection
fig = plt.figure()
ax = fig.add_subplot(111, projection = "lambert")
ax.scatter(ra, dec, marker = 'o', color = 'g', s = 0.7, alpha = 0.5)
xlab = ['14h', '16h', '18h', '20h', '22h', '0h', '2h', '4h', '6h', '8h', '10h']
ax.set_xticklabels(xlab, weight = 800)
ax.grid(color = 'b', linestyle = 'dashed', linewidth = 2)
plt.savefig('/d/www/nikhil/public_html/lambert.png') #Saving Plot
#Lambert and Aitoff plots created, Task 2 finished.
