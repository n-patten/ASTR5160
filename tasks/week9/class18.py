import os
import numpy as np
import astropy.units as un
import astropy.units as un
import matplotlib.pyplot as plt
from astropy.table import Table
from astropy.coordinates import SkyCoord
from tasks.week8.class16 import whichsweep
# NP Necessary imports

stars = Table.read('/d/scratch/ASTR5160/week10/'
                   'stars-ra180-dec30-rad3.fits', memmap=True)
quasars = Table.read('/d/scratch/ASTR5160/week10/'
                   'qsos-ra180-dec30-rad3.fits', memmap=True)
files = os.listdir('/d/scratch/ASTR5160/data/legacysurvey/dr9/'
                   'south/sweep/9.0/')
sweeps = files[1:]
# NP Reading in the star and quasar files as well as the sweep directory

ras, decs = stars['RA'], stars['DEC']
raq, decq = quasars['RA'], quasars['DEC']
# NP Creating a list of RA's and Dec's for the stars/quasars

print(whichsweep(ras, decs, sweeps))
print(whichsweep(raq, decq, sweeps))
# NP Prints {'sweep-170p025-180p030.fits', 'sweep-180p030-190p035.fits',
# NP 'sweep-180p025-190p030.fits', 'sweep-170p030-180p035.fits'}
# NP 4 total sweep files arr needed

sweep1 = Table.read('/d/scratch/ASTR5160/data/legacysurvey/dr9/south/'
    'sweep/9.0/sweep-170p025-180p030.fits', memmap=True)
sweep2 = Table.read('/d/scratch/ASTR5160/data/legacysurvey/dr9/south/'
    'sweep/9.0/sweep-170p030-180p035.fits', memmap=True)
sweep3 = Table.read('/d/scratch/ASTR5160/data/legacysurvey/dr9/south/'
    'sweep/9.0/sweep-180p025-190p030.fits', memmap=True)
sweep4 = Table.read('/d/scratch/ASTR5160/data/legacysurvey/dr9/south/'
    'sweep/9.0/sweep-180p030-190p035.fits', memmap=True)
# NP Reading in contents of 4 sweep files
rasw1 = sweep1['RA'].value
rasw2 = sweep2['RA'].value
rasw3 = sweep3['RA'].value
rasw4 = sweep4['RA'].value
# NP Creating list of RA's for objects in sweep files
decsw1 = sweep1['DEC'].value
decsw2 = sweep2['DEC'].value
decsw3 = sweep3['DEC'].value
decsw4 = sweep4['DEC'].value
# NP Creating list of Dec's for objects in sweep files

csw1 = SkyCoord(rasw1*un.deg, decsw1*un.deg, frame='icrs')
csw2 = SkyCoord(rasw2*un.deg, decsw2*un.deg, frame='icrs')
csw3 = SkyCoord(rasw3*un.deg, decsw3*un.deg, frame='icrs')
csw4 = SkyCoord(rasw4*un.deg, decsw4*un.deg, frame='icrs')
# NP Creating skycoordinates for objects in sweep files
cs = SkyCoord(ras*un.deg, decs*un.deg, frame='icrs')
cq = SkyCoord(raq*un.deg, decq*un.deg, frame='icrs')
# NP Creating skycoordinates for stars and quasars from previous lists

idxc1s, idxcatalog1s, d2d1s, d3d1s = cs.search_around_sky(csw1, 0.0001*un.deg)
idxc2s, idxcatalog2s, d2d2s, d3d2s = cs.search_around_sky(csw2, 0.0001*un.deg)
idxc3s, idxcatalog3s, d2d3s, d3d3s = cs.search_around_sky(csw3, 0.0001*un.deg)
idxc4s, idxcatalog4s, d2d4s, d3d4s = cs.search_around_sky(csw4, 0.0001*un.deg)
idxc1q, idxcatalog1q, d2d1q, d3d1q = cq.search_around_sky(csw1, 0.0001*un.deg)
idxc2q, idxcatalog2q, d2d2q, d3d2q = cq.search_around_sky(csw2, 0.0001*un.deg)
idxc3q, idxcatalog3q, d2d3q, d3d3q = cq.search_around_sky(csw3, 0.0001*un.deg)
idxc4q, idxcatalog4q, d2d4q, d3d4q = cq.search_around_sky(csw4, 0.0001*un.deg)
# Matching stars and quasars to objects in sweep files

FLUX_G1s = sweep1['FLUX_G'][idxc1s].value/sweep1['MW_TRANSMISSION_G'][idxc1s].value
FLUX_G2s = sweep2['FLUX_G'][idxc2s].value/sweep2['MW_TRANSMISSION_G'][idxc2s].value
FLUX_G3s = sweep3['FLUX_G'][idxc3s].value/sweep3['MW_TRANSMISSION_G'][idxc3s].value
FLUX_G4s = sweep4['FLUX_G'][idxc4s].value/sweep4['MW_TRANSMISSION_G'][idxc4s].value
FLUX_G1q = sweep1['FLUX_G'][idxc1q].value/sweep1['MW_TRANSMISSION_G'][idxc1q].value
FLUX_G2q = sweep2['FLUX_G'][idxc2q].value/sweep2['MW_TRANSMISSION_G'][idxc2q].value
FLUX_G3q = sweep3['FLUX_G'][idxc3q].value/sweep3['MW_TRANSMISSION_G'][idxc3q].value
FLUX_G4q = sweep4['FLUX_G'][idxc4q].value/sweep4['MW_TRANSMISSION_G'][idxc4q].value
# Finding the g flux for each object in each sweep file

FLUX_W11s = sweep1['FLUX_W1'][idxc1s].value/sweep1['MW_TRANSMISSION_W1'][idxc1s].value
FLUX_W12s = sweep2['FLUX_W1'][idxc2s].value/sweep2['MW_TRANSMISSION_W1'][idxc2s].value
FLUX_W13s = sweep3['FLUX_W1'][idxc3s].value/sweep3['MW_TRANSMISSION_W1'][idxc3s].value
FLUX_W14s = sweep4['FLUX_W1'][idxc4s].value/sweep4['MW_TRANSMISSION_W1'][idxc4s].value
FLUX_W11q = sweep1['FLUX_W1'][idxc1q].value/sweep1['MW_TRANSMISSION_W1'][idxc1q].value
FLUX_W12q = sweep2['FLUX_W1'][idxc2q].value/sweep2['MW_TRANSMISSION_W1'][idxc2q].value
FLUX_W13q = sweep3['FLUX_W1'][idxc3q].value/sweep3['MW_TRANSMISSION_W1'][idxc3q].value
FLUX_W14q = sweep4['FLUX_W1'][idxc4q].value/sweep4['MW_TRANSMISSION_W1'][idxc4q].value
# Finding the W1 flux for each object in each sweep file

FLUX_W21s = sweep1['FLUX_W2'][idxc1s].value/sweep1['MW_TRANSMISSION_W2'][idxc1s].value
FLUX_W22s = sweep2['FLUX_W2'][idxc2s].value/sweep2['MW_TRANSMISSION_W2'][idxc2s].value
FLUX_W23s = sweep3['FLUX_W2'][idxc3s].value/sweep3['MW_TRANSMISSION_W2'][idxc3s].value
FLUX_W24s = sweep4['FLUX_W2'][idxc4s].value/sweep4['MW_TRANSMISSION_W2'][idxc4s].value
FLUX_W21q = sweep1['FLUX_W2'][idxc1q].value/sweep1['MW_TRANSMISSION_W2'][idxc1q].value
FLUX_W22q = sweep2['FLUX_W2'][idxc2q].value/sweep2['MW_TRANSMISSION_W2'][idxc2q].value
FLUX_W23q = sweep3['FLUX_W2'][idxc3q].value/sweep3['MW_TRANSMISSION_W2'][idxc3q].value
FLUX_W24q = sweep4['FLUX_W2'][idxc4q].value/sweep4['MW_TRANSMISSION_W2'][idxc4q].value
# Finding the W2 flux for each object in each sweep file

FLUX_R1s = sweep1['FLUX_R'][idxc1s].value/sweep1['MW_TRANSMISSION_R'][idxc1s].value
FLUX_R2s = sweep2['FLUX_R'][idxc2s].value/sweep2['MW_TRANSMISSION_R'][idxc2s].value
FLUX_R3s = sweep3['FLUX_R'][idxc3s].value/sweep3['MW_TRANSMISSION_R'][idxc3s].value
FLUX_R4s = sweep4['FLUX_R'][idxc4s].value/sweep4['MW_TRANSMISSION_R'][idxc4s].value
FLUX_R1q = sweep1['FLUX_R'][idxc1q].value/sweep1['MW_TRANSMISSION_R'][idxc1q].value
FLUX_R2q = sweep2['FLUX_R'][idxc2q].value/sweep2['MW_TRANSMISSION_R'][idxc2q].value
FLUX_R3q = sweep3['FLUX_R'][idxc3q].value/sweep3['MW_TRANSMISSION_R'][idxc3q].value
FLUX_R4q = sweep4['FLUX_R'][idxc4q].value/sweep4['MW_TRANSMISSION_R'][idxc4q].value
# Finding the r flux for each object in each sweep file

FLUX_Z1s = sweep1['FLUX_Z'][idxc1s].value/sweep1['MW_TRANSMISSION_Z'][idxc1s].value
FLUX_Z2s = sweep2['FLUX_Z'][idxc2s].value/sweep2['MW_TRANSMISSION_Z'][idxc2s].value
FLUX_Z3s = sweep3['FLUX_Z'][idxc3s].value/sweep3['MW_TRANSMISSION_Z'][idxc3s].value
FLUX_Z4s = sweep4['FLUX_Z'][idxc4s].value/sweep4['MW_TRANSMISSION_Z'][idxc4s].value
FLUX_Z1q = sweep1['FLUX_Z'][idxc1q].value/sweep1['MW_TRANSMISSION_Z'][idxc1q].value
FLUX_Z2q = sweep2['FLUX_Z'][idxc2q].value/sweep2['MW_TRANSMISSION_Z'][idxc2q].value
FLUX_Z3q = sweep3['FLUX_Z'][idxc3q].value/sweep3['MW_TRANSMISSION_Z'][idxc3q].value
FLUX_Z4q = sweep4['FLUX_Z'][idxc4q].value/sweep4['MW_TRANSMISSION_Z'][idxc4q].value
# Finding the z flux for each object in each sweep file

G1s = 22.5-np.log10(FLUX_G1s)
G2s = 22.5-np.log10(FLUX_G2s)
G3s = 22.5-np.log10(FLUX_G3s)
G4s = 22.5-np.log10(FLUX_G4s)
W11s = 22.5-np.log10(FLUX_W11s)
W12s = 22.5-np.log10(FLUX_W12s)
W13s = 22.5-np.log10(FLUX_W13s)
W14s = 22.5-np.log10(FLUX_W14s)
W21s = 22.5-np.log10(FLUX_W21s)
W22s = 22.5-np.log10(FLUX_W22s)
W23s = 22.5-np.log10(FLUX_W23s)
W24s = 22.5-np.log10(FLUX_W24s)
R1s = 22.5-np.log10(FLUX_R1s)
R2s = 22.5-np.log10(FLUX_R2s)
R3s = 22.5-np.log10(FLUX_R3s)
R4s = 22.5-np.log10(FLUX_R4s)
Z1s = 22.5-np.log10(FLUX_Z1s)
Z2s = 22.5-np.log10(FLUX_Z2s)
Z3s = 22.5-np.log10(FLUX_Z3s)
Z4s = 22.5-np.log10(FLUX_Z4s)
# NP Calculating the g, W1, W2, r and z magnitudes for each star for each sweep
# NP I got some warnings for null fluxes, but the programs procees.

G1q = 22.5-np.log10(FLUX_G1q)
G2q = 22.5-np.log10(FLUX_G2q)
G3q = 22.5-np.log10(FLUX_G3q)
G4q = 22.5-np.log10(FLUX_G4q)
W11q = 22.5-np.log10(FLUX_W11q)
W12q = 22.5-np.log10(FLUX_W12q)
W13q = 22.5-np.log10(FLUX_W13q)
W14q = 22.5-np.log10(FLUX_W14q)
W21q = 22.5-np.log10(FLUX_W21q)
W22q = 22.5-np.log10(FLUX_W22q)
W23q = 22.5-np.log10(FLUX_W23q)
W24q = 22.5-np.log10(FLUX_W24q)
R1q = 22.5-np.log10(FLUX_R1q)
R2q = 22.5-np.log10(FLUX_R2q)
R3q = 22.5-np.log10(FLUX_R3q)
R4q = 22.5-np.log10(FLUX_R4q)
Z1q = 22.5-np.log10(FLUX_Z1q)
Z2q = 22.5-np.log10(FLUX_Z2q)
Z3q = 22.5-np.log10(FLUX_Z3q)
Z4q = 22.5-np.log10(FLUX_Z4q)
# NP Calculating the g, W1, W2, r and z magnitudes for each quasar for each sweep
# NP I got some warnings for null fluxes, but the programs procees.

f = plt.figure()
f.set_figwidth(8)
f.set_figheight(5)
# NP Making plot larger
plt.scatter(G1s - Z1s, R1s - W11s, color = 'black', label = 'Star', s = 0.7)
plt.scatter(G2s - Z2s, R2s - W12s, color = 'black', s = 0.7)
plt.scatter(G3s - Z3s, R3s - W13s, color = 'black', s = 0.7)
plt.scatter(G4s - Z4s, R4s - W14s, color = 'black', s = 0.7)
# NP Plotting all star objects
plt.scatter(G1q - Z1q, R1q - W11q, color = 'red', label = 'Quasar', s = 0.7)
plt.scatter(G2q - Z2q, R2q - W12q, color = 'red', s = 0.7)
plt.scatter(G3q - Z3q, R3q - W13q, color = 'red', s = 0.7)
plt.scatter(G4q - Z4q, R4q - W14q, color = 'red', s = 0.7)
# NP Plotting all quasar objects
# NP I got some warnings for null fluxes, but the programs procees.
x = np.linspace(-0.5, 2.5, 100)
y = -.8 + 1.05*x
# NP Generating a fit by eye-balling
plt.plot(x,y, color = 'g', label = 'Approximate fit')
# NP Plotting fit
plt.legend()
# NP Generating legend for graph
plt.xlabel('g-z')
plt.ylabel('r-W1')
plt.title('Color-color plots for stars and quasars')
# NP Labeling figure
plt.savefig('/d/www/nikhil/public_html/ASTR5160/images/starsquasars.png')
# NP Saving plot

def isquasar(rminusW1, gminusz):
	if (rminusW1 > (1.05*gminusz -0.4)):
		return True
	else:
		return False
# NP Making plot to determine if an object is a quasar based on its color cuts.
# NP Anything within 0.4 of the line of best fit is considered a star.

print(isquasar(R1s[0]-W11s[0], G1s[0]-Z1s[0]))
# NP The function correctly identifies a star

print(isquasar(R1q[0]-W11q[0], G1q[0]-Z1q[0]))
# NP The function correctly identifies a quasar

