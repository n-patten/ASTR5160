import numpy as np
import matplotlib.pyplot as plt
import argparse
from numpy.random import random
# NP Necessary imports
# ADM I added this one!
import os


def area(amin, amax, dmin, dmax):
    '''Returns the area in square degrees of a rectangle bounded by amin, 
    amax, dmin and dmax. All inputs must be inputted in degrees.

    ADM:
    docstrings should include info on inputs and outputs in a specific
    format. For example:

    Parameters
    ----------
    amin : float, lower ra bound in degrees
    amax : float, upper ra bound in degrees
    dmin : float, lower dec bound in degrees
    dmax : float, upper dec bound in degrees

    Returns
    -------
    float, area of a lat-lon rectangle in square degrees.
    '''
    a = (np.pi/180*(amax-amin))*(np.sin(dmax*np.pi/180)-np.sin(dmin*np.pi/180))
    # NP Calculating the area in str first using the equation in the lecture notes.
    adeg = a*(180/np.pi)**2
    # NP Converting this answer into square degrees
    # ADM Python style is to leave a blank line before a return statement.

    return adeg


def aitoffplot(amin, amax, dmin, dmax, plot_dir):
    '''Inputs right ascensions amin and amax and declinations dmin and dmax in degrees
    and generates an aitoff projection of the lat-lon rectangles spanning 15 degree
    declination icrements and labels their areas'''
    fig = plt.figure()
    fig.set_figwidth(15)
    fig.set_figheight(15)
    # NP Changing the size of the plot so that the title is able to be read
    ax = fig.add_subplot(111, projection="aitoff")

    # NP Creating an aitoff plot
#    ax.plot([amin*np.pi/180,amin*np.pi/180,amax*np.pi/180,amax*np.pi/180,amin*np.pi/180],
#            [(dmin)*np.pi/180,(dmax)*np.pi/180,(dmax)*np.pi/180,(dmin)*np.pi/180,
#             (dmin)*np.pi/180],'-r', label = 'Area:'+str(np.round(area(amin, amax, dmin, dmax)
#            ,3))+' sq. deg.')
    # NP Plotting the inputted lat-lon rectangle with label corresponding to area
#    ax.plot([amin*np.pi/180,amin*np.pi/180,amax*np.pi/180,amax*np.pi/180,amin*np.pi/180],
#            [(dmax+0)*np.pi/180,(dmax+15)*np.pi/180,(dmax+15)*np.pi/180,(dmax+0)*np.pi/180,
#             (dmax+0)*np.pi/180],'-g', label = 'Area:'+str(np.round(area(amin, amax, dmax,
#            dmax+15),3))+' sq. deg.')
    # NP Plotting another lat-lon rectangle 15 deg above the inputted rectangle with area labeled
#    ax.plot([amin*np.pi/180,amin*np.pi/180,amax*np.pi/180,amax*np.pi/180,amin*np.pi/180],
#            [(dmax+15)*np.pi/180,(dmax+30)*np.pi/180,(dmax+30)*np.pi/180,(dmax+15)*np.pi/180,
#             (dmax+15)*np.pi/180],'-b', label = 'Area:'+str(np.round(area(amin, amax, dmax+15,
#            dmax+30),3))+' sq. deg.')
    # NP Plotting another lat-lon rectangle 30 deg above the inputted rectangle with area labeled
#    ax.plot([amin*np.pi/180,amin*np.pi/180,amax*np.pi/180,amax*np.pi/180,amin*np.pi/180],
#            [(dmax+30)*np.pi/180,(dmax+45)*np.pi/180,(dmax+45)*np.pi/180,(dmax+30)*np.pi/180,
#             (dmax+30)*np.pi/180],'-k', label = 'Area:'+str(np.round(area(amin, amax, dmax+30,
#            dmax+45),3))+' sq. deg.')

    # ADM when you're doing the same task repeatedly, it's fine to use a 
    # ADM for loop. If you find yourself repeating very similar code, and
    # ADM there isn't an array-based approach (for numbers), or a list
    # ADM comprehension approach (for strings) use a for loop.
    
    # ADM first convert to radians to keep everything nice and compact.
    amin, amax, dmin, dmax = np.radians([amin, amax, dmin, dmax])

    # ADM set up the dec boundaries in advance.
    step = np.radians(15)
    dmins = [dmin, dmax, dmax + step, dmax + 2*step]
    dmaxs = [dmax, dmax + step, dmax + 2*step, dmax + 3*step]

    # ADM a list of symbols/colors to use.
    symbols = ["-r", "-g", "-b", "-k"]
    for ddmin, ddmax, sym in zip(dmins, dmaxs, symbols):
        # ADM remember, the locations are now in radians, so need converted
        # ADM to degrees. Better, actually, would be to write a function
        # ADM that took inputs in radians.
        areasqdeg = area(np.degrees(amin), np.degrees(amax),
                         np.degrees(ddmin), np.degrees(ddmax))
        label = "Area: {:.3f} sq. deg.".format(areasqdeg)
        ax.plot([amin, amin, amax, amax, amin],
                [ddmin, ddmax, ddmax, ddmin, ddmin], sym, label=label)

    # NP Plotting final lat-lon rectangle 45 deg above the inputted rectangle with area labeled
    ax.grid(color='k', linestyle='solid', linewidth=0.5)
    # NP Adding grid so dimensions of rectangle can easily be obtained
    xlab = ['14h','16h','18h','20h','22h','0h','2h','4h','6h','8h','10h']
    ax.set_xticklabels(xlab, weight=800)
    # NP Labeling x-axis in hours
    plt.legend()
    # NP Creating a legend for the plot
    plt.title('Aitoff projection of lat-lon rectangles')
    # NP Creating a title for the plot
#    plt.savefig('/d/www/nikhil/public_html/ASTR5160/aitofflatlon.png')
    # NP Saving figure
    # ADM only you can write to your public_html directory! So, hardcoding
    # ADM a directory like this is not wise. Instead, I've set this up
    # ADM so the user specifies their own input directory.
    plt.savefig(os.path.join(plot_dir, 'aitofflatlon.png'))


def populatesphere(amin, amax, dmin, dmax, n):
    '''Takes right ascensions amin, amax and declinations dmin, dmax
    and returns the list of ras and decs that lie in the lat-lon rectangle
    drawn by amin, amax and dmin, dmax.

    ADM: n, here is the number of points to generate
    '''
    ra = 360.*(random(n))-180
    dec=(180/np.pi)*np.arcsin(1.-random(n)*2.)
    # NP Generating a set of 1000000 random points populated throughout the celestial sphere
    # ADM Excellent use of Boolean indexing!
    ii = (ra > amin) & (ra < amax) & (dec < dmax) & (dec > dmin)
    # NP Creating index of points contained in the lat-lon rectangle
    # NP returning a filtered list of points only inside the lat-lon rectangle.
    # ADM Python style is to leave a blank line before a return statement
    # ADM and to have no comments outside of a function.

    return ra[ii], dec[ii]


if __name__ == '__main__':
    # ADM note that indenting by 4 spaces is standard Python style.
    # ADM also note that Python style is to limit lines to ~70-80 characters.
    desc ="""Generates a lat-lon rectangle from inputted variables and plots
    the rectangle in an Aitoff Projection. Additionally generates 100000000
    random points across the entire sphere and calculates which points are
    contained in the defined lat-lon rectangle. The fraction of the number
    of the 100000000 points that are inside the defined lat-lon rectangle
    compared to the total number of points is compared to the fraction of
    the area of the lat-lot rectangle to the entire area of the sphere."""
    parser = argparse.ArgumentParser(description=desc)

    # ADM you can save some space here, even.
#	parser.add_argument('amin', metavar = 'amin', type = float, help = 'Minimum RA of the lat-lon rectangle. Expected input is in degrees. Values should be between -180 and +180.')
#	parser.add_argument('amax', metavar = 'amax', type = float, help = 'Maximum RA of the lat-lon rectangle. Expected input is in degrees. Values should be between -180 and +180')
#	parser.add_argument('dmin', metavar = 'dmin', type = float, help = 'Minimum DEC of the lat-lon rectangle. Expected input is in degrees. Values should be between -90 and +90')
#	parser.add_argument('dmax', metavar = 'dmax', type = float, help = 'Maximum DEC of the lat-lon rectangle. Expected input is in degrees. Values should be between -90 and +90')
    msg = '{} of the lat-lon rectangle. Expected input is in degrees. Values should be between {} and {}'
    parser.add_argument('amin', metavar='amin', type=float,
                        help=msg.format("Minimum RA", "-180", "+180"))
    parser.add_argument('amax', metavar='amax', type=float,
                        help=msg.format("Maximum RA", "-180", "+180"))
    parser.add_argument('dmin', metavar='dmin', type=float,
                        help=msg.format("Minimum DEC", "-90", "+90"))
    parser.add_argument('dmax', metavar='dmax', type=float,
                        help=msg.format("Maximum DEC", "-90", "+90"))
    # ADM I added this input.
    parser.add_argument('plot_dir', metavar= 'plot_dir', help = 'output directory for plots')
    args = parser.parse_args()

    # NP Adding parser
    print('Area of half of the sphere: '+str(area(0, 360, 0, 90))+' sq. deg.')
    #Answer is consistent with the area of a hemisphere
    print('Area of the lat-lon rectangle: '+str(area(args.amin, args.amax, args.dmin,
                                                     args.dmax))+' sq. deg.')
    # NP Printing area of the inputted lat-lon rectangle
    aitoffplot(args.amin, args.amax, args.dmin, args.dmax, args.plot_dir)

    # ADM let's use 100000000 points. That should be enough?
    n = 100000000

    # NP Generating Aitoff plot of the inputted lat-lon rectangle
    ralist, declist = populatesphere(args.amin, args.amax, args.dmin, args.dmax, n)

    # NP Generating points inside the lat-lon rectangle
    print('Ratio of points inside the lat-lon rectangle: '+str(len(ralist)/n))
    print('Ratio of area of the rectangle to the total area: '
          +str(round(area(args.amin, args.amax, args.dmin, args.dmax)/area(0, 360, -90, 90),6)))
    # NP These two numbers are almost exactly the same, as expected
    # ADM might be time to learn Python's mini string formatting language, 
    # ADM which is considered the professional way to write text and labels:
    print('Ratio of area of the rectangle to the total area: {:.6f}'.format(
        area(args.amin, args.amax, args.dmin, args.dmax)/area(0, 360, -90, 90)))
