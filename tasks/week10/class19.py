import os
import numpy as np
import astropy.units as u
from astropy.table import Table, vstack
from astropy.coordinates import SkyCoord
from tasks.week8.class16 import whichsweep

def readsweeps(ra, dec):
	files = os.listdir('/d/scratch/ASTR5160/data/legacysurvey/dr9/'
		'south/sweep/9.0/')
	sweeps = files[1:]
	names = list(whichsweep(np.array(ra), np.array(dec), sweeps))
	sweep1 = Table.read('/d/scratch/ASTR5160/data/legacysurvey/dr9/south/'
	    	'sweep/9.0/' + names[0], memmap=True)
	sweep2 = Table.read('/d/scratch/ASTR5160/data/legacysurvey/dr9/south/'
	    	'sweep/9.0/' + names[1], memmap=True)
	sweep3 = Table.read('/d/scratch/ASTR5160/data/legacysurvey/dr9/south/'
	   	 'sweep/9.0/' + names[2], memmap=True)
	sweep4 = Table.read('/d/scratch/ASTR5160/data/legacysurvey/dr9/south/'
	    	'sweep/9.0/' + names[3], memmap=True)
	print('sweep files read')
	sweepfiles = [sweep1, sweep2, sweep3, sweep4]
	return sweepfiles    

def getpsf(ra, dec, t, sweep):
	sweep2 = sweep
	ras2 = sweep2['RA'].value
	decs2 = sweep2['DEC'].value
	racenter, deccenter = ra*u.degree, dec*u.degree
	ct2 = SkyCoord([racenter], [deccenter], frame = 'icrs')
	c2 = SkyCoord(ras2*u.degree, decs2*u.degree, frame = 'icrs')
	idxc2, idxcatalog2, d2d2, d3d2 = c2.search_around_sky(ct2, t*u.deg)
	ii = (sweep2[idxcatalog2]['TYPE'] == 'PSF')
	psfobjs = sweep2[idxcatalog2][ii]
	print(str(len(psfobjs)) +' PSF objects found near (a, d): ('
		+str(ra) +', ' +str(dec) +')')
	return psfobjs

def limitsweeps(sweeps, rmag):
	ii = (22.5-2.5*np.log10(sweeps[0]['FLUX_R'])< rmag)
	combine = sweeps[0][ii]
	print('starting loop')
	for i in range(len(sweeps)-1):
		ii = (22.5-2.5*np.log10(sweeps[i+1]['FLUX_R']) < rmag)
		combine = vstack([combine, sweeps[i+1][ii]])
		print('Combine done')
	return combine

def whichquasars(psf):
	'''Finds which quasars are close to a certain ra and dec above a given brightness'''
	'''------------------------------'''
	'''Inputs'''
	'''rmag- float. The limiting r magnitude to limit the search by.'''
	'''psf- array. Array of psf objects near a given ra and dec.'''
	'''------------------------------'''
	'''Outputs'''
	'''A list of SkyCoord objects of quasars that were found.'''
	qsos = Table.read('/d/scratch/ASTR5160/week10/'
		'qsos-ra180-dec30-rad3.fits', memmap=True)
	raqso, decqso = qsos['RA'], qsos['DEC']
	quasars = SkyCoord(raqso*u.degree, decqso*u.degree, frame = 'icrs')
	psfobjs = psf
	ras2 = psfobjs['RA'].value
	decs2 = psfobjs['DEC'].value
	cpsfobjs = SkyCoord(ras2*u.degree, decs2*u.degree, frame = 'icrs')
	idxc3, idxcatalog3, d2d3, d3d3 = quasars.search_around_sky(cpsfobjs, 0.0001*u.deg)
	qsos = psfobjs[idxc3]
	print(str(len(qsos)) +' Quasars matched')
	return qsos

if(__name__ == '__main__')
	files = os.listdir('/d/scratch/ASTR5160/data/legacysurvey/dr9/'
		'south/sweep/9.0/')
	sweeps = files[1:]
	print(whichsweep(np.array(188.53667), np.array(21.04572), sweeps))
	# NP Prints:
	# NP {'sweep-180p020-190p025.fits'}
	sweep = Table.read('/d/scratch/ASTR5160/data/legacysurvey/dr9/south/'
	    	'sweep/9.0/sweep-180p020-190p025.fits', memmap=True)
	# NP Defining sweep file with point in question
	ras = sweep['RA'].value
	decs = sweep['DEC'].value
	# NP Making list of ra's and dec's for objects in the sweep file
	c = SkyCoord(ras*u.deg, decs*u.deg, frame = 'icrs')
	ct = SkyCoord([188.53667*u.deg], [21.04572*u.deg], frame = 'icrs')
	idxc, idxcatalog, d2d, d3d = c.search_around_sky(ct, 0.00001*u.deg)
	# NP Using search_around_sky to find particular object
	print(sweep[idxcatalog]['TYPE'])
	# NP Prints:
	# NP EXP
	# NP This object is an exponential galaxy
	# NP Task 1 complete
	print('ALLMASK_G: '+str(int(sweep[idxcatalog]['ALLMASK_G'].value))
	     	+'\nALLMASK_R: '+str(int(sweep[idxcatalog]['ALLMASK_R'].value))
	      	+'\nALLMASK_Z: '+str(int(sweep[idxcatalog]['ALLMASK_Z'].value)))
	# NP Prints:
	# NP ALLMASK_G: 2
	# NP ALLMASK_R: 2
	# NP ALLMASK_Z: 2
	# NP This object was saturated in the above filters for all exposures
	# NP According to SIMBAD, this source is a possible BLAZAR (head-on
	# quasar).
	# NP Task 2 complete
	sweep = readsweeps(180, 30)
	cutsweeps = limitsweeps(sweep, 20)
	psfs = getpsf(180, 30, 3, cutsweeps)
	qsos = whichquasars(psfs)
	# NP 275 quasars found for the above conditions

