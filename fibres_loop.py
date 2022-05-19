import numpy as np 
import sys
import scipy.spatial as sp
import copy

mshName=sys.argv[1]

print('Reading mesh...')

lon = np.loadtxt(mshName+'.lon',dtype=float,skiprows=1)
pts = np.loadtxt(mshName+'.pts',dtype=float,skiprows=1)
elem = np.loadtxt(mshName+'.elem',dtype=int,skiprows=1,usecols=[1,2,3,4])
print('Done')

print('Reading element centres...')
elemC = np.loadtxt(mshName+'_elem_centres.pts',dtype=float,skiprows=1)
print('Done')

default_fibre_rows=[]
fibre_rows=[]

for i,l in enumerate(lon):
	# if lon[row] == np.array([1,0,0]):
	if l[0] == 1.:
		default_fibre_rows.append(i)
	else:
		fibre_rows.append(i)

distance_tree = sp.cKDTree(elemC[fibre_rows])
new_lon = copy.deepcopy(lon)
for idx in default_fibre_rows:
	new_lon[idx] = lon[fibre_rows[distance_tree.query(elemC[idx])[1]]]

np.savetxt(mshName+'_corrected.lon',new_lon,fmt="%g",header='1',comments='')