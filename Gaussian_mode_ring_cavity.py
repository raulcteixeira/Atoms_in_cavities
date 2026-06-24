import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

RedsTransp = np.zeros([256, 4])
RedsTransp[:, 0] = np.ones([256])
RedsTransp[:, 3] = np.linspace(0, 1, 256)
RedsTransp = ListedColormap(RedsTransp)

def prop_m(d):
    return np.array([[1, d], [0, 1]])

def mirror_m(R):
    return np.array([[1, 0], [-2./R, 1]])

def waist_from_matrix(M,lmbda):
    # return waist of beam from total matrix of round trip
    return np.sqrt(2*lmbda*M[0,1]/np.pi)/np.sqrt(4-(M[0,0] + M[1,1])**2)

def inverse_radius_from_matrix(M):
    # return 1/radius of curvature of wavefront of beam from total matrix of round trip
    return (M[1,1] - M[0,0])/(2*M[0,1])

def Gaussian_beam_intensity(x,z, w0, lmbda):
    zR = np.pi * w0**2 / lmbda  # Rayleigh range for a given wavelength
    w = w0 * np.sqrt(1 + (z / zR)**2)
    return np.exp(-2 * (x / w)**2)

# ring cavity geometry as an isosceles triangle
# plane mirror at symmetry vertice
# curved mirrors of radius R at others
# Side D between curved mirrors

# reflection angle at plane mirror
angle_deg = 45
angle = np.pi*angle_deg/180

wavelength = 689e-9

D = 0.001
d1 = D/2/np.sin(angle)
L = D + 2*d1

R = 0.002

print(L)
round_matrix = prop_m(D/2) @ mirror_m(R) @ prop_m(2*d1) @ mirror_m(R) @ prop_m(D/2)

w0 = waist_from_matrix(round_matrix,wavelength)
iR = inverse_radius_from_matrix(round_matrix)
print(w0, iR)

round_matrix_2 = prop_m(d1) @ mirror_m(R) @ prop_m(D) @ mirror_m(R) @ prop_m(d1)
w02 = waist_from_matrix(round_matrix_2,wavelength)
iR2 = inverse_radius_from_matrix(round_matrix_2)
print(w02, iR2)

x_lim = 5*w0
xx = np.linspace(-x_lim, x_lim, 1000)  # Transverse position

Z = np.linspace(-D/2, D/2, 1000)  # Propagation distance
X, Z = np.meshgrid(xx, Z, indexing='ij')  # Create a meshgrid for X and Z
beam = Gaussian_beam_intensity(X-3*w0, Z, w0, wavelength)
beam1 = Gaussian_beam_intensity(X+6*w0*Z/D, Z, w02, wavelength)
beam2 = Gaussian_beam_intensity(X-6*w0*Z/D, Z, w02, wavelength)

transp = 0.8

fig, ax = plt.subplots(figsize=(10, 6))
ax.imshow(beam, extent=[-D/2, D/2, -x_lim, x_lim], aspect='auto', cmap=RedsTransp, alpha = transp)
ax.imshow(beam1, extent=[-D/2, D/2, -x_lim, x_lim], aspect='auto', cmap=RedsTransp,  alpha = transp)
ax.imshow(beam2, extent=[-D/2, D/2, -x_lim, x_lim], aspect='auto', cmap=RedsTransp,  alpha = transp)
ax.set_ylim(-x_lim, 0)
ax.set_xlim(-D/2, D/2)
ax.axis('off')
plt.tight_layout()
plt.show()
