import numpy as np
import matplotlib.pyplot as plt
import healpy as hp
from numpy.random import random # NP necessary imports

ra = 360.*(random(1000000))
dec=(180/np.pi)*np.arcsin(1.-random(1000000)*2.) # NP making 1000000 different points
# NP Task 1 complete

nside1 = hp.ang2pix(1, ra, dec, lonlat=True)
print(nside1)

print(hp.nside2pixarea(1))
# NP Area of the nside = 1 is 1/12 of the sphere, exactly what it should be
# NP Task 1 complete

print(np.histogram(nside1,12)) # NP Each nside has roughly the same number of points

plt.hist(nside1, bins = 12)
plt.savefig('/d/www/nikhil/public_html/ASTR5160/images/histogram.png')
# NP histogram is flat, ra and dec evenly distributed about sphere
# NP Task 3 complete
