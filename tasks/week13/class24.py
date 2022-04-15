import numpy as np
import matplotlib.pyplot as plt
# NP Necessary imports

data = np.loadtxt('/d/scratch/ASTR5160/week13/line.data')
# NP Loading in data

def printdiag(data):
	covar = np.cov(data, ddof = 1)
	print('Diagonal of the covariant matrix:')
	for i in range(len(covar)):
		print(covar[i][i])
# NP Defining function to print diagonal of the covariant matrix

printdiag(data)
# NP Printing diagonal of the covaraint matrix

def printvars(data):
	print('Variances of each data point:')
	for i in range(len(data)):
		print(np.var(data[i], ddof = 1))
# NP Defining function to print the varaince of the data

printvars(data)
# NP Printing data variances
# NP Both print the same thing, diagonal of the covariant matrix are
# NP the variance of the data
# NP The covariant matrix should be 20x20 because there are 20 data points
# NP to measure how they change with each other.

corr = np.corrcoef(data)
# NP Defining correlation matrix

sortcorr = np.sort(corr.flatten())
# NP Sorting correlation matrix

print('Most correlated data at: \n' +str(np.where(corr == sortcorr\
	[len(sortcorr) - 1])))
print('with value of ' +str(corr[np.where(corr == sortcorr[len(sortcorr)\
	- 1])][0]))
# NP Printing the most correlated data by printing the value and index of
# NP maximumum of the correlation matrix

print('Most anti-correlated data at: \n' +str(np.where(corr ==\
	sortcorr[0])))
print('with value of ' +str(corr[np.where(corr == sortcorr[0])][0]))
# NP Printing the least correlated data by printing the value and index of
# NP minimum of the correlation matrix

print('Most correlated data not on diagonal at: \n' +str(np.where(corr\
	== sortcorr[len(sortcorr) - 21])))
print('with value of ' +str(corr[np.where(corr == sortcorr[len(sortcorr)\
	- 21])][0]))
# NP Printing the most correlated data  not on the diagonal by printing the
# NP value and index of maximum of the correlation matrix 20 indices in
# NP (excluding 20 places because of diagonal).
