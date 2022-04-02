import pymangle
import matplotlib.pyplot as plt # NP Necessary imports

minter = pymangle.Mangle("/d/users/nikhil/ASTR5160/week6/intersection.ply")
mboth = pymangle.Mangle("/d/users/nikhil/ASTR5160/week6/bothcaps.ply")
# NP Creating both masks
# NP minter is the overlap of the two caps
# NP mboth are both caps drawn together
ra1, dec1 = minter.genrand(10000)
ra2, dec2 = mboth.genrand(10000)
# NP Generating 10,000 points to see the shape of both masks

f = plt.figure()
f.set_figwidth(8)
f.set_figheight(5)
# NP Making figure larger
plt.plot(ra2, dec2, '.g', label = 'Two caps overlapped')
plt.plot(ra1, dec1, '.r', label = 'Intersection of two caps')
# NP Plotting both masks
plt.title('Overplot of two spherical caps')
plt.xlabel('RA (deg)')
plt.ylabel('Dec (deg)')
plt.legend()
# NP Labelling axes and title of the plot
plt.savefig('/d/www/nikhil/public_html/ASTR5160/Mangle.png')
# NP Saving figure
# NP As seen in the plots, minter shows the overlap of the two spherical
# NP caps while mboth show both caps together
# NP Task 3 complete

mflip1 = pymangle.Mangle("/d/users/nikhil/ASTR5160/week6/flip.ply")
ra3, dec3 = mflip1.genrand(10000)
# NP Reading in flip.ply and generating 10,000 points to deduce shape

f.set_figwidth(8)
f.set_figheight(5)
# NP Making plot larger
plt.plot(ra3, dec3, '.r', label = 'Excluded area of cap 1')
plt.plot(ra1, dec1, '.g', label = 'Intersection of two caps')
# NP Plotting both masks to deduce shape
plt.title('Overplot of two spherical caps')
plt.xlabel('RA (deg)')
plt.ylabel('Dec (deg)')
plt.legend()
# NP Labelling axes and title of the plot
plt.savefig('/d/www/nikhil/public_html/ASTR5160/flip.png')
# NP Saving figure
# NP Flipping the constraint of the cap1 now shoes the region of cap1 that is
# NP does not overlap with the other spherical cap
# NP Task 4 complete
