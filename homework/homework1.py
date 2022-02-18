import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from astropy.coordinates import SkyCoord, EarthLocation, AltAz
from astropy import units as u
from astropy.table import Table
from astropy.time import Time # NP necessary imports

def airmass(m):
    '''Takes a number, m, which corresponds to a month in the year 2022 and returns a table of 
        quasars observable from Kitt Peak Observatory sorted by airmass.'''
    df = pd.read_csv('/d/scratch/ASTR5160/week4/HW1quasarfile.txt', header = None, names=['Coordinates'])
    t = Table.from_pandas(df) # NP creating an astropy Table of the quasars
    ra = []
    dec = []
    for i in t:
        ra.append(i.__str__()[38:40]+'h'+i.__str__()[40:42]+'m'+i.__str__()[42:47]+'s')
        dec.append(i.__str__()[47:50]+'d'+i.__str__()[50:52]+'m'+i.__str__()[52:56]+'s')
        # NP running through quasar list and creating tables of their RA's and decs
    c = SkyCoord(ra,dec,frame = 'icrs') # NP creating SkyCoords for each quasar
    month = m # Defining month from user input
    days = 0 # NP Number of days in the month, will be defined later
    utcoffset = 6*u.hour # NP MST correction
    times = [] # NP Lists that will all be utilized in the program, instantiating them now
    altaz =[]
    airmass = []
    legitairmasses = []
    indices = []
    quasarindex = []
    sortedquasarlist = []
    sortedra = []
    sorteddec = []
    sortedtimes = []
    sorteddates = []
    kpno = EarthLocation.of_site('Kitt Peak National Observatory') # NP Defining KPNO
    if (month == 2):
        days = 28
    elif (month == 9 or month == 4 or month == 6 or month == 11):
        days = 30
    else:
        days = 31 # NP Defining the number of days depending on which month was inputted
    for i in range(days):
        times.append(Time('2022-'+str(month)+'-'+str(i+1)+' 23:00:00')-utcoffset)
        # NP Creating a list of times corresponding to all the days in the month
    for i in times:
        altaz.append(c.transform_to(AltAz(obstime=i,location=kpno)))
        # NP Finding Alt and Az for each quasar in the last for every day in the month
    for i in altaz:
        airmass.append(i.secz) # NP calculating airmass
    for i in airmass:
        for b in i:
            if(b > 1):
                legitairmasses.append(b) # NP Finding all airmasses that are above the horizon
    sortedairmasses = np.sort(legitairmasses) # NP Sorting the airmasses
    for i in sortedairmasses:
        indices.append(np.where(airmass == i))
        # NP Crearing a list of indices that point to a particular quasar
    for i in indices:
        sortedtimes.append(i[0])
        quasarindex.append(i[1])
        # NP Creating a sorted list of quasars and times based on their airmasses
    for i in quasarindex:
        sortedquasarlist.append(t[i].__str__()[38:56])
        sortedra.append(c[i].ra.degree)
        sorteddec.append(c[i].dec.degree)
    for i in sortedtimes:
        sorteddates.append('2022-'+str(month)+'-'+str(int(i+1))+' 23:00:00')
        # NP Creating a sorted list of dates that each quasar is observable
    t = Table([sorteddates, sortedquasarlist, sortedra, sorteddec, sortedairmasses],
         names = ('Date','Quasar Coordinates (hms.ss deg arcmin ")', 'RA (deg)', 'Dec (deg)', 'Airmass'))
    # NP Defining a table that contains all of the sorted quasars and their associated information
    return t
