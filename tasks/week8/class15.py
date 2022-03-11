import pandas as pd
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

i = (g <= 18)
i2 = (g > 18) & (g <= 19)
i3 = (g > 19) & (g <= 20)
i4 = (g > 20) & (g <= 21)
i5 = (g > 21) & (g <= 22)
i6 = (g > 22) & (g <= 23)
i7 = (g > 23) & (g <= 24)
i8 = (g > 24) & (g <= 25)
i9 = (g > 25)
# NP Binning at different magnitude between 18 and 25
f = plt.figure()
f.set_figwidth(8)
f.set_figheight(5)
# NP Making the figure larger
import numpy as np
f = plt.figure()
f.set_figwidth(8)
f.set_figheight(5)
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
