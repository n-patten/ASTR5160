import numpy as np
import matplotlib.pyplot as plt
import argparse
from numpy.random import random
# NP Necessary imports

def area(amin, amax, dmin, dmax):
    '''Returns the area in square degrees of a rectangle bounded by amin, 
    amax, dmin and dmax. All inputs must be inputted in degrees.'''
    a = (np.pi/180*(amax-amin))*(np.sin(dmax*np.pi/180)-np.sin(dmin*np.pi/180))
    # NP Calculating the area in str first using the equation in the lecture notes.
    adeg = a*(180/np.pi)**2
    # NP Converting this answer into square degrees
    return adeg

def aitoffplot(amin, amax, dmin, dmax):
    '''Inputs right ascensions amin and amax and declinations dmin and dmax in degrees
    and generates an aitoff projection of the lat-lon rectangles spanning 15 degree
    declination icrements and labels their areas'''
    fig = plt.figure()
    fig.set_figwidth(15)
    fig.set_figheight(15)
    # NP Changing the size of the plot so that the title is able to be read
    ax = fig.add_subplot(111, projection="aitoff")
    # NP Creating an aitoff plot
    ax.plot([amin*np.pi/180,amin*np.pi/180,amax*np.pi/180,amax*np.pi/180,amin*np.pi/180],
            [(dmin)*np.pi/180,(dmax)*np.pi/180,(dmax)*np.pi/180,(dmin)*np.pi/180,
             (dmin)*np.pi/180],'-r', label = 'Area:'+str(np.round(area(amin, amax, dmin, dmax)
            ,3))+' sq. deg.')
    # NP Plotting the inputted lat-lon rectangle with label corresponding to area
    ax.plot([amin*np.pi/180,amin*np.pi/180,amax*np.pi/180,amax*np.pi/180,amin*np.pi/180],
            [(dmax+0)*np.pi/180,(dmax+15)*np.pi/180,(dmax+15)*np.pi/180,(dmax+0)*np.pi/180,
             (dmax+0)*np.pi/180],'-g', label = 'Area:'+str(np.round(area(amin, amax, dmax,
            dmax+15),3))+' sq. deg.')
    # NP Plotting another lat-lon rectangle 15 deg above the inputted rectangle with area labeled
    ax.plot([amin*np.pi/180,amin*np.pi/180,amax*np.pi/180,amax*np.pi/180,amin*np.pi/180],
            [(dmax+15)*np.pi/180,(dmax+30)*np.pi/180,(dmax+30)*np.pi/180,(dmax+15)*np.pi/180,
             (dmax+15)*np.pi/180],'-b', label = 'Area:'+str(np.round(area(amin, amax, dmax+15,
            dmax+30),3))+' sq. deg.')
    # NP Plotting another lat-lon rectangle 30 deg above the inputted rectangle with area labeled
    ax.plot([amin*np.pi/180,amin*np.pi/180,amax*np.pi/180,amax*np.pi/180,amin*np.pi/180],
            [(dmax+30)*np.pi/180,(dmax+45)*np.pi/180,(dmax+45)*np.pi/180,(dmax+30)*np.pi/180,
             (dmax+30)*np.pi/180],'-k', label = 'Area:'+str(np.round(area(amin, amax, dmax+30,
            dmax+45),3))+' sq. deg.')
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
    plt.savefig('/d/www/nikhil/public_html/ASTR5160/aitofflatlon.png')
    # NP Saving figure

def populatesphere(amin, amax, dmin, dmax):
    '''Takes right ascensions amin, amax and declinations dmin, dmax
    and returns the list of ras and decs that lie in the lat-lon rectangle
    drawn by amin, amax and dmin, dmax.'''
    ra = 360.*(random(1000000))-180
    dec=(180/np.pi)*np.arcsin(1.-random(1000000)*2.)
    # NP Generating a set of 1000000 random points populated throughout the celestial sphere
    ii = (ra > amin) & (ra < amax) & (dec < dmax) & (dec > dmin)
    # NP Creating index of points contained in the lat-lon rectangle
    return ra[ii], dec[ii]
    # NP returning a filtered list of points only inside the lat-lon rectangle.

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description = '')
	parser.add_argument('amin', metavar = 'amin', type = float, help = 'Minimum RA of the lat-lon rectangle. Expected input is in degrees.')
	parser.add_argument('amax', metavar = 'amax', type = float, help = 'Maximum RA of the lat-lon rectangle. Expected input is in degrees.')
	parser.add_argument('dmin', metavar = 'dmin', type = float, help = 'Minimum DEC of the lat-lon rectangle. Expected input is in degrees.')
	parser.add_argument('dmax', metavar = 'dmax', type = float, help = 'Maximum DEC of the lat-lon rectangle. Expected input is in degrees.')
	args = parser.parse_args()
	# NP Adding parser
	print('Area of half of the sphere: '+str(area(0, 360, 0, 90))+' sq. deg.')
	#Answer is consistent with the area of a hemisphere
	print('Area of the lat-lon rectangle: '+str(area(args.amin, args.amax, args.dmin,
	args.dmax))+'sq. deg.')
	# NP Printing area of the inputted lat-lon rectangle
	aitoffplot(args.amin, args.amax, args.dmin, args.dmax)
	# NP Generating Aitoff plot of the inputted lat-lon rectangle
	ralist, declist = populatesphere(args.amin, args.amax, args.dmin, args.dmax)
	# NP Generating points inside the lat-lon rectangle
	print('Ratio of points inside the lat-lon rectangle: '+str(len(ralist)/1000000))
	print('Ratio of area of the rectangle to the total area: '
	+str(round(area(args.amin, args.amax, args.dmin, args.dmax)/area(0, 360, -90, 90),6)))
	# NP These two numbers are almost exactly the same, as expected
    
