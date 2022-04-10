import os
import argparse
import numpy as np
import matplotlib.pyplot as plt
from astropy import units as u
from astropy.table import Table, vstack
from astropy.coordinates import SkyCoord
from tasks.week08.class16 import whichsweep
# NP Necessary imports

def whichfirst(ra, dec, t):
	'''Displays which objects in the FIRST survey are
	within a given radius of a target RA and Dec.
	---------------------------------------------
	Inputs
	-ra: float. The Right Ascension of the point to
	search around in units of degrees.
	-dec: float. The Declination of the point to search
	around in units of degrees.
	-t: float. The radius to search around the given
	point in degrees. Default value is 3 degrees.
	---------------------------------------------
	Outputs
	firstobjs: array. An array of SkyCoord objects that
	are within the given radius from the target point.'''
	first = Table.read('/d/scratch/ASTR5160/data/'
		'first/first_08jul16.fits')
	# NP Reading in FIRST file.
	rafirst = first['RA']
	decfirst = first['DEC']
	# NP Creating a list of RA's and Dec's for FIRST objects.
	cfirst = SkyCoord(rafirst, decfirst,
		unit = u.deg, frame = 'icrs')
	# NP Creating SkyCoord objects for FIRST objects
	ctarget = SkyCoord([ra], [dec],
		unit = u.deg, frame = 'icrs')
	# NP Creating a SkyCoord object for the RA/Dec to search around
	idx1, idx2, spe2d, dist3d = \
		ctarget.search_around_sky(cfirst, seplimit = t*u.deg)
	# NP Searching around the sky of the target RA/Dec
	firstobjs = cfirst[idx1]
	# NP Creating FIRST objects that are within a given radius of
	# NP the target RA/Dec
	print(str(len(firstobjs))+' FIRST objects found within '
		+str(t) +' degrees of (' +str(ra) +', ' +str(dec) +')')
	# NP Printing how many objects were found
	return firstobjs

def matchsweeps(objs, names, r = 22, W1minusW2 = 0.5):
	'''Displays which objects in the FIRST survey are
	within a given radius of a target RA and Dec.
	---------------------------------------------
	Inputs
	-objs: array. An array of FIRST objects to match.
	-sweeps: list. A list of sweepfiles to cross-reference.
	-r: float. Limiting r magnitude to fitler by. Default
	value is 22.
	-W1minusW2: float. Limiting W1 - W2 color to filter by.
	Default value is 0.5.
	---------------------------------------------
	Outputs
	firstobjs: array. An array of sweep objects that
	are within the given radius from the target point.'''
	objs_list = []
	for filename in names:
		print('Searching file '+filename)
		obj = Table.read('/d/scratch/ASTR5160/data/'
			'legacysurvey/dr9/north/sweep/9.0/' +filename)
		rmag = 22.5-2.5*np.log10(obj['FLUX_R'])
		W1mag = 22.5-2.5*np.log10(obj['FLUX_W1'])
		W2mag = 22.5-2.5*np.log10(obj['FLUX_W2'])
		ii = (obj["TYPE"] == "PSF") & (rmag < r) & (W1mag-W2mag > W1minusW2)
		objs_list.append(obj[ii])
	# NP Searching through multiple sweep files and appending only
	# NP objects that meet the required criteria.
	objs_all = vstack(objs_list)
	sweepsra = objs_all['RA'].value
	sweepsdec = objs_all['DEC'].value
	# NP Generating RA/Dec for all objects in sweep files to match to
	# NP FIRST objects.
	csweeps = SkyCoord(sweepsra, sweepsdec, unit = u.deg, frame = 'icrs')
	idx1, idx2, d2d, d3d = \
		csweeps.search_around_sky(objs, (1)*u.arcsec)
	# NP Matching FIRST objects to sweep objects
	print(str(len(objs_all[idx2])) +' sources matched.')
	# NP Printing how many objects were matched
	return objs_all[idx2]

class sdssQuery:
	"""
	NAME: sdssQuery

	PURPOSE: class that can be initialized using Python's urllib tools to
	send an SQL command to SDSS web services

	CALLING SEQUENCE: from the UNIX command line:

	python sdssDR9query.py ra dec

	INPUTS: ra and dec shoud be sent from the command line:

	ra - Right Ascension of position to query around in SDSS DR9
	dec - declination of position to query around in SDSS DR9

	OUTPUTS: the result of the SQL command called "query" in the
	code, below, is executed by the SDSS DR9 SQL API and
	printed at the command line.

	COMMENTS: This is adapted from an example provide by the SDSS 
	in an early tutorial on web services.

	Note that the SQL command passed as "query" can be changed to
	any valid SDSS string.

	EXAMPLES: At the Unix command line:

	python sdssDR9query.py 145.285854 34.741254

	should return:

	145.28585385,34.74125418,21.132605,20.059248,19.613457,19.379345,19.423323,7.7489487E-4
	"""
	# ADM this is the URL of the SDSS "web services" API.
	url='http://skyserver.sdss3.org/dr9/en/tools/search/x_sql.asp'
	# ADM always return the output in .csv format
	format = 'csv'

	# ADM initialize the class with a null query.
	def __init__(self):
		self.query = ''
		self.cleanQuery = ''

	# ADM use Python's urllib module to initialize a query string.
	def executeQuery(self):
		from urllib.parse import urlencode
		from urllib.request import urlopen
		self.filterQuery()
		params = urlencode({'cmd': self.cleanQuery, 'format':self.format})
		return urlopen(self.url + '?%s' % params)
	    
	# ADM this cleans up the syntax in the query string.
	def filterQuery(self):
		from os import linesep
		self.cleanQuery = ''
		tempQuery = self.query.lstrip()
		for line in tempQuery.split('\n'):
	    		self.cleanQuery += line.split('--')[0] + ' ' + linesep;

def matchsdss(objs):
	qry = sdssQuery()
	from time import sleep
	# ADM the query to be executed. You can substitute any query, here!
	query = ["""SELECT top 1 ra,dec,u,i FROM PhotoObj as PT
	JOIN dbo.fGetNearbyObjEq({},{},0.02) as GNOE
	on PT.objID = GNOE.objID ORDER BY GNOE.distance""".format(str(i['RA']),\
		str(i['DEC'])) for i in objs]

	results = []
	# ADM execute the query.
	# NP This was mostly Dr. Myer's code from SDSSquery.py, but I
	# NP had to slightly modify it for this problem.
	for i in query:
		qry.query = i
		for line in qry.executeQuery():
			result = line.strip().decode()
		results.append(result)

	# ADM NEVER remove this line! It won't speed up your code, it will
	# ADM merely overwhelm the SDSS server (a denial-of-service attack)!
	sleep(1)
	rarray = np.vstack(results)
	ii = np.array([phrase[0] != 'N' for phrase in results])
	# NP Filtering results to only include matches
	print(str(len(rarray[ii])) +' objects matched to SDSS')
	# NP Printing how many objects were matched with SDSS
	return rarray[ii]

def findfluxes(objs):
	'''Displays the u, g, r, i, z, W1, W2, W3 and W4 fluxes
	of the brightest object in u magnitude
	---------------------------------------------
	Inputs
	-objs: array. An array of sweep objects to match.
	---------------------------------------------
	Outputs
	fluxes: array. An array of the objects corresponding ugriz and W1, W2
	W3 and W4 fluxes.'''
	results = matchsdss(objs)
	umag = np.array([i[0].split(',')[2] for i in results]).astype(float)
	imag = np.array([i[0].split(',')[3] for i in results]).astype(float)
	ras = np.array([i[0].split(',')[0] for i in results]).astype(float)
	decs = np.array([i[0].split(',')[1] for i in results]).astype(float)
	# NP Creating lists of ra, dec, u mag, and i mag from SDSS results
	ubrite1 = np.min(umag)
	# NP Finding minimum u mag
	ii = np.where(umag == np.min(umag))
	ratarget = ras[ii].item()
	dectarget = decs[ii].item()
	# NP Obtaining RA/Dec of birghtest u umag object
	print('ubrite1: ' +str(ubrite1) +' at (' +str(ratarget) 
		+',' +str(dectarget)+')')
	print(umag[ii].item())
	# NP Printing result
	cobjs = SkyCoord(objs['RA'], objs['DEC'], unit = u.deg, \
		frame = 'icrs')
	ctarget = SkyCoord([ratarget], [dectarget], unit = u.deg, \
		frame = 'icrs')
	idxc, idxcatalog, d2d, d3d = \
		ctarget.search_around_sky(cobjs, (1)*u.arcsec)
	# NP Matching brightest u mag object to array of FIRST objects
	fu = 10**((22.5-umag[ii].item())/2.5)
	fg = objs[idxc]['FLUX_G'].value.item()
	fr = objs[idxc]['FLUX_R'].value.item()
	fi = 10**((22.5-imag[ii].item())/2.5)
	fz = objs[idxc]['FLUX_Z'].value.item()
	fW1 = objs[idxc]['FLUX_W1'].value.item()
	fW2 = objs[idxc]['FLUX_W2'].value.item()
	fW3 = objs[idxc]['FLUX_W3'].value.item()
	fW4 = objs[idxc]['FLUX_W4'].value.item()
	# NP Obtaining all of the fluxes for this object
	print('u flux: ' +str(fu) +' nmgy')
	print('g flux: ' +str(fg) +' nmgy')
	print('r flux: ' +str(fr) +' nmgy')
	print('i flux: ' +str(fi) +' nmgy')
	print('z flux: ' +str(fz) +' nmgy')
	print('W1 flux: ' +str(fW1) +' nmgy')
	print('W2 flux: ' +str(fW2) +' nmgy')
	print('W3 flux: ' +str(fW3) +' nmgy')
	print('W4 flux: ' +str(fW4) +' nmgy')
	# NP Printing all fluxes
	fluxes = [fu, fg, fr, fi, fz, fW1, fW2, fW3, fW4]
	# NP Returning all fluxes
	return fluxes

def plotfluxes(fluxes):
	'''Generates a plot of flux densities versus wavelength
	for an SDSS object.
	---------------------------------------------
	Inputs
	-objs: array. u, g, r, i, z, W1, W2, W3, and W4 fluxes.
	-save: boolean. Whether to save the figure to a
	directory. Default is False.
	-dir: str. Directory to save to. Default is my public
	directory for this class.
	---------------------------------------------
	Outputs
	-Null. Generates a plot and optionally saves it as a png.'''
	lambdas = [3543, 4770, 6231, 7625, 9134, 34000, 46000,\
		120000, 220000]
	# NP These are the wavelengths in angstroms for all the bandpasses
	# NP that we have fluxes for
	fl = [(i*10**(-9))/(y*10**(-10)) for i,y in zip(fluxes,\
		lambdas)]
	# NP Creating a flux density variable
	f = plt.figure()
	f.set_figwidth(8)
	f.set_figheight(6)
	# NP Making figure larger
	plt.scatter(lambdas, fl, color = 'g')
	# NP Plotting points
	plt.xlabel('Wavelength (Angstroms)')
	plt.ylabel('fλ (Mgy/Angstrom)')
	plt.title('Flux density plotted over Wavelength for '
		'brightest u object')
	# NP Labeling graph
	plt.show()
	# NP Open a window of the graph

if(__name__ == '__main__'):
	parser = argparse.ArgumentParser(description = 'Module to match\
		FIRST objects to sweep objects and SDSS. After this, the\
		module will calculate the fluxes for the brightest u-band\
		object in the ugriz and W1W2W3W4 bands and generate a plot\
		of flux density versus wavelength for this object. The\
		matchSDSS method heavily sourced Dr. Myers SDSSDR9query.py\
		file in /d/scratch/ASTR5160/week8.')
	parser.add_argument('RA', type = float, help = 'Right ascension \
		in degrees to search around.')
	parser.add_argument('DEC', type = float, help = 'Declination in \
		degrees to search around.')
	parser.add_argument('radius', type = float, help = 'Radius in \
		degrees to search around target RA/Dec.')
	args = parser.parse_args()
	firstobjs = whichfirst(args.RA, args.DEC, args.radius)
	files = os.listdir('/d/scratch/ASTR5160/data/legacysurvey/dr9/'
    		'north/sweep/9.0/')
	sweeps = files[1:]
	sweepsnames = whichsweep(firstobjs.ra.value, firstobjs.dec.value, sweeps)
	objs = matchsweeps(firstobjs, sweepsnames)
	fluxes = findfluxes(objs)
	print('Prints ubrite1: 18.093157 at (160.66713674,48.56763031)')
	print('SDSS Spectrum gives [MgII] 2799A at 5699A. z is therefore')
	print('~1.036. At this redshift, the r band, 6231A, corresponds')
	print('to 3060A in the galaxy\'s frame. This is very close to')
	print('the Mg II line. Therefore, this object appears so bright')
	print('in the r band because of the strong [MgII] emission from')
	print('this object. In addition, the [CIII] 1908A line has been')
	print('redshifted to ~3800A. This is why this object is so bright')
	print('in the u band. These features, coupled with the strong')
	print('W flux densities makes this object very likely to be a')
	print('quasar.')
	plotfluxes(fluxes)
