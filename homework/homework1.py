# ADM this code uses a range of ideas and approaches from four different
# ADM students in the University of Wyoming's (2022) ASTR-5160 course.
from astropy import units as u
from astropy.coordinates import SkyCoord, EarthLocation, AltAz
from astropy.time import Time
from astropy.table import Table
import argparse
import numpy as np
from calendar import monthrange

# ADM just hard-coding the offset between UTC and MST.
utc_off = 7*u.hour


def get_coords(filename):
     """
     Convert a .txt file containing quasars in hmsdms to a SkyCoord object.

     Parameters
     ----------
     filename : Name of quasar file.

     Returns
     -------
     SkyCoord object with quasar RAs and Decs.
     list of quasar names.
     """
     # ADM read in the file.
     quasars = Table.read(filename, format='ascii.no_header')

     # ADM use list comprehensions to determine the coordinates
     ra = ["{}h{}m{}s".format(q[0:2], q[2:4], q[4:9]) for q in quasars["col1"]]
     dec = ["{}d{}m{}s".format(q[9:12], q[12:14], q[14:18]) for q in quasars["col1"]]
     coords = SkyCoord(ra, dec, frame='icrs')
   
     return coords, quasars['col1']


def get_times(month):
     """
     Create astropy.time object at 6AM UTC for each day of a month.
  
     Parameters
     ----------
     month : Interger onth of the year [1-12].

     Returns
     -------
     list of observation times (6:00 UTC).
     """
     # ADM monthrange returns the number of days in a given month.
     days = np.arange(monthrange(2022, month)[1]) + 1

     # ADM create a time object at 6AM UTC or 11PM MST.
     t = ['2022-' + str(month) + '-' + str(d) + ' 23:00:00' for d in days]
     times = Time(t, format='iso') + utc_off

     return times


def get_airmass(filename, month):
     """
     Lowest-airmass object in a file that can be observed on each day in a month.

     Parameters
     ----------
     filename : Name of quasar file as a string.
     month : Month of the year as an integer.

     Returns
     -------
     list of observation timestamps.
     list of hmsdms coordinates of lowest airmass quasar.
     list of right ascension of lowest-airmass quasar
     list of declination of lowest-airmass quasar.
     list of airmass of lowest-airmass quasar.
     """
     kpno = EarthLocation.of_site("kpno")

     # ADM get needed coordinates from file.
     coords, quasars = get_coords(filename)
     # ADM get needed time objects for passed month.
     times = get_times(month)

     # ADM all of the required quantities without appending to anything.
     airmasses = [coords.transform_to(AltAz(obstime=t, location=kpno)).secz for t in times]
     ii = np.array([np.argmin(np.where(am > 0, am, 1e16)) for am in airmasses])
     airmass = np.array([np.min(np.where(am > 0, am, 1e16)) for am in airmasses])

     return times, quasars[ii], coords[ii].ra.value, coords[ii].dec.value, airmass


if __name__ == "__main__": # AMC if quasar_airmass_homework1.py is main program
     # ADM hardcode the filename.
     filename = "/d/scratch/ASTR5160/week4/HW1quasarfile.txt"

     description = ("Return the lowest-airmass observation of any quasar listed" 
                    "in the file".format(filename))

     parser = argparse.ArgumentParser(description=description)
     parser.add_argument('month', type=int)
     args = parser.parse_args()

     # ADM call the function to make the table and print the result
     time, coords, ra, dec, airmass = get_airmass(filename, args.month)
     names = ['Date (MST)', 'Quasar Coordinates', 'RA (o)', 'Dec (o)', 'Airmass']
     t = Table([time - utc_off, coords, ra, dec, airmass], names=names)

     print(t)

