import emcee
import corner
import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt
from scipy.optimize import minimize
# NP Necessary imports

def log_likelihood(theta, x, y, yerr):
	'''Gaussian function for fitting a linear line with reduced variance
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	Inputs:
	theta: array. An array containing the parameters to fit the line.
	The first item is expected to be the slope and the second is
	expected to be the y-intercept.
	x: array. An array of x-values for the data you want to fit.
	y: array. An array of y-values for the data you want to fit.
	yerr: array. An array of values corresponding to the error in y.
	Outputs:
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	float. The likelihood that the given parameters fit the data.'''
	m, b = theta
	model = np.multiply(m,x) + b
	# NP Defining model line from inputted slope and intercept
	sigma2 = yerr
	return -0.5 * np.sum((y - model) ** 2 / sigma2 + np.log(sigma2))
	# NP Calculating and returning likelihood

def log_likelihood2(theta, x, y, yerr):
	'''Gaussian function for fitting a quadratic line with reduced variance
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	Inputs:
	theta: array. An array containing the parameters to fit the parabola.
	The first item is expected to be the quadratic term, the second
	 is the linear term and the third is the zeroth order constant.
	x: array. An array of x-values for the data you want to fit.
	y: array. An array of y-values for the data you want to fit.
	yerr: array. An array of values corresponding to the error in y.
	Outputs:
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	float. The likelihood that the given parameters fit the data.'''
	a2, a1, a0 = theta
	model = np.multiply(a2, np.square(x)) +np.multiply(a1, x) + a0
	# NP Defining model quadratic function from inputted coefficients
	sigma2 = yerr
	return -0.5 * np.sum((y - model) ** 2 / sigma2 + np.log(sigma2))
	# NP Calculating and returning likelihood

def log_prior(theta):
	'''Function for determining priors on m and b to limit search
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	Inputs:
	theta: array. An array containing the parameters to fit the line.
	The first item is expected to be the slope and the second is
	expected to be the y-intercept.
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	float. The probability that the given parameters fit the data.
	0 probability for m and b in certain ranges and 100% probability
	for different ranges.'''
	m, b = theta
	if -1.3 < m < 0.5 and 0 < b < 7:
		return 0.0
	# NP Only accepting value of m between -1.3 and 0.5 and values
	# NP of b between 0 and 7
	return -np.inf

def log_prior2(theta):
	'''Function for determining priors on m and b to limit search
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	Inputs:
	theta: array. An array containing the parameters to fit the parabola.
	The first item is expected to be the quadratic term, the second
	 is the linear term and the third is the zeroth order constant.
	The first item is expected to be the slope and the second is
	expected to be the y-intercept.
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	float. The probability that the given parameters fit the data.
	0 probability for m and b in certain ranges and 100% probability
	for different ranges.'''
	a2, a1, a0 = theta
	if -0.1 < a2 < 0.14 and -4.0 < a1 <0 and 2 < a0 < 13:
		return 0.0
	# NP Only accepting value of a2 between -0.1 and 0.14, a1 between
	# NP -4 and 0, and a0 between 2 and 13
	return -np.inf

def log_probability(theta, x, y, yerr):
	'''Full probability function for determining the fit of a model
	to data
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	Inputs:
	theta: array. An array containing the parameters to fit the line.
	The first item is expected to be the slope and the second is
	expected to be the y-intercept.
	x: array. An array of x-values for the data you want to fit.
	y: array. An array of y-values for the data you want to fit.
	yerr: array. An array of values corresponding to the error in y.
	Outputs:
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	float. The probability that the given parameters fit the data.'''
	lp = log_prior(theta)
	if not np.isfinite(lp):
		return -np.inf
	return lp + log_likelihood(theta, x, y, yerr)

def log_probability2(theta, x, y, yerr):
	'''Full probability function for determining the fit of a model
	to data
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	Inputs:
	theta: array. An array containing the parameters to fit the parabola.
	The first item is expected to be the quadratic term, the second
	 is the linear term and the third is the zeroth order constant.
	x: array. An array of x-values for the data you want to fit.
	y: array. An array of y-values for the data you want to fit.
	yerr: array. An array of values corresponding to the error in y.
	Outputs:
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	float. The probability that the given parameters fit the data.'''
	lp = log_prior2(theta)
	if not np.isfinite(lp):
		return -np.inf
	return lp + log_likelihood2(theta, x, y, yerr)

def linear(x, y, variances):
	'''Function for determining best-fit parameters for line fit to data
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	Inputs:
	x: array. An array of x-values for the data you want to fit.
	y: array. An array of y-values for the data you want to fit.
	yerr: array. An array of values corresponding to the error in y.
	Outputs:
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	none.
	Sourced from:
	https://emcee.readthedocs.io/en/stable/tutorials/line/'''
	m_true = -0.91
	b_true = 3.33
	# NP Inital guesses at slope and intercept based on previous
	# NP runs of this code
	nll = lambda *args: -log_likelihood(*args)
	initial = np.array([m_true, b_true]) + 0.1 * np.random.randn(2)
	soln = minimize(nll, initial, args=(x, y, variances))
	pos = soln.x + 1e-4 * np.random.randn(32, 2)
	nwalkers, ndim = pos.shape
	sampler = emcee.EnsembleSampler(
	nwalkers, ndim, log_probability, args=(x, y, variances))
	sampler.run_mcmc(pos, 5000, progress=True);
	flat_samples = sampler.get_chain(discard=100, thin=15, flat=True)
	labels = ["m", "b"]
	# NP The process of fitting functions to the data was taken directly
	# NP from the emcee tutorial page.
	for i in range(ndim):
		mcmc = np.percentile(flat_samples[:, i], [16, 50, 84])
		q = np.diff(mcmc)
		txt = "{{{3}}} = {0:.5f}-{1:.5f}+{2:.5f}"
		txt = txt.format(mcmc[1], q[0], q[1], labels[i])
		print(txt)
		# NP Printing value of m and b to command line
	mguess = np.percentile(flat_samples[:, 0], [50])
	bguess = np.percentile(flat_samples[:, 1], [50])
	# NP Extracting most probable results for m and b
	xfit = np.linspace(1, 20, 100)
	yfit = np.multiply(mguess, xfit) +bguess
	# Generated fitted function
	fig, ax = plt.subplots()
	fig.set_figwidth(8)
	fig.set_figheight(6)
	# NP Making figure larger
	ax.errorbar(x, y, yerr=np.sqrt(variances),capsize=4, color = 'b',\
		fmt = 'o', label = 'data')
	ax.plot(xfit, yfit, 'r', label = 'trendline\nm: '\
		+str(float(np.round(mguess, 5)))
		+'\nb: ' +str(float(np.round(bguess, 5))))
	plt.legend()
	# NP Plotting generated fit to data
	flat_samples = sampler.get_chain(discard=100, thin=15, flat=True)
	fig = corner.corner(flat_samples, labels = labels,\
		truths=[mguess[0], bguess[0]])
	# NP Generating corner plots
	plt.show()
	# NP Displaying graphs

def quadratic(x, y, variances):
	'''Function for determining best-fit parameters for quadratic\
	 fit to data
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	Inputs:
	x: array. An array of x-values for the data you want to fit.
	y: array. An array of y-values for the data you want to fit.
	yerr: array. An array of values corresponding to the error in y.
	Outputs:
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	none.
	Sourced from:
	https://emcee.readthedocs.io/en/stable/tutorials/line/'''
	a2_true = 0.05937
	a1_true = -2.146
	a0_true = 7.75
	# NP Initial guess on coefficients, obtanied from running code
	# NP previously
	nll = lambda *args: -log_likelihood2(*args)
	initial = np.array([a2_true, a1_true, a0_true]) + 0.1 *\
		np.random.randn(3)
	soln = minimize(nll, initial, args=(x, y, variances))
	pos = soln.x + 1e-4 * np.random.randn(32, 3)
	nwalkers, ndim = pos.shape
	sampler = emcee.EnsembleSampler(
		nwalkers, ndim, log_probability2, args=(x, y, variances))
	sampler.run_mcmc(pos, 5000, progress=True);
	# NP The above code is sourced from the link in the help command
	# NP for this functions
	flat_samples = sampler.get_chain(discard=100, thin=15, flat=True)
	labels = ["a2", "a1", "a0"]
	for i in range(ndim):
		mcmc = np.percentile(flat_samples[:, i], [16, 50, 84])
		q = np.diff(mcmc)
		txt = "{{{3}}} = {0:.5f}-{1:.5f}+{2:.5f}"
		txt = txt.format(mcmc[1], q[0], q[1], labels[i])
		print(txt)
		# NP Printing values of a2, a1 and a0 to command line
	a2guess = np.percentile(flat_samples[:, 0], [50])
	a1guess = np.percentile(flat_samples[:, 1], [50])
	a0guess = np.percentile(flat_samples[:, 2], [50])
	# NP Extracting most probable results for a2, a1 and a0
	xfit = np.linspace(2, 20, 100)
	yfit = np.multiply(a2guess,(np.square(xfit)))\
		+np.multiply(a1guess, xfit) +a0guess
	# NP Generating fitted function
	fig, ax = plt.subplots()
	fig.set_figwidth(8)
	fig.set_figheight(6)
	# NP Making figure larger
	ax.errorbar(x, y, yerr=np.sqrt(variances),capsize=4,\
		color = 'b', fmt = 'o', label = 'data')
	ax.plot(xfit, yfit, 'r', label = 'trendline'
		'\na2: ' +str(float(np.round(a2guess, 5)))\
		+'\na1: ' +str(float(np.round(a1guess, 5)))\
		+'\na0: ' +str(float(np.round(a0guess, 5))))
	plt.legend()
	# NP Plotting generated fit to data		
	flat_samples = sampler.get_chain(discard=100, thin=15, flat=True)
	fig = corner.corner(flat_samples, labels = labels,\
		truths=[a2guess[0], a1guess[0], a0guess[0]])
	# NP Generating corner plots
	plt.show()

if(__name__ == '__main__'):
	data = fits.getdata("/d/scratch/ASTR5160/final/dataxy.fits")
	# NP Reading in data
	x = [data[i][0] for i in range(len(data))]
	y = [data[i][1] for i in range(len(data))]
	variances = np.square([data[i][2] for i in range(len(data))])
	# NP Creating arrays the correspond to x, y, and variances for data
	linear(x, y, variances)
	# NP Generating linear fit to the data
	quadratic(x, y, variances)
	# NP Generating quadratic fit to the data
	print('Looking at the posterior probability distribution for'
		'\na2, the probability for a2 being 0 is about three sigma'
		'\naway from the most probable value for a2. Therefore,'
		'\nit is very unlikely that a2, the quadratic term, is 0.'
		'\nThis means there is ~99.7% chance that the quadratic fit'
		'\nwas the correct choice for this data.')
