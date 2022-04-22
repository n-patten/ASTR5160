import random
import numpy as np
# NP Necessary imports

data = np.loadtxt("/d/scratch/ASTR5160/week13/line.data")
# NP Loading in data table
means = np.mean(data, 0)
# NP Calculating means
variances = np.var(data, 0, ddof = 1)
# NP Calculating variances

def postprob(m, b):
	# NP Creating a function to calculate the posterior probability
	bins = np.arange(0,10) +0.5
	lnL = 0
	if(0 < b < 8):
	# NP Checking if b is in an acceptible range
		for mean, binx, var in zip(means, bins, variances):
			lnL += -0.5*(((mean-(m*binx+b))**2)/(var**2)\
				+np.log(2*np.pi*var**2))
	else:
		lnL = -np.inf
	return lnL

slopes = np.array(np.repeat(0,10000), dtype = float)
slopes[0] = 3.0
# NP Generating an empty list of slopes with an inital guess
ints = np.array(np.repeat(0,10000), dtype = float)
ints[0] = 4.7
# NP Generating an empty list of intercepts with an inital guess
for i in range(len(slopes)-1):
	curslope = slopes[i]
	propslope = random.gauss(slopes[i], 0.1)
	curint = ints[i]
	propint = random.gauss(ints[i], .1)
	# NP Deviating from guess with Gaussian
	R = postprob(propslope, propint) - postprob(curslope, curint)
	if(np.exp(R) > 1):
		slopes[i+1] = propslope
		ints[i+1] = propint
		# NP If guess was better than previous guess, then accept
		# NP new value
	else:
		slopes[i+1] = curslope
		ints[i+1] = curint
		# NP Otherwise, continute using old value

print('Best Slope: ' +str(slopes[len(slopes)-1]) +'\nBest Intercept: '\
	+str(ints[len(ints) -1]))
# NP Printing best fit parameters
