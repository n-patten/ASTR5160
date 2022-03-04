import numpy as np#necessary imports
from astropy.coordinates import SkyCoord,EarthLocation, AltAz
from astropy.time import Time
import astropy.units as u

c = SkyCoord('00h42m30s', '+41d12m51s')#some arbitrary coordinates in hms and deg arcmin arcsec
print(c.ra.degree)#printing the converted coordinates in degrees
print(c.dec.degree)#Task 1 complete

nt = Time.now()#current time
print(nt.jd)#current Julian Date
print(nt.mjd)#current modified Julian date, task 2 complete

dates = nt+[0,1,2,3,4,5] #creating an array of days starting from the current date up to 5 days later
for i in dates:
    print(i) #printing the next 5 days from todays date, task 3 complete

WIRO = EarthLocation(lat='+41d05m49s', lon='-105d58m33s', height='2943m')#defining WIRO's location, task 4 complete

utcoffset = -6*u.hour#MST
time1 = Time('2022-1-27 23:00:00') -utcoffset#defining times and correcting for time zons
time2 = Time9'2022-2-27 23:00:00') -utcoffset
times = [time1, time2]
object = SkyCoord('12h00m00s', '+30d00m00s')#creating object at RA and dec
objaltaz = object.transform_to(AltAz(obstime = times, location = WIRO)) #calculating alt and az
print(objaltaz.alt.degree)#printing results
print(objaltaz.secz)#printing airmasses at this time
