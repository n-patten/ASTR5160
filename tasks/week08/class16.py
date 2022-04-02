import matplotlib.pyplot as plt
import numpy as np
import os
from astropy.table import Table
# NP Necessary imports

def decode_sweep_name(sweepname):
    """Retrieve RA/Dec edges from a full directory path to a sweep file
    Parameters
    ----------
    sweepname : :class:`str`
        Full path to a sweep file, e.g., /a/b/c/sweep-350m005-360p005.fits
    nside : :class:`int`, optional, defaults to None
        (NESTED) HEALPixel nside
    inclusive : :class:`book`, optional, defaults to ``True``
        see documentation for `healpy.query_polygon()`
    fact : :class:`int`, optional defaults to 4
        see documentation for `healpy.query_polygon()`
    Returns
    -------
    :class:`list` (if nside is None)
        A 4-entry list of the edges of the region covered by the sweeps file
        in the form [RAmin, RAmax, DECmin, DECmax]
        For the above example this would be [350., 360., -5., 5.]
    :class:`list` (if nside is not None)
        A list of HEALPixels that touch the  files at the passed `nside`
        For the above example this would be [16, 17, 18, 19]
    """
    # ADM extract just the file part of the name.
    sweepname = os.path.basename(sweepname)

    # ADM the RA/Dec edges.
    ramin, ramax = float(sweepname[6:9]), float(sweepname[14:17])
    decmin, decmax = float(sweepname[10:13]), float(sweepname[18:21])

    # ADM flip the signs on the DECs, if needed.
    if sweepname[9] == 'm':
        decmin *= -1
    if sweepname[17] == 'm':
        decmax *= -1
    rasdecs = [ramin, ramax, decmin, decmax]
    return rasdecs
# NP This code was taken from https://github.com/desihub/desitarget/blob/2.4.0/
# NP py/desitarget/io.py#L2354-L2397
# NP This was used to obtain the ramin, ramax, dmin and dmax for each sweep file

def whichsweep(ra, dec, sweepfiles):
    '''Takes in a list of RA/DEC and sweepfiles and returns which 
    sweep files contain these RA/DEC.'''
    files = []
    # NP This will be the list of files that contain the inputted objects
    for i in sweepfiles:
        # NP Looping through all of the sweep files
        rmin, rmax, dmin, dmax = decode_sweep_name(i)
        # NP Defining rmin, rmax, dmin and dmax for all sweep files
        ii = (ra <= rmax) & (ra >= rmin) & (dec <= dmax) & (dec >= dmin)
        # NP Finding if any sweep files contain inputted RA/DEC
        if (ii.any()):
            files.append(os.path.basename(i))
            # NP Appending any sweep files that contain the points

    return(set(files))
    # NP Returning the sweep files that contain any inputted points, removing
    # NP duplicates

def class16():
	table = Table.read('/d/scratch/ASTR5160/data/first/first_08jul16.'
		'fits', memmap=True)
	# NP Creating a table of the VLA FIRST data

	ra = table['RA']
	dec = table['DEC']
	# NP Making ra and dec lists

	f = plt.figure()
	f.set_figwidth(8)
	f.set_figheight(5)
	# NP Making the figure largeer
	plt.scatter(ra, dec, color = 'green')
	# NP Plotting all of the points in the lists
	plt.ylabel('Dec(deg)')
	plt.xlabel('Dec(deg)')
	plt.title('Objects in the VLA FIRST survey')
	# NP Labelling the figure
	plt.savefig('/d/www/nikhil/public_html/ASTR5160/images/VLAFIRST.png')
	# NP Saving the figure
	# NP Task 1 complete

	for r,de in zip(ra[:100], dec[:100]):
	    os.system("python /d/users/nikhil/ASTR5160/tasks/week8/sdssDR9"
		      "query.py "+str(r)+" "+str(de)+" >> /d/users/nikhil/"
		      "ASTR5160/tasks/week8/file.txt")
	# NP Searchin SDSS for objects near the first 100 points, takes a long time
	# NP Task 3 complete

	table2 = Table.read('/d/scratch/ASTR5160/data/legacysurvey/dr9/north/'
	    'sweep/9.0/sweep-000m005-010p000.fits', memmap=True)
	ra2 = table2['RA']
	dec2 = table2['DEC']
	print(ra2[:10].value)
	print(dec2[:10].value)
	# NP Exploring the sweep data

	table3 = Table.read('/d/scratch/ASTR5160/data/legacysurvey/dr9/north/'
		            'sweep/9.0/sweep-010m005-020p000.fits', memmap=True)
	ra3 = table3['RA']
	dec3 = table3['DEC']
	print(ra3[:10].value)
	print(dec3[:10].value)

	plt.scatter(ra[:100], dec[:100])
	# NP Plotting the first 100 points of the VLA FIRST data

	files = os.listdir('/d/scratch/ASTR5160/data/legacysurvey/dr9/'
	    'north/sweep/9.0/')
	# NP Creating a directory for the sweep data

	print(whichsweep(ra[:100], dec[:100], files[1:]))
	# NP Returns 11 files as expected
