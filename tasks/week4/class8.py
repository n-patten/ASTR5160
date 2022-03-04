import numpy as np
import matplotlib.pyplot as plt
import math as m
from astropy import units as u
from astropy.coordinates import SkyCoord #Necessary imports

ra, dec = [263.75, 306.2495833]*u.degree, [-17.9, 10.1]*u.degree
c1,c2 = SkyCoord(ra, dec, frame = 'icrs') #Defining two coordinates
cartesian = c.cartesian #Converting to cartesian
dot = np.dot(cartesian.x[0], cartesian.x[1])+np.dot(cartesian.y[0],cartesian.y[1])+np.dot(cartesian.z[0],cartesian.z[1])
degree = m.acos(dot)*180/np.pi #Calulating Degrees from dot product
print(degree) #Printing result, degree = 50.4
print(c1.separation(c2)) #Verifying result, separation = 50.4
#Results verified, task 1 complete.

f = plt.figure()
f.set_figwidth(8)
f.set_figheight(5) #Making graph larger
ra1 = (np.random.random(100)+2)*15*u.degree
ra2 = (np.random.random(100)+2)*15*u.degree
dec1 = ((np.random.random(100)*4)-2)*u.degree
dec2 = ((np.random.random(100)*4)-2)*u.degree #Generating sets of random points
plt.plot(ra1,dec1,'r^', label = 'Set 1')
plt.plot(ra2, dec2, 'db', label = 'Set 2') #Plotting sets of points
plt.legend() #Creating legend
plt.savefig('/d/www/nikhil/public_html/randompoints.png') #Saving figure
#Task 2 complete

c1 = SkyCoord(ra1, dec1, frame = 'icrs') #Creating SkyCoords for points in set
c2 = SkyCoord(ra2, dec2, frame = 'icrs')
id1, id2, d1, d2 = c2.search_around_sky(c1, (10/60)*u.degree) #Searching
f = plt.figure()
f.set_figwidth(8)
f.set_figheight(5) #Making plot large
plt.plot(ra1, dec1,'r^', label = 'Set 1')
plt.plot(ra2, dec2, 'db', label = 'Set 2')
plt.plot(ra1[id1], dec1[id1], 'og', label = 'Close Points')
plt.plot(ra2[id2], dec2[id2], 'og') #Plotting sets of data and close points
plt.legend() #Creating legend
plt.savefig('/d/users/nikhil/public_html/randompointswithmatch.png') #Saving
#Task 3 complete
