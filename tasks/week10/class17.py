import numpy as np
import astropy.units as un
from astropy.table import Table
from astropy.coordinates import SkyCoord
# NP Necessary imports

V = 15.256
BminusV = 0.873
UminusB = 0.320
VminusR = 0.505
RminusI = 0.511
# NP Inputting information about PG1633+099A
B = BminusV + V
U = UminusB + B
R = V - VminusR
I = R - RminusI
# NP Calculating each UBVRI magnitude from the information given
print('___U___B___V___R___I___')
print(str(U)+' '+str(B)+' '+str(V)
      +' '+str(R)+' '+str(I))
# NP Prints 16.449 16.129 15.256 14.751 14.24

uminusg = 1.28*(U-B)   + 1.14
gminusr = 1.09*(B-V)   - 0.23
rminusi = 0.98*(R-I) - 0.22
rminusz = 1.69*(R-I) - 0.42
g = V + 0.64*(B-V) - 0.13
r = V - 0.46*(B-V) + 0.11
u = uminusg + g
i = r - rminusi
z = r - rminusz
# NP Calculating SDSS ugriz magnitudes from the UBVRI magnitudes
print('___u___g___r___i__z____')
print(str(u)+' '+str(g)+' '+str(r)
      +' '+str(i)+' '+str(z))
# NP Prints 17.23432 15.68472 16.96442 14.68364 14.52083
# NP These calculated SDSS ugriz magnitudes were very close to the
# NP magnitudes listed in the SDSS navigator
# NP SDSS gives 17.30 15.70 15.19 14.71 14.55
# NP Task 1 complete

table = Table.read('/d/scratch/ASTR5160/data/legacysurvey/'
                   'dr9/south/sweep/9.0/sweep-240p005-'
                   '250p010.fits', memmap=True)
# NP Creating a table with the legacy data in the sweep that contains
# NP PG1633+099A

c1 = SkyCoord([248.8583333]*un.deg, [9.798055556]*un.deg, frame='icrs')
# NP Creating a coordinate for PG1633+099A
ra = table['RA'].value
dec = table['DEC'].value
# NP Creating a list of RA's and Dec's from the table
c2 = SkyCoord(ra*un.deg, dec*un.deg, frame='icrs')
idxc, idxcatalog, d2d, d3d = c1.search_around_sky(c2, 0.001*un.deg)
# NP Finding all objects in the catalog that are within 0.001 degrees
# NP of PG1633+099A. This returns one index which points to PG1633+099A
# NP in the sweep file.
FLUX_G = table['FLUX_G'][idxc].value
FLUX_R = table['FLUX_R'][idxc].value
FLUX_Z = table['FLUX_Z'][idxc].value
# NP Pulling the fluxes for PG1633+099A from the sweep file

gs = 22.5 - 2.5*np.log10(FLUX_G)
rs = 22.5 - 2.5*np.log10(FLUX_R)
zs = 22.5 - 2.5*np.log10(FLUX_Z)
# NP Calculating the magnitudes
print('___g___r___z___')
print(str(gs)+' '+str(rs)+' '+str(zs))
# NP Prints 15.580078 14.901785 14.517736
# NP These grz magnitudes are really close to the expected values
# NP SDSS gives 15.70 15.19 14.55

FLUX_W1 = table['FLUX_W1'][idxc].value
FLUX_W2 = table['FLUX_W2'][idxc].value
FLUX_W3 = table['FLUX_W3'][idxc].value
FLUX_W4 = table['FLUX_W4'][idxc].value
print('___W4FLUX___')
print(FLUX_W4)
# NP Creating W flux values from the table for our star
# NP W4 is negative

w1s = 22.5 - 2.5*np.log10(FLUX_W1)
w2s = 22.5 - 2.5*np.log10(FLUX_W2)
w3s = 22.5 - 2.5*np.log10(FLUX_W3)
w4s = 22.5 - 2.5*np.log10(FLUX_W4)
# NP Calculating magnitudes
print('___w1___w2___w3___w4___')
print(str(w1s)+' '+str(w2s)+' '+str(w3s)+str(w4s))
# NP Prints 15.547712 16.20843 18.522753 nan
# NP Since W4 flux was negative, there is non calculation of magnitude in W4.
# NP I suppose this means that the W4 flux of this star was too low to be
# NP detected by this survey. After background subtraction, this flux
# NP flux turned out to be negative, meaning that it was not detected in this
# NP survey.
# NP Task 2 complete.
