import numpy as np 
import math
import sys
import scipy.spatial as sp
import copy
import matplotlib.pyplot as plt

def rotation_matrix_marina(axis,angle):
    R = np.zeros((3,3), dtype=float)

    R[0][0] = axis[0]**2 + np.cos(theta)*(1-axis[0]**2)
    R[0][1] = (1 - np.cos(theta)) * axis[0] * axis[1] - axis[2] * np.sin(theta)
    R[0][2] = (1 - np.cos(theta)) * axis[0] * axis[2] + axis[1] * np.sin(theta)
    R[1][0] = (1 - np.cos(theta)) * axis[0] * axis[1] + axis[2] * np.sin(theta)
    R[1][1] = axis[1]**2 + np.cos(theta)*(1-axis[1]**2)
    R[1][2] = (1 - np.cos(theta)) * axis[1] * axis[2] - axis[0] * np.sin(theta)
    R[2][0] = (1 - np.cos(theta)) * axis[0] * axis[2] - axis[1] * np.sin(theta)
    R[2][1] = (1 - np.cos(theta)) * axis[1] * axis[2] + axis[0] * np.sin(theta)
    R[2][2] = axis[2]**2 + np.cos(theta)*(1-axis[2]**2)

    return R

# def rotation_matrix(axis, angle):
#     """
#     Return the rotation matrix associated with counterclockwise rotation about
#     the given axis by theta radians.
#     """
#     axis = np.asarray(axis)
#     axis = axis / math.sqrt(np.dot(axis, axis))
#     a = math.cos(angle / 2.0)
#     b, c, d = -axis * math.sin(angle / 2.0)
#     aa, bb, cc, dd = a * a, b * b, c * c, d * d
#     bc, ad, ac, ab, bd, cd = b * c, a * d, a * c, a * b, b * d, c * d
#     return np.array([[aa + bb - cc - dd, 2 * (bc + ad), 2 * (bd - ac)],
#                      [2 * (bc - ad), aa + cc - bb - dd, 2 * (cd + ab)],
#                      [2 * (bd + ac), 2 * (cd - ab), aa + dd - bb - cc]])


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

sheet_corrected = np.zeros((norms_grad.shape[0],3), dtype=float)
sheet_corrected_normalised = np.zeros((norms_grad.shape[0],3), dtype=float)
#print(np.shape(sheet_corrected))

for i,n in enumerate(norms_grad):
    #print(i)
    #print(np.dot(fibres_lon[i],norms_grad[i]))

    alpha = np.arccos(np.dot(fibres_lon[i],norms_grad[i]/np.linalg.norm(norms_grad[i])))
    theta = np.pi/2 - alpha
    sheet_corrected[i,:] = np.matmul(rotation_matrix_marina(axes_lon[i], theta), norms_grad[i])

    mag=np.linalg.norm(sheet_corrected[i,:])
    normalised = sheet_corrected[i,:]/mag
    normalised_norm = np.linalg.norm(normalised)
    sheet_corrected_normalised[i,:] = normalised



# print(sheet_corrected[30,:])
# print(sheet_corrected_normalised[30,:])
# a1 = sheet_corrected[30,:][0]
# b1 = sheet_corrected_normalised[30,:][0]
# a2 = sheet_corrected[30,:][1]
# b2 = sheet_corrected_normalised[30,:][1]
# a3 = sheet_corrected[30,:][2]
# b3 = sheet_corrected_normalised[30,:][2]

# print(a1)
# print(b1)
# print(a2)
# print(b2)
# print(a3)
# print(b3)

# print(b1/a1)
# print(b2/a2)
# print(b3/a3)

np.savetxt(fibres+'_sheet.lon',sheet_corrected_normalised,fmt="%g",header='1',comments='')
