import numpy as np 
import sys
import scipy.spatial as sp
import copy

fibres=sys.argv[1]
norms=sys.argv[2]

print('Reading mesh...')
fibres_lon = np.loadtxt(fibres+'.lon',dtype=float,skiprows=1)
fibres_pts = np.loadtxt(fibres+'.pts',dtype=float,skiprows=1)
fibres_elem = np.loadtxt(fibres+'.elem',dtype=int,skiprows=1,usecols=[1,2,3])
print('Done')

print('Reading gradient...')
norms_grad = np.loadtxt(norms,dtype=float)
print('Done')

# find the axes of rotation

axis_normalised = np.zeros((fibres_elem.shape[0],3), dtype=float)

for i,l in enumerate(fibres_lon):
	axis = np.cross(fibres_lon[i],norms_grad[i])
	axis_normalised[i,:] = axis/np.linalg.norm(axis)

np.savetxt(fibres+'_axis.lon',axis_normalised,fmt="%g",header='1',comments='')








