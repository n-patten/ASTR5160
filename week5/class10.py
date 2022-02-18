import numpy as np
from astropy.coordinates import SkyCoord
from astropy import units as u
# NP necessary imports

def boundedbyra():
    '''returns an array of the spherical cap bounded by 5 h ra'''
    ra = (5*15)+90
    dec=0
    c = SkyCoord(ra,dec,unit="deg")
    array = [c.cartesian.x, c.cartesian.y, c.cartesian.z, 1]
    return array
print(boundedbyra())
# NP Prints [-0.97, 0.26, 0, 1]
# NP Task 1 complete

def boundedbydec():
    '''returns the 4 vector of the spherical cap bounded by +36 degrees dec'''
    ra = 0
    dec = 90
    c = SkyCoord(ra,dec,unit = "deg")
    array = [c.cartesian.x, c.cartesian.y, c.cartesian.z, 1-np.sin(36*np.pi/180)]
    return array
print(boundedbydec())
# NP Prints [0,0,1,0.4122]
# NP Task 2 complete

def boundedbyraanddec():
    '''returns the 4 vector of the spherical cap bounded by 5h ra and +36 degrees dec'''
    ra = 5*15
    dec = 36
    c = SkyCoord(ra,dec,unit = "deg")
    array = [c.cartesian.x, c.cartesian.y, c.cartesian.z, 1-np.cos(1*np.pi/180)]
    return array
print(boundedbyraanddec())
# NP Prints [0.21, 0.78, 0.59, 0.00015]
# NP Task 3 complete
