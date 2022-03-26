import numpy as np
from astropy.coordinates import SkyCoord
from astropy import units as u
# NP necessary imports

def boundedbyra(r, flip = False):
    '''returns an array of the spherical cap bounded by 5 h ra
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Inputs:
    r- float. Right ascension in hours
    flip- boolean. Whether to flip the height of the spherical cap.
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Outputs:
    array. [x,y,z, 1-h]. The 4 vector of the cap bounded in ra.'''
    ra = (r*15)+90
    dec=0
    c = SkyCoord(ra,dec,unit="deg")
    if flip:
        size = -1
    else:
        size = 1
    array = [c.cartesian.x.value, c.cartesian.y.value, c.cartesian.z.value, size]
    return array
#print(boundedbyra())
# NP Prints [-0.97, 0.26, 0, 1]
# NP Task 1 complete

def boundedbydec(d, flip = False):
    '''returns the 4 vector of the spherical cap bounded by +36 degrees dec
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Inputs:
    d- float. Declination in degrees
    flip- boolean. Whether to flip the height of the spherical cap.
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Outputs:
    array. [x,y,z, 1-h]. The 4 vector of the cap bounded in ra.'''
    ra = 0
    dec = 90
    c = SkyCoord(ra,dec,unit = "deg")
    if flip:
        size = -1*(1-np.sin(d*np.pi/180))
    else:
        size = 1-np.sin(d*np.pi/180)
    array = [c.cartesian.x.value, c.cartesian.y.value, c.cartesian.z.value, size]
    return array
#print(boundedbydec())
# NP Prints [0,0,1,0.4122]
# NP Task 2 complete

def boundedbyraanddec(r,d,t, flip = False):
    '''returns the 4 vector of the spherical cap bounded by 5h ra and +36 degrees dec
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Inputs:
    r- float. Right ascension in hours
    d- float. Declination in degrees
    t- float. The angular size of the spherical cap in degrees.
    flip- boolean. Whether to flip the height of the spherical cap.
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Outputs:
    array. [x,y,z, 1-h]. The 4 vector of the cap bounded in ra.'''
    ra = r*15
    dec = d
    c = SkyCoord(ra,dec,unit = "deg")
    if flip:
        size = -1*(1-np.cos(t*np.pi/180))
    else:
        size = 1-np.cos(t*np.pi/180)
    array = [c.cartesian.x.value, c.cartesian.y.value, c.cartesian.z.value, size]
    return array
#print(boundedbyraanddec())
# NP Prints [0.21, 0.78, 0.59, 0.00015]
# NP Task 3 complete
