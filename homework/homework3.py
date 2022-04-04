import pymangle
import matplotlib.pyplot as plt
import numpy as np
from numpy.random import random
from astropy.table import Table
from astropy.coordinates import SkyCoord
from tasks.week05.class10 import boundedbyra
from tasks.week05.class10 import boundedbydec
from tasks.week05.class10 import boundedbyraanddec
from homework.homework2 import area
# NP Necessary imports

def makeply(name, caps, weight = 1):
	'''A function designed to create a ply file given weights and caps
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	Inputs
	name- str. The name of the ply file.
	caps- array. A list of caps for each polygon
	weights- float. Default 1. A weight corresponding to the weight of the polygon
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	Outputs
	null
	Write ply file to directory /d/users/nikhil/ASTR5160/homework/'''
	f = open(r'/d/users/nikhil/ASTR5160/homework/' +name +'.ply', 'w')
	# NP Creating file
	f.write(str(len(caps))+' polygons\n')
	# NP Specifying how many polygons there are based on inputs
	for i in range(len(caps)):
		f.write('polygon ' +str(i+1) +' ( ' +str(len(caps[i])) 
			+' caps, ' +str(weight)
		        +' weight, 0 pixel, 0 str):\n')
		for x in caps[i]:
			f.write('\t'+str(x[0])+' ' +str(x[1]) +' '
				+str(x[2]) +' ' +str(x[3])+'\n')
		# NP Putting caps for each polygon
	f.close()
	# NP Saving file

def makerect(ramin, ramax, dmin, dmax):
	'''A function to generate the lat-lon rectangle from ra and dec bounds
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	Inputs
	ramin- float. The minimum right ascension of the lat-lon rectangle in hours
	ramax- float. The maximum right ascension of the lat-lon rectangle in hours
	dmin- float. The minimum declination of the lat-lon rectangle in degrees
	dmax- float. The maximum declination of the lat-lon rectangle in degrees
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	Outputs
	array- List of spherical caps'''
	cap1 = boundedbyra(ramin)
	cap2 = boundedbyra(ramax, True)
	cap3 = boundedbydec(dmin)
	cap4 = boundedbydec(dmax, True)
	# NP Creating a list of spherical caps correspinding to a lat-
	# NP lon rectangle. ramax and dmax require flip=True
	return [cap1, cap2, cap3, cap4]

if (__name__ == '__main__'):
	latloncaps = makerect(10.25, 11.25, 30, 40)
	# NP Making rectangle coverage for the survey
	makeply('rectangle', [latloncaps])
	# NP Making a ply file for the lat-lon rectangle
	rect = pymangle.Mangle('/d/users/nikhil/ASTR5160/homework/rectangle.ply')
	# NP Making mask from the lat-lon rectangle
	ra = 15.*(random(1000000)) +(10.25*15)
	dec= 10.*(random(1000000)) +30
	# NP Generating random points throughout the lat-lon rectangle
	# NP 1000000 random points were needed for a precision of 0.5 deg^2
	spec1 = np.append(latloncaps, [boundedbyraanddec(155/15, 34, 2)], axis = 0)
	spec2 = np.append(latloncaps, [boundedbyraanddec(159/15, 36, 2)], axis = 0)
	spec3 = np.append(latloncaps, [boundedbyraanddec(163/15, 34, 2)], axis = 0)
	spec4 = np.append(latloncaps, [boundedbyraanddec(167/15, 36, 2)], axis = 0)
	# NP Generating 4 polygons for the 4 spectroscopic regions
	allspecs = [spec1, spec2, spec3, spec4]
	# NP Combining them into one set of spherical cap list
	makeply('observation', allspecs)
	# NP Making polygons for each spectroscopic mask
	mobs = pymangle.Mangle('/d/users/nikhil/ASTR5160/homework/observation.ply')
	# NP Creating mask for each spectroscopic region
	inside = mobs.contains(ra, dec)
	# NP List of ra's/dec's inside the spectroscopic mask
	rectarea = area(10.25*15, 11.25*15, 30, 40)
	# NP Caculating the area of the entire lat-lon rectangle
	specarea = (len(ra[inside])/len(ra))*rectarea
	# NP Calculating the area of the masks using the rectangle area and points
	print(specarea)

	# NP I know it wasn't required, but I made a plot of the masks and the lat-
	# NP lon rectangle for the spectroscopic regions and the survey to help me
	# NP visualize the problem.
	f = plt.figure()
	f.set_figwidth(8)
	f.set_figheight(5)
	# NP Making figure larger
	ra1 = 15.*(random(100000)) +(10.25*15)
	dec1 = 10.*(random(100000)) +30
	# NP Creating new ra's and dec's inside the lat-lon rectangle because
	# NP the original list of ra's and dec's took too long to plot on a
	# NP scatter plot.
	inside = mobs.contains(ra1, dec1)
	# NP Finding points that are inside the masks
	plt.scatter(ra1[inside], dec1[inside], color = 'blue', s = 0.5,
		label = 'Spectroscopic plates')
	# NP Plotting the points inside the spectroscopic regions
	outside = ~(inside)
	# NP Defining the outside points
	plt.scatter(ra1[outside], dec1[outside], color = 'red', s = 0.5,
		label = 'Survey')
	# NP Plotting the outside points
	plt.ylabel('Declination (degrees)')
	plt.xlabel('Right Ascension (degrees)')
	plt.title('Spectroscopic Plate Areas Overlayed the'
		' Survey Lat-Lon Rectangle')
	# NP Labeling the graph
	plt.legend()
	# NP Creating a legend
	plt.savefig('/d/www/nikhil/public_html/ASTR5160/images/homework3test.png')
	# NP Saving the figure
	quasars = Table.read('/d/scratch/ASTR5160/week8/HW3quasarfile.dat',
		format = 'ascii.no_header')
	# NP Reading in quasar list
	raq = ["{}h{}m{}s".format(q[0:2], q[2:4], q[4:9]) for q in quasars["col1"]]
	decq = ["{}d{}m{}s".format(q[9:12], q[12:14], q[14:18]) for q in quasars["col1"]]
	# NP Creating strings for the ra's and dec's for each quasar
	c = SkyCoord(raq, decq, frame = 'icrs')
	# NP Generating skycoords for each quasar
	raqlist = c.ra.value
	decqlist = c.dec.value
	# NP Obtaining a list of ra's and dec's in degree format
	inside = mobs.contains(raqlist, decqlist)
	outside = ~inside
	# NP Defining a list of indices whether each quasar is in the spectroscopic region
	f = plt.figure()
	f.set_figwidth(8)
	f.set_figheight(5)
	# NP Making figure bigger
	plt.scatter(raqlist[inside], decqlist[inside], color = 'blue',
	    s = 0.8, label = 'Quasars inside mask')
	# NP Plotting all the quasar that are inside the mask
	plt.scatter(raqlist[outside], decqlist[outside], color = 'green',
	    s = 0.8, label = 'Quasars outside mask')
	# NP Plotting all of the quasars that are outside of the mask
	plt.text(150, 18, 'Mask area: \n'+str(np.round(specarea,2))+' sq. deg.', size = 16)
	plt.text(165, 20, 'Quasar density: \n'+str(np.round(len(raqlist[inside])/specarea,2))
	    + ' quasars per sq. deg.', size = 16)
	# NP Annotating the graph with the mask area and quasar density
	plt.ylabel('Declination (degrees)')
	plt.xlabel('Right Ascension (degrees)')
	plt.title('Quasars from list color-coded inside and outside of the mask')
	# NP Labeling the graph
	plt.legend()
	# NP Creating a legend
	plt.savefig('/d/www/nikhil/public_html/ASTR5160/images/homework3.png')
	# NP Saving figure
