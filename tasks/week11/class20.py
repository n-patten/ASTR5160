import argparse
import numpy as np
import matplotlib.pyplot as plt
from sklearn import neighbors
from sklearn.datasets import load_iris
from tasks.week11.class19 import whichquasars, limitsweeps, getpsf, readsweeps

def algorithm(path):
	sweep = readsweeps(180, 30)
	# NP Reading in sweep
	cutsweeps = limitsweeps(sweep, 20)
	# NP Limiting sweeps by r<20
	psfobjs = getpsf(180, 30, 3, cutsweeps)
	# Limiting sweep objects to be within 3 deg. of (a,d) = (180, 30)

	qsos = whichquasars(psfobjs)
	# NP Searching for known quasars found in the sweep
	s = psfobjs[6002:6277]
	# NP Assuming random subset of psfs are stars
	# NP Making a plot of r-W1 vs. g-z for quasars and star subset
	f = plt.figure()
	f.set_figwidth(8)
	f.set_figheight(6)
	# NP Making figure larger
	W1q = 22.5-2.5*np.log10(qsos['FLUX_W1']/qsos['MW_TRANSMISSION_W1'])
	gq = 22.5-2.5*np.log10(qsos['FLUX_G']/qsos['MW_TRANSMISSION_G'])
	rq = 22.5-2.5*np.log10(qsos['FLUX_R']/qsos['MW_TRANSMISSION_R'])
	zq = 22.5-2.5*np.log10(qsos['FLUX_Z']/qsos['MW_TRANSMISSION_Z'])
	W1s = 22.5-2.5*np.log10(s['FLUX_W1']/s['MW_TRANSMISSION_W1'])
	gs = 22.5-2.5*np.log10(s['FLUX_G']/s['MW_TRANSMISSION_G'])
	rs = 22.5-2.5*np.log10(s['FLUX_R']/s['MW_TRANSMISSION_R'])
	zs = 22.5-2.5*np.log10(s['FLUX_Z']/s['MW_TRANSMISSION_Z'])
	# NP Definining relevant magnitudes
	rminusW1q = rq.value-W1q.value
	gminuszq = gq.value-zq.value
	rminusW1s = rs.value-W1s.value
	gminuszs = gs.value-zs.value
	# NP Defining colors to be plotted
	plt.scatter(gminuszs, rminusW1s, s = 2, color = 'black', label = 'Star')
	plt.scatter(gminuszq, rminusW1q, s = 2, color = 'red', label = 'Quasars')
	# NP Scattering quasars and stars
	plt.xlabel('g-z')
	plt.ylabel('r-W1')
	plt.title('Color-color plot of Quasars and Stars')
	# NP Labeling figure
	plt.legend()
	# NP Creating legend
	plt.savefig(path+'/QuasarsstarML1.png')
	# NP Saving figure

	qdata = [gminuszq, rminusW1q]
	sdata = [gminuszs, rminusW1s]
	# NP Combining star and quasar data inton one array
	data = np.concatenate((qdata, sdata), axis = 0)
	print(np.reshape(data, (2, 550)).T)
	shapeddata = np.reshape(data, (2, 550)).T
	# NP Shaping the array to be used by the algorithm
	identity = []
	for i in range(275):
		identity.append(0)
	for i in range(275):
		identity.append(1)
	# NP Creating a list of identities for each point for fitting algorithm
	print(len(identity))

	knn1 = neighbors.KNeighborsClassifier(n_neighbors=1)
	knn1.fit(shapeddata, identity)
	# NP Fitting the data

	n = 100000
	colnames = "r-W1 g-z" 
	mock_data = []
	for i in range(2):
		print("working on column: {}".format(colnames.split()[i]))
		col_min = np.min(shapeddata[..., i])
		col_max = np.max(shapeddata[..., i])
		mock_meas = np.random.random(n)*(col_max - col_min) + col_min
		mock_data.append(mock_meas)
	qtargetnames = ['Quasar', 'Star']
	mock_data = np.reshape(mock_data, (2, n)).T
	mock_data
	# NP Generating random data between the maximum and minimum values of the real data

	fig, ax = plt.subplots(1, 1, figsize=(8,6))
	colors = ['red', 'black']
	mock_target_class = knn1.predict(mock_data)
	for i in range(2):
		target_class = mock_target_class == i
		ax.scatter(mock_data[target_class, 0], mock_data[target_class, 1], s=10,
			label=qtargetnames[i], color = colors[i])
		ax.tick_params(labelsize=14)
		ax.set_xlabel("g-z", size=14)
		ax.set_ylabel("r-W1", size=14)
		ax.legend(prop={'size': 14})
	# NP Plotting the generated data classified using the fitting algorithm to
	# NP see the regions in which each object occupies on the color-color
	# NP diagram.
	plt.savefig(path+'/starsquasarspedictedML.png')
	# NP Saving figure

if (__name__ == '__main__'):
	parser = argparse.ArgumentParser(description='Use an algorithm to classify quasars.')
	parser.add_argument('path', type=str, help='path of file save location for graphs')
	args = parser.parse_args()
	iris = load_iris()
	n = 100000
	mock_data = []
	colnames = "sepal_length sepal_width petal_length petal_width" 
	for i in range(2):
		print("working on column: {}".format(colnames.split()[i]))
		col_min = np.min(iris.data[..., i])
		col_max = np.max(iris.data[..., i])
		mock_meas = np.random.random(n)*(col_max - col_min) + col_min
		mock_data.append(mock_meas)
	mock_data = np.reshape(mock_data, (2, n)).T
	mock_data
	knn = neighbors.KNeighborsClassifier(n_neighbors=1)
	knn.fit(iris.data[..., :2], iris.target)
	mock_target_class = knn.predict(mock_data)
	# NP Generating iris data
	ii = iris.target_names[mock_target_class] == 'virginica'
	# NP Limiting selection to virginica irises
	print(len(mock_data[ii])/len(mock_data))
	# NP Prints:
	# NP 0.44023
	# NP Approximately 44% of generated irises are virginica
	# NP Task 1 complete
	algorithm(args.path)
