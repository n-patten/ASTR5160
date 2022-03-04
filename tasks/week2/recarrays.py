from astropy.table import Table
import matplotlib.pyplot as plt
objs = Table.read("/d/scratch/ASTR5160/week2/struc.fits")#reading file
plt.plot(objs["RA"],objs["DEC"],'bx')#plotting dec vs ra
plt.xlabel("RA")#adding labels
plt.ylabel("DEC")
plt.savefig("/d/scratch/ASTR5160/week2/ravsdecplot.png")#saving figure, task 1
for x,y in zip(objs[(objs["EXTINCTION"][...,0]>.22)]["RA",objs[(objs["EXTINCTION"][...,0]>.22)]["DEC"]):
               label = f"({x},{y})"
               plt.annotate(label,(x,y),textcoords="offset points",xytext=(0,10),ha='center')#labeling all points with extinction >.22 in first column, im not sure if this is right, i had some trouble figuring out how to test for loops in ipython
plt.savefig("/d/scratch/ASTR5160/week2/labeledplot.png")#saving figure
