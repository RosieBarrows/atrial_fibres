import numpy as np 
import sys
import scipy.spatial as sp
import copy

fibres_mshName_endo=sys.argv[1]
la_mshName=sys.argv[2]
output_folder=sys.argv[3]
fibres_ECs=sys.argv[4]
la_ECs=sys.argv[5]
uvcs=sys.argv[6]
fibres_mshName_epi=sys.argv[7]

print('Reading endo mesh...')

endo_lon = np.loadtxt(fibres_mshName_endo+'.lon',dtype=float,skiprows=1)
endo_pts = np.loadtxt(fibres_mshName_endo+'.pts',dtype=float,skiprows=1)
endo_elem = np.loadtxt(fibres_mshName_endo+'.elem',dtype=int,skiprows=1,usecols=[1,2,3,4])
print('Done')

print('Reading epi mesh...')

epi_lon = np.loadtxt(fibres_mshName_epi+'.lon',dtype=float,skiprows=1)
epi_pts = np.loadtxt(fibres_mshName_epi+'.pts',dtype=float,skiprows=1)
epi_elem = np.loadtxt(fibres_mshName_epi+'.elem',dtype=int,skiprows=1,usecols=[1,2,3,4])
print('Done')

print('Reading endo element centres...')
endo_elemC = np.loadtxt(fibres_ECs,dtype=float,skiprows=1)
print('Done')

print('Reading vol mesh...')

la_lon = np.loadtxt(la_mshName+'.lon',dtype=float,skiprows=1)
la_pts = np.loadtxt(la_mshName+'.pts',dtype=float,skiprows=1)
la_elem = np.loadtxt(la_mshName+'.elem',dtype=int,skiprows=1,usecols=[1,2,3,4])
print('Done')

print('Reading vol element centres...')
la_elemC = np.loadtxt(la_ECs,dtype=float,skiprows=1)
print('Done')

print('Reading uvcs...')
UVCs = np.loadtxt(uvcs,dtype=float)
print('Done')

to_be_endo_rows=[]
to_be_epi_rows=[]

for i,u in enumerate(UVCs):
	if u <= 0.5:
		to_be_endo_rows.append(i)
	else:
		to_be_epi_rows.append(i)

endo_distance_tree = sp.cKDTree(endo_elemC)
new_la_lon = copy.deepcopy(la_lon)

for idx in to_be_endo_rows:
	new_la_lon[idx] = endo_lon[endo_distance_tree.query(la_elemC[idx])[1]]

for idx in to_be_epi_rows:
	new_la_lon[idx] = epi_lon[endo_distance_tree.query(la_elemC[idx])[1]]

np.savetxt(output_folder+'/fibres_from_uvc.lon',new_la_lon,fmt="%g",header='1',comments='')
