import numpy as np 
import matplotlib.pyplot as plt
import sys
import scipy.spatial as sp
import copy

path="/data/Dropbox/Segmentations/2016111001EP/final_heart/RA_endo_fch/fibres_inc_uvc/"
fibres="/data/Dropbox/Segmentations/2016111001EP/final_heart/RA_endo_fch/fibres_inc_uvc/fibres_from_uvc"
sheets="/data/Dropbox/Segmentations/2016111001EP/final_heart/RA_endo_fch/fibres_inc_uvc/fibres_from_uvc_sheet"

print('Reading mesh...')
fibres_lon = np.loadtxt(fibres+'.lon',dtype=float,skiprows=1)
fibres_pts = np.loadtxt(fibres+'.pts',dtype=float,skiprows=1)
fibres_elem = np.loadtxt(fibres+'.elem',dtype=int,skiprows=1,usecols=[1,2,3])
print('Done')

print('Reading mesh...')
sheets_lon = np.loadtxt(sheets+'.lon',dtype=float,skiprows=1)
sheets_pts = np.loadtxt(sheets+'.pts',dtype=float,skiprows=1)
sheets_elem = np.loadtxt(sheets+'.elem',dtype=int,skiprows=1,usecols=[1,2,3])
print('Done')

ra_fibres = np.concatenate((fibres_lon,sheets_lon),axis=1)
np.savetxt(path+'ra_fibres.lon',ra_fibres,fmt="%g",header='2',comments='')

#check that the dot product of the fibre direction and sheet direction is zero

orthog = np.zeros((fibres_lon.shape[0],1), dtype=float)
dot_prod = np.zeros((fibres_lon.shape[0],1), dtype=float)

for i,f in enumerate(fibres_lon):
	#orthog[i] = np.arccos(np.dot(fibres_lon[i],sheets_lon[i]))
	dot_prod[i] = np.dot(fibres_lon[i],sheets_lon[i])

#plt.scatter(range(len(fibres_lon)), 180*orthog/np.pi, marker = '.')
plt.scatter(range(len(fibres_lon)), dot_prod, marker = '.')
plt.xlabel("element")
plt.ylabel("Angle between fibre and sheet direction (deg)")
plt.show()