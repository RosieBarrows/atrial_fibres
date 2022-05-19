import numpy as np 
import math
import sys
import scipy.spatial as sp
import copy

def rotation_matrix(axis, angle):
    """
    Return the rotation matrix associated with counterclockwise rotation about
    the given axis by theta radians.
    """
    axis = np.asarray(axis)
    axis = axis / math.sqrt(np.dot(axis, axis))
    a = math.cos(angle / 2.0)
    b, c, d = -axis * math.sin(angle / 2.0)
    aa, bb, cc, dd = a * a, b * b, c * c, d * d
    bc, ad, ac, ab, bd, cd = b * c, a * d, a * c, a * b, b * d, c * d
    return np.array([[aa + bb - cc - dd, 2 * (bc + ad), 2 * (bd - ac)],
                     [2 * (bc - ad), aa + cc - bb - dd, 2 * (cd + ab)],
                     [2 * (bd + ac), 2 * (cd - ab), aa + dd - bb - cc]])


fibres=sys.argv[1]
norms=sys.argv[2]
axes=sys.argv[3]

print('Reading mesh...')
fibres_lon = np.loadtxt(fibres+'.lon',dtype=float,skiprows=1)
fibres_pts = np.loadtxt(fibres+'.pts',dtype=float,skiprows=1)
fibres_elem = np.loadtxt(fibres+'.elem',dtype=int,skiprows=1,usecols=[1,2,3])
print('Done')

print('Reading mesh...')
norms_grad = np.loadtxt(norms,dtype=float)
print('Done')

print('Reading mesh...')
axes_lon = np.loadtxt(axes+'.lon',dtype=float,skiprows=1)
axes_pts = np.loadtxt(axes+'.pts',dtype=float,skiprows=1)
axes_elem = np.loadtxt(axes+'.elem',dtype=int,skiprows=1,usecols=[1,2,3])
print('Done')

sheet_normalised = np.zeros((norms_grad.shape[0],3), dtype=float)
sheet_normalised_corrected = np.zeros((norms_grad.shape[0],3), dtype=float)

for i,n in enumerate(norms_grad):
    mag=np.linalg.norm(norms_grad[i,:])
    sheet_normalised[i,:]=norms_grad[i,:]/mag

for i,n in enumerate(sheet_normalised):
    alpha = np.arccos(np.dot(fibres_lon[i,:],sheet_normalised[i,:]))
    theta = alpha - np.pi/2
    sheet_normalised_corrected[i,:] = np.dot(rotation_matrix(axes_lon[i,:], theta), sheet_normalised[i,:])

np.savetxt(fibres+'_sheet.lon',sheet_normalised_corrected,fmt="%g",header='1',comments='')
