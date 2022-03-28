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
# NP Generating a list of magnitudes from max to min g mag.
print(index)
for i in range(4):
    ii = (g < index[i]) & (g > index[i+1])
    plt.scatter(ra[ii],dec[ii], color = 'blue', s = (6)*(i+1)**2)
# NP Looping through the list of g magnitudes and plotting them according
# NP to size
plt.xlabel('RA (deg)')
plt.ylabel('Dec (deg)')
plt.title('SDSS Objects within 2 arc mins of (300, -1) sized by g magnitude')
# NP Labeling figure
plt.savefig('/d/www/nikhil/public_html/ASTR5160/images/SDSSobjssized.png')
# NP Saving figure
