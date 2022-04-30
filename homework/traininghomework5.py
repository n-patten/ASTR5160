import os
import numpy as np
import matplotlib.pyplot as plt
from astropy import units as u
from astropy.table import Table, vstack
from astropy.coordinates import SkyCoord
from tasks.week08.class16 import whichsweep
# NP Necessary imports

def matchsweeps(objs, names, r = 19):
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
			'legacysurvey/dr9/south/sweep/9.0/' +filename)
		rmag = 22.5-2.5*np.log10(obj['FLUX_R'])
		ii = (obj["TYPE"] == "PSF") & (rmag < r) & (obj['FLUX_W1'] > 0)
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
	return objs_all[idx2], objs_all[:1000]

if(__name__ == '__main__'):
	qsos = Table.read('/d/scratch/ASTR5160/week10/qsos-ra180-dec30-rad3.'\
		+'fits', memmap = True)
	# NP Defining known quasars
	print(qsos.colnames)
	# NP Getting column names for the quasar file for information
	qra = qsos['RA']
	qdec = qsos['DEC']
	# NP Making RA's and Dec's for the quasars
	files = os.listdir('/d/scratch/ASTR5160/data/legacysurvey/dr9/'
	    	'south/sweep/9.0/')
	# NP Defining path to sweep files
	sweeps = files[1:]
	# NP Defining sweep files list
	sweeps = whichsweep(qra, qdec, sweeps)
	# NP Finding which sweeps contain the known quasars
	print('Sweeps needed: '+str(sweeps))
	# NP Printing which sweeps are required
	cqsos = SkyCoord(qra, qdec, unit = u.deg, frame = 'icrs')
	# NP Making SkyCoord objects for the quasars
	qsweeps, restsweeps = matchsweeps(cqsos, sweeps)
	# NP Matching quasars to sweep objects and making list of
	# NP non-quasars
	rq = 22.5-2.5*np.log10(qsweeps['FLUX_R']/qsweeps['MW_TRANSMISSION_R'])
	gq = 22.5-2.5*np.log10(qsweeps['FLUX_G']/qsweeps['MW_TRANSMISSION_G'])
	zq = 22.5-2.5*np.log10(qsweeps['FLUX_Z']/qsweeps['MW_TRANSMISSION_Z'])
	W1q = 22.5-2.5*np.log10(qsweeps['FLUX_W1']/qsweeps['MW_TRANSMISSION_W1'])
	W2q = 22.5-2.5*np.log10(qsweeps['FLUX_W2']/qsweeps['MW_TRANSMISSION_W2'])
	W3q = 22.5-2.5*np.log10(qsweeps['FLUX_W3']/qsweeps['MW_TRANSMISSION_W3'])
	W4q = 22.5-2.5*np.log10(qsweeps['FLUX_W4']/qsweeps['MW_TRANSMISSION_W4'])
	rs = 22.5-2.5*np.log10(restsweeps['FLUX_R']/restsweeps['MW_TRANSMISSION_R'])
	gs = 22.5-2.5*np.log10(restsweeps['FLUX_G']/restsweeps['MW_TRANSMISSION_G'])
	zs = 22.5-2.5*np.log10(restsweeps['FLUX_Z']/restsweeps['MW_TRANSMISSION_Z'])
	W1s = 22.5-2.5*np.log10(restsweeps['FLUX_W1']/restsweeps['MW_TRANSMISSION_W1'])
	W2s = 22.5-2.5*np.log10(restsweeps['FLUX_W2']/restsweeps['MW_TRANSMISSION_W2'])
	W3s = 22.5-2.5*np.log10(restsweeps['FLUX_W3']/restsweeps['MW_TRANSMISSION_W3'])
	W4s = 22.5-2.5*np.log10(restsweeps['FLUX_W4']/restsweeps['MW_TRANSMISSION_W4'])
	# NP Defining magnitudes in all bandpasses and correcting for 
	# NP galactic extinction
	rminusW1s = rs -W1s
	gminuszs = gs -zs
	rminusW1q = rq -W1q
	gminuszq = gq -zq
	# NP Defined some colors but ultimately abadnoned this

	f = plt.figure()
	f.set_figwidth(8)
	f.set_figheight(6)
	plt.xlabel('g-z')
	plt.ylabel('r-W1')
	plt.scatter(gminuszq, rminusW1q, s = 6, color = 'red', label = 'quasar')
	plt.scatter(gminuszs, rminusW1s, s = 6, color = 'black', label = 'star')
	x = np.linspace(-1.5, 3.5, 100)
	plt.plot(x, x - 1)
	plt.legend()
	plt.show()
	# NP Plot 1

	f = plt.figure()
	f.set_figwidth(8)
	f.set_figheight(6)
	plt.xlabel('r-z')
	plt.ylabel('r-W1')
	plt.scatter((rq-zq), rminusW1q, s = 6, color = 'red', label = 'quasar')
	plt.scatter((rs-zs), rminusW1s, s = 6, color = 'black', label = 'star')
	x = np.linspace(-1.5, 2, 100)
	plt.plot(x, 1.8*x - .8)
	plt.legend()
	plt.show()
	# NP Plot 2

	f = plt.figure()
	f.set_figwidth(8)
	f.set_figheight(6)
	plt.xlabel('r-W1')
	plt.ylabel('z-W1')
	plt.scatter((rq-W1q), (zq-W1q), s = 6, color = 'red', label = 'quasar')
	plt.scatter((rs-W1s), (zs-W1s), s = 6, color = 'black', label = 'star')
	x = np.linspace(-2, 5, 100)
	plt.plot(x, 0.4*x - .3)
	plt.legend()
	plt.show()
	# NP Plot 3

	f = plt.figure()
	f.set_figwidth(8)
	f.set_figheight(6)
	plt.xlabel('g-r')
	plt.ylabel('r-W1')
	plt.scatter((gq-rq), (rq-W1q), s = 6, color = 'red', label = 'quasar')
	plt.scatter((gs-rs), (rs-W1s), s = 6, color = 'black', label = 'star')
	x = np.linspace(-2, 3, 100)
	plt.plot(x, 2*x - 1)
	plt.legend()
	plt.show()
	# NP Plot 4

	f = plt.figure()
	f.set_figwidth(8)
	f.set_figheight(6)
	plt.xlabel('g-z')
	plt.ylabel('z-W1')
	plt.scatter((gq-zq), (zq-W1q), s = 6, color = 'red', label = 'quasar')
	plt.scatter((gs-zs), (zs-W1s), s = 6, color = 'black', label = 'star')
	x = np.linspace(-2, 3, 100)
	plt.plot(x, 0.8*x - .8)
	plt.legend()
	plt.show()
	# NP Plot 5

	f = plt.figure()
	f.set_figwidth(8)
	f.set_figheight(6)
	plt.xlabel('W1-W2')
	plt.ylabel('W1-W4')
	plt.scatter((W1q-W2q), (W1q-W4q), s = 6, color = 'red', label = 'quasar')
	plt.scatter((W1s-W2s), (W1s-W4s), s = 6, color = 'black', label = 'star')
	x = np.linspace(-1, 2, 100)
	plt.plot(x, -10*x -0)
	plt.legend()
	plt.show()
	# NP Plot 6

	f = plt.figure()
	f.set_figwidth(8)
	f.set_figheight(6)
	plt.xlabel('W1-W3')
	plt.ylabel('W3-W4')
	plt.scatter((W1q-W3q), (W3q-W4q), s = 6, color = 'red', label = 'quasar')
	plt.scatter((W1s-W3s), (W3s-W4s), s = 6, color = 'black', label = 'star')
	x = np.linspace(-1, 2, 100)
	plt.plot(x, 5*x -2.5)
	plt.legend()
	plt.show()
	# NP Plot 7

	f = plt.figure()
	f.set_figwidth(8)
	f.set_figheight(6)
	plt.xlabel('g-W3')
	plt.ylabel('r-W4')
	plt.scatter((gq-W3q), (rq-W4q), s = 6, color = 'red', label = 'quasar')
	plt.scatter((gs-W3s), (rs-W4s), s = 6, color = 'black', label = 'star')
	x = np.linspace(-0, 4, 100)
	plt.plot(x, -2*x +6.5)
	plt.legend()
	plt.show()
	# NP Plot 8

	f = plt.figure()
	f.set_figwidth(8)
	f.set_figheight(6)
	plt.xlabel('W1-W3')
	plt.ylabel('r-W1')
	plt.scatter((W1q-W3q), (rq-W1q), s = 6, color = 'red', label = 'quasar')
	plt.scatter((W1s-W3s), (rs-W1s), s = 6, color = 'black', label = 'star')
	x = np.linspace(-3, 4, 100)
	plt.plot(x, -1*x +1.5)
	plt.legend()
	plt.show()
	# NP Plot 9

	f = plt.figure()
	f.set_figwidth(8)
	f.set_figheight(6)
	plt.xlabel('r-z')
	plt.ylabel('g-W3')
	plt.scatter((rq-zq), (gq-W3q), s = 6, color = 'red', label = 'quasar')
	plt.scatter((rs-zs), (gs-W3s), s = 6, color = 'black', label = 'star')
	x = np.linspace(-2, 3, 100)
	plt.plot(x, 1*x +1.2)
	plt.legend()
	plt.show()
	# NP Plot 10

	f = plt.figure()
	f.set_figwidth(8)
	f.set_figheight(6)
	plt.xlabel('r-z')
	plt.ylabel('g-W3')
	plt.scatter((rq-zq), (gq-W2q), s = 6, color = 'red', label = 'quasar')
	plt.scatter((rs-zs), (gs-W2s), s = 6, color = 'black', label = 'star')
	x = np.linspace(-2, 2.5, 100)
	plt.plot(x, 2*x -0.5)
	plt.legend()
	plt.show()
	# NP Plot 11

	f = plt.figure()
	f.set_figwidth(8)
	f.set_figheight(6)
	plt.xlabel('W1-W2')
	plt.ylabel('W1-W4')
	plt.scatter((W1q-W2q), (W1q-W4q), s = 6, color = 'red', label = 'quasar')
	plt.scatter((W1s-W2s), (W1s-W4s), s = 6, color = 'black', label = 'star')
	x = np.linspace(0, 0, 100)
	plt.plot(x, -100*x -0)
	plt.xlim(-1,1)
	plt.legend()
	plt.show()
	# NP Plot 12

	print(np.min(qsweeps['PMRA']))
	print(np.max(qsweeps['PMRA']))
	print(np.min(qsweeps['PMDEC']))
	print(np.max(qsweeps['PMDEC']))
	# NP Printing proper motions in RA and Dec for quasars

	print(np.min(restsweeps['PMRA']))
	print(np.max(restsweeps['PMRA']))
	print(np.min(restsweeps['PMDEC']))
	print(np.max(restsweeps['PMDEC']))
	# NP Printing proper motions in RA and Dec for non-quasars
