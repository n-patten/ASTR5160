import os
import numpy as np
import astropy.units as u
from astropy.table import Table, vstack
from astropy.coordinates import SkyCoord
from tasks.week8.class16 import whichsweep
# NP Necessary imports

files = os.listdir('/d/scratch/ASTR5160/data/legacysurvey/dr9/'
	'south/sweep/9.0/')
sweeps = files[1:]
# NP Defining path to sweep files

print(whichsweep(np.array(188.53667), np.array(21.04572), sweeps))
# NP Prints:
# NP {'sweep-180p020-190p025.fits'}
# NP This sweep file contains the object at (a,d) = (188.5.., 21.0..)

sweep = Table.read('/d/scratch/ASTR5160/data/legacysurvey/dr9/south/'
    	'sweep/9.0/sweep-180p020-190p025.fits', memmap=True)
# NP Reading in the sweep file

ras = sweep['RA'].value
decs = sweep['DEC'].value
# NP Making a list of ra's and dec's for objects in the sweep file
c = SkyCoord(ras*u.deg, decs*u.deg, frame = 'icrs')
ct = SkyCoord([188.53667*u.deg], [21.04572*u.deg], frame = 'icrs')
# Making SkyCoords for these objs and the target ra and dec
idxc, idxcatalog, d2d, d3d = c.search_around_sky(ct, 0.00001*u.deg)
# NP Using search_around_sky to find the object at (a,d) = (188.., 21..)

print(sweep[idxcatalog]['TYPE'])
# NP Prints:
# NP EXP
# NP This object is an exponential galaxy according to sweep documentation
# NP Task 1 complete

print('ALLMASK_G: '+str(int(sweep[idxcatalog]['ALLMASK_G'].value))
      	+'\nALLMASK_R: '+str(int(sweep[idxcatalog]['ALLMASK_R'].value))
      	+'\nALLMASK_Z: '+str(int(sweep[idxcatalog]['ALLMASK_Z'].value)))
# NP Prints:
# NP ALLMASK_G: 2
# NP ALLMASK_R: 2
# NP ALLMASK_Z: 2
# NP According to the bitmasks page, all exposures are saturated
# NP According to the Legacy Viewer, object is saturated. Searching SIMBAD
# NP reveals this object is a possible blazar; a head-on quasar.
# NP Task 2 complete

print(whichsweep(np.array(180), np.array(30), sweeps))
# NP Finding which sweep files I need to read in.
# NP Prints:
# NP {'sweep-180p025-190p030.fits', 'sweep-180p030-190p035.fits',
# NP 'sweep-170p025-180p030.fits', 'sweep-170p030-180p035.fits'}

names = list(whichsweep(np.array(180), np.array(30), sweeps))
sweep2 = Table.read('/d/scratch/ASTR5160/data/legacysurvey/dr9/south/'
        'sweep/9.0/' + names[0], memmap=True)
for i in range(len(names)-1):
	s1 = Table.read('/d/scratch/ASTR5160/data/legacysurvey/dr9/south/'
		'sweep/9.0/' + names[i+1], memmap=True)
    	sweep2 = vstack([sweep2, s1])
# NP Reading all the sweep files into one table using a for-loop

ras2 = sweep2['RA'].value
decs2 = sweep2['DEC'].value
# NP Generating lists of ra and dec for each of the objects in the sweep files
racenter, deccenter = 180*u.degree, 30*u.degree
ct2 = SkyCoord([racenter], [deccenter], frame = 'icrs')
c2 = SkyCoord(ras2*u.degree, decs2*u.degree, frame = 'icrs')
idxc2, idxcatalog2, d2d2, d3d2 = c2.search_around_sky(ct2, 3*u.deg)
# NP Finding all of the objects in the sweep files that are within 3 degrees of
# NP (a,d) = (180, 30)

FLUX_R = sweep2[idxcatalog2]['FLUX_R']#/sweep2[idxcatalog2]['MW_TRANSMISSION_R']
r = 22.5 -2.5*np.log10(FLUX_R)
# NP Calculating r magnitude. Initially, I used the MW_TRANSMISSION_R but
# NP later commented that out because it wasn't necessary

ii = (sweep2[idxcatalog2]['TYPE'] == 'PSF') & (r < 20)
psfobjs = sweep2[idxcatalog2][ii]
# NP Limiting our results by PSF objects brighter than r = 20

print(len(psfobjs))
# NP Prints:
# NP 39655
# NP There are 39655 objects in the sweeps that are within 3 degrees of
# NP (a,d) = (180, 30) that are PSF objects and brighter than r = 20

qsos = Table.read('/d/scratch/ASTR5160/week10/'
	'qsos-ra180-dec30-rad3.fits', memmap=True)
# NP Reading in quasars

raqso, decqso = qsos['RA'], qsos['DEC']
ras2 = psfobjs['RA'].value
decs2 = psfobjs['DEC'].value
# NP Defining the ra's and dec's of the quasars and psfobjs
quasars = SkyCoord(raqso*u.degree, decqso*u.degree, frame = 'icrs')
cpsfobjs = SkyCoord(ras2*u.degree, decs2*u.degree, frame = 'icrs')
idxc3, idxcatalog3, d2d3, d3d3 = cpsfobjs.search_around_sky(quasars, 0.0001*u.deg)
# NP Using search_around_sky to coordinate match each object in both lists.

qsos = quasars[idxc3]
# NP Defining quasars from matched list indices
print(len(qsos))
# NP Prints:
# NP 275
# NP There are 275 quasars that are within 3 degrees of (a,d) = (180, 30)
# NP that are PSF objects and are brighter than r = 20
# NP Task 3 complete
