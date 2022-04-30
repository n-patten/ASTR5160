import argparse
import numpy as np
from astropy.table import Table

def W1mag(objs):
	'''Calculates the W1 magnitude from a table of inputted objects.
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	Inputs
	-objs: astropy.Table. A table containing data found the sweep
	files.
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	Outputs
	W1: float. The W1 magnitude of each object in the objs table.'''
	W1 = 22.5-2.5*np.log10(objs['FLUX_W1'])
	return W1

def W2mag(objs):
	'''Calculates the W2 magnitude from a table of inputted objects.
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	Inputs
	-objs: astropy.Table. A table containing data found the sweep
	files.
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	Outputs
	W2: float. The W2 magnitude of each object in the objs table.'''
	W2 = 22.5-2.5*np.log10(objs['FLUX_W2'])
	return W2

def W3mag(objs):
	'''Calculates the W3 magnitude from a table of inputted objects.
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	Inputs
	-objs: astropy.Table. A table containing data found the sweep
	files.
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	Outputs
	W3: float. The W3 magnitude of each object in the objs table.'''
	W3 = 22.5-2.5*np.log10(objs['FLUX_W3'])
	return W3

def W4mag(objs):
	'''Calculates the W4 magnitude from a table of inputted objects.
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	Inputs
	-objs: astropy.Table. A table containing data found the sweep
	files.
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	Outputs
	W4: float. The W4 magnitude of each object in the objs table.'''
	W4 = 22.5-2.5*np.log10(objs['FLUX_W4'])
	return W4

def rmag(objs):
	'''Calculates the r magnitude from a table of inputted objects.
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	Inputs
	-objs: astropy.Table. A table containing data found the sweep
	files.
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	Outputs
	r: float. The r magnitude of each object in the objs table.'''
	r = 22.5-2.5*np.log10(objs['FLUX_R'])
	return r

def rmag(objs):
	'''Calculates the r magnitude from a table of inputted objects.
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	Inputs
	-objs: astropy.Table. A table containing data found the sweep
	files.
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	Outputs
	r: float. The r magnitude of each object in the objs table.'''
	r = 22.5-2.5*np.log10(objs['FLUX_R'])
	return r

def gmag(objs):
	'''Calculates the g magnitude from a table of inputted objects.
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	Inputs
	-objs: astropy.Table. A table containing data found the sweep
	files.
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	Outputs
	g: float. The g magnitude of each object in the objs table.'''
	g = 22.5-2.5*np.log10(objs['FLUX_G'])
	return g

def zmag(objs):
	'''Calculates the z magnitude from a table of inputted objects.
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	Inputs
	-objs: astropy.Table. A table containing data found the sweep
	files.
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	Outputs
	z: float. The z magnitude of each object in the objs table.'''
	z = 22.5-2.5*np.log10(objs['FLUX_Z'])
	return z

def splendid_function(objs):
	'''Displays which of the inputted table of objects is a quasar
	determined using color-cuts and proper motions.
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	Inputs
	-objs: astropy.Table. A table containing data found the sweep
	files.
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	Outputs
	-ii: array. An array of booleans indicating which indices of the
	inputted objects identified to be a quasar.
	Prints the number of objects identified as quasars.'''
	W1 = W1mag(objs)
	W2 = W2mag(objs)
	W3 = W3mag(objs)
	W4 = W4mag(objs)
	r = rmag(objs)
	g = gmag(objs)
	z = zmag(objs)
	ii = (r -W1 > (g -z -1)) & (objs['TYPE'] == 'PSF') &\
		(z - W1 > (0.4*(r-W1)-.3)) &\
		(objs['PMDEC'] > -1.4) & (objs['PMDEC'] < 1.4) &\
		(z - W1 > (0.8*(g-r)-0.8)) &\
		(r - W4 > (-2*(g-W3)+6.5)) & (r-W1 > 1.8*(r-z)-0.8) &\
		(W1-W2 > -.2) & (r < 19) & (objs['PMRA'] > -1.4) &\
		(objs['PMRA'] < 1.4) & (r - W1 > (2*(g-r)-1)) &\
		(W1 - W4 > (-10*(W1-W2)-0.8)) & (g-W3 > 1.0*(r-z)+1.2) &\
		(r - W1 > (-1*(W1-W3)+1.5))
	print(str(len(objs[ii])) +' quasars found.')
	return ii

if (__name__ == '__main__'):
	parser = argparse.ArgumentParser(description = 'Module to identify\
		potential quasars from an inputted file. This file must\
		contain the same data columns as the sweep files found in\
		/d/scratch/ASTR5160/data/legacysurvey/dr9/north/sweep/9.0.')
	parser.add_argument('path', type = str, help = 'Path to the \
		file.')
	args = parser.parse_args()
	sweepfile = args.path
	objs = Table.read(sweepfile)
	splendid_function(objs)
