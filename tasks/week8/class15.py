import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# NP Necessary imports

df = pd.read_csv('/d/users/nikhil/ASTR5160/tasks/week8/result.csv')
# NP Reading in the data file

f = plt.figure()
f.set_figwidth(8)
f.set_figheight(5)
# NP Making the graph larger
ra, dec, g = df['ra'], df['dec'], df['g']
# NP Defining ra, dec, and g arrays
plt.scatter(ra, dec, color = 'red')
# NP Plotting the ra and dec of each object in the list
plt.xlabel('RA (deg)')
plt.ylabel('Dec (deg)')
plt.title('SDSS Objects within 2 arc mins of (300, -1)')
# NP Labeling the graph
plt.savefig('/d/www/nikhil/public_html/ASTR5160/SDSSobjs.png')
# NP Saving the figure, task 2 complete

f = plt.figure()
f.set_figwidth(8)
f.set_figheight(5)
# NP Making figure larger
index = np.linspace(np.max(g), np.min(g), 5)
# NP Generating a list of values between the min. and max. g mag.
for i in range(4):
    ii = (g < index[i]) & (g > index[i+1])
    plt.scatter(ra[ii],dec[ii], color = 'blue', s = (6)*(i+1)**2)
# NP Looping through this array to plot each point with a size according to its brightness
plt.xlabel('RA (deg)')
plt.ylabel('Dec (deg)')
plt.title('SDSS Objects within 2 arc mins of (300, -1) sized by g magnitude')
plt.savefig('/d/www/nikhil/public_html/ASTR5160/SDSSobjssized.png')
# NP Plotting each of the binned objects with sizes corresponding to their
# NP apparent magnitude
plt.xlabel('RA (deg)')
plt.ylabel('Dec (deg)')
plt.title('SDSS Objects within 2 arc mins of (300, -1) sized by g magnitude')
# NP Labeling the figure
plt.savefig('/d/www/nikhil/public_html/ASTR5160/SDSSobjssized.png')
# NP Saving the figure
