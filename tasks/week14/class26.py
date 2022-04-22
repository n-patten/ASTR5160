import emcee
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize
# NP Necessary imports

data = np.loadtxt("/d/scratch/ASTR5160/week13/line.data")
# NP Reading in data
means = np.mean(data, 0)
variances = np.var(data, 0, ddof = 1)
# NP Calculating means and variances
x = np.linspace(0, 9, 10) +0.5
# NP Defining x-bins

def log_likelihood(theta, x, y, yerr):
	m, b = theta
	model = m * x + b
	sigma2 = variances**2
	return -0.5 * np.sum((y - model) ** 2 / sigma2 + np.log(sigma2))

def log_probability(theta, x, y, yerr):
	lp = log_prior(theta)
	if not np.isfinite(lp):
		return -np.inf
	return lp + log_likelihood(theta, x, y, yerr)

def log_prior(theta):
	m, b = theta
	if -5.0 < m < 0.5 and 0.0 < b < 10.0:
		return 0.0
	return -np.inf
# NP All functions imported from tutorial
# NP Found at: https://emcee.readthedocs.io/en/stable/tutorials/line/

m_true = 3
b_true = 4.7
# NP Defining guess at slope and intercepts
# NP The following code was adapted from the same tutorial
nll = lambda *args: -log_likelihood(*args)
initial = np.array([m_true, b_true]) + 0.1 * np.random.randn(2)
soln = minimize(nll, initial, args=(x, means, variances))

pos = soln.x + 1e-4 * np.random.randn(32, 2)
nwalkers, ndim = pos.shape
sampler = emcee.EnsembleSampler(
    	nwalkers, ndim, log_probability, args=(x, means, variances))
sampler.run_mcmc(pos, 5000, progress=True);

from IPython.display import display, Math
flat_samples = sampler.get_chain(discard=100, thin=15, flat=True)
labels = ["m", "b"]
for i in range(ndim):
	mcmc = np.percentile(flat_samples[:, i], [16, 50, 84])
	q = np.diff(mcmc)
	txt = "\mathrm{{{3}}} = {0:.5f}_{{-{1:.5f}}}^{{{2:.5f}}}"
	txt = txt.format(mcmc[1], q[0], q[1], labels[i])
	display(Math(txt))
	print(txt)
	# NP Printing results
	# NP Prints:
	# NP m = 3.02905+0.00012-0.00007
	# NP b = 4.65309+0.00008-0.00007
