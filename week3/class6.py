import numpy as np
import matplotlib.pyplot as plt
import sfdmap
from astropy.coordinates import SkyCoord #necessary imports

ra1, dec1 = '16h39m43.92s', '+40d47m42s'
ra2, dec2 = '15h46m14.88s', '+2d26m24s' #coordinates of both quasars
ugriz1 = np.array([18.82, 18.81, 18.73, 18.82, 18.90])
ugriz2 = np.array([19.37, 19.1, 18.79, 18.73, 18.63)] #magnitude of both quasars
plt.plot(ugriz1[2]-ugriz1[3], ugriz1[1]-ugriz1[2], '.b', label = 'Quasar 1')
plt.plot(ugriz2[2]-ugriz2[3], ugriz2[1]-ugriz2[2], '.r', label = 'Quasar 2')
plt.legend()
plt.xlabel('r-i')
plt.ylabel('g-r')
plt.savefig('uncorrected.png') #plotting g-r vs. r-i
#colors don't agree, one is redder than the other, likely due to extinction
c1 = SkyCoord(ra1, dec1).galactic
c2 = SkyCoord(ra2, dec2).galactic
dustdir = '/d/scratch/ASTR5160/data/dust/v0_1/maps'
m = sfdmap.SFDMap(dustdir, scaling = 1)
ebv1 = m.ebv(c1.l.value, c1.b.value, frame = 'galactic')
ebv2 = m.ebv(c2.l.value, c2.b.value, frame = 'galactic')
A1 = ebv1*ugriz1
A2 = ebv2*ugriz2
m1 = ugriz1 - A1
m2 = ugriz2 - A2
plt.plot(m1[2]-m1[3], m1[1]-m1[2], '.b', label = 'Quasar 1')
plt.plot(m2[2]-m2[3]m m2[1]-m2[2], '.r', label = 'Quasar 2')
plt.xlabel('r-i')
plt.ylabel('g-r')
plt.legend()
plt.savefig('corrected.png')
#The colors agree slightly better when corrected. Task 1 complete

ragrid1 = np.linspace(231.6, 241.6, 100)
decgrid1 = np.linspace(-2.6, 7.4, 100)
ragrid2 = np.linspace(240.4, 253.4, 100)
decgrid2 = np.linspace(35.8, 45.8, 100)

mesh1 = np.meshgrid(ragrid1, decgrid1)
mesh2 = np.meshgrid(ragrid2, decgrid2)
#Mesh grids created, Task 2 complete
