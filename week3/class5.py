import numpy as np
import matplotlib.pyplot as plt
from astropy.coordinates import SkyCoord#imports
c = SkyCoord('01h00m00s', '+41d30m00s')#defining coordinates in ra dec
c.representation_type = "cartesian"#changing to cartesian
print(c)#printing cartesian results
x = np.cos(15*np.pi/180)*np.cos(41.5*np.pi/180)#doing x y and z conversions
y = np.sin(15*np.pi/180)*np.cos(41.5*np.pi/180)
z = np.sin(41.5*np.pi)
coords = [x,y,z]
print(coords)#printing results, they're the same, Task 1 complete

center = SkyCoord('0d00m00s', '0d00m00s', frame = 'galactic')#galactic center
center_fk5 = center.transform_to('fk5')#transforming to ra dec
print(center_fk5)#printing conversion, task 2 complete
#center in the top right corner of saggitarius

ra = [90,120,150,180,210,240,270,300,330,360,30,60]#defining list of ra in degrees that are at the meridian at midnight on the winer solstice over 12 months
zenith = SkyCoord(ra,40, unit = 'deg')#defining coordinates of zenith
plt.plot(zenith.galactic.l, zenith.galactic.b)#making plot of galactic coordinates of object at zenith
plt.xlabel('Galactic Longitude')
plt.ylabel('Galactic Latitude')#various labels
plt.title('Galactic Longitude and Latitude at zenith over Laramie from Winter Solstice throughout the course of a year')
plt.savefig('plot.png')#save figure
