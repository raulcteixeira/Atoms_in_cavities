import numpy as np
import matplotlib.pyplot as plt


"""
Gaussian beam expression
"""

def Gaussian_beam_intensity(x,z, w0, lmbda):
    zR = np.pi * w0**2 / lmbda  # Rayleigh range for a given wavelength
    w = w0 * np.sqrt(1 + (z / zR)**2)
    return np.exp(-2 * (x / w)**2)


# w0 = 1e-3  # Beam waist (m)
# wavelength = 689e-9  # Wavelength (m)
# zR = np.pi * w0**2 / wavelength  # Rayleigh range  

# Z = np.linspace(-zR, zR, 1000)  # Propagation distance
# X = np.linspace(-5 * w0, 5 * w0, 1000)  # Transverse position
# X, Z = np.meshgrid(X, Z, indexing='ij')  # Create a meshgrid for X and Z

# plt.figure(figsize=(10, 6))
# plt.imshow(Gaussian_beam_intensity(X, Z, w0, wavelength),  extent=[-zR, zR, -5 * w0, 5 * w0], aspect='auto', cmap='Reds')
# # plt.colorbar(label='Intensity')
# # plt.xlabel('Transverse Position (m)')
# # plt.ylabel('Propagation Distance (m)')
# # plt.title('Gaussian Beam Intensity')
# plt.axis('off')
# plt.tight_layout()
# plt.show()

# w0 = 0.5e-3  # New beam waist (m)
# plt.figure(figsize=(10, 6))
# plt.imshow(Gaussian_beam_intensity(X, Z, w0, wavelength), extent=[-zR, zR, -5 * w0, 5 * w0], aspect='auto', cmap='Reds')
# plt.axis('off')
# plt.tight_layout()
# plt.show()

# w0 = 0.25e-3  # New beam waist (m)
# plt.figure(figsize=(10, 6))
# plt.imshow(Gaussian_beam_intensity(X, Z, w0, wavelength), extent=[-zR, zR, -5 * w0, 5 * w0], aspect='auto', cmap='Reds')
# plt.axis('off')
# plt.tight_layout()
# plt.show()

# Xt = np.linspace(-3 * w0, 3 * w0, 1000)  # Transverse position for intensity profile
# Yt = np.linspace(-3 * w0, 3 * w0, 1000)  # Transverse position for intensity profile
# Xt, Yt = np.meshgrid(Xt, Yt, indexing='ij')  # Create a meshgrid for Xt and Yt

# Rt = np.sqrt(Xt**2 + Yt**2)  # Radial distance from the center


# plt.figure(figsize=(6, 6))
# plt.imshow(Gaussian_beam_intensity(Rt, 0, w0, wavelength), extent=[-3 * w0, 3 * w0, -3 * w0, 3 * w0], aspect='auto', cmap='Reds')
# plt.axis('off')
# plt.tight_layout()
# plt.show()


"""
Gaussian modes of different cavities
"""

def beam_curved_mirrors(R1,R2,d,lmbda):
    b2 = np.sqrt((d * (R1 - d) * (R2 - d) * (R1 + R2 - d)) / (R1 + R2 - 2 * d))
    w0 = np.sqrt(lmbda * b2 / np.pi)
    t = d*(R2 - d) / (R1 + R2 - 2 * d)
    return w0,t

def beam_flat_curved_mirror(R,d,lmbda):
    b2 = np.sqrt(d * (R - d))
    w0 = np.sqrt(lmbda * b2 / np.pi)
    t = 0
    return w0,t

# R = 0.1
# d = 0.09
# wavelength = 689e-9

# w0, t = beam_curved_mirrors(R,R,d,wavelength)

# print(w0)

# x_lim = 7*w0
# Z = np.linspace(0, d, 1000)  # Propagation distance
# X = np.linspace(-x_lim, x_lim, 1000)  # Transverse position
# X, Z = np.meshgrid(X, Z, indexing='ij')  # Create a meshgrid for X and Z

# beam = Gaussian_beam_intensity(X, Z-t, w0, wavelength)


# fig, ax = plt.subplots(figsize=(10, 6))
# ax.imshow(Gaussian_beam_intensity(X, Z-t, w0, wavelength), extent=[0, d, -x_lim, x_lim], aspect='auto', cmap='Reds')
# ax.axis('off')
# plt.tight_layout()
# plt.show()

# # different radius of curvature
# R1 = 0.15
# R2 = 0.1
# d = 0.07
# wavelength = 689e-9

# w0, t = beam_curved_mirrors(R1, R2, d, wavelength)

# print(w0)

# x_lim = 5*w0
# Z = np.linspace(0, d, 1000)  # Propagation distance
# X = np.linspace(-x_lim, x_lim, 1000)  # Transverse position
# X, Z = np.meshgrid(X, Z, indexing='ij')  # Create a meshgrid for X and Z

# beam = Gaussian_beam_intensity(X, Z-t, w0, wavelength)


# fig, ax = plt.subplots(figsize=(10, 6))
# ax.imshow(Gaussian_beam_intensity(X, Z-t, w0, wavelength), extent=[0, d, -x_lim, x_lim], aspect='auto', cmap='Reds')
# ax.axis('off')
# plt.tight_layout()
# plt.show()


# # flat with curved mirror
# R = 0.1
# d = 0.09
# wavelength = 689e-9

# w0, t = beam_flat_curved_mirror(R, d, wavelength)

# print(w0)

# x_lim = 5*w0
# Z = np.linspace(0, d, 1000)  # Propagation distance
# X = np.linspace(-x_lim, x_lim, 1000)  # Transverse position
# X, Z = np.meshgrid(X, Z, indexing='ij')  # Create a meshgrid for X and Z

# beam = Gaussian_beam_intensity(X, Z-t, w0, wavelength)


# fig, ax = plt.subplots(figsize=(10, 6))
# ax.imshow(Gaussian_beam_intensity(X, Z-t, w0, wavelength), extent=[0, d, -x_lim, x_lim], aspect='auto', cmap='Reds')
# ax.axis('off')
# plt.tight_layout()
# plt.show()


"""
Intensity profile considering the formed standing wave
"""

R = 0.1
d = 0.05
wavelength = 689e-9
k0 = 2*np.pi/wavelength

w0, t = beam_curved_mirrors(R,R,d,wavelength)

x_lim = 2*w0
z_lim = 3*wavelength
Z = np.linspace(d/2-z_lim, d/2+z_lim, 1000)  # Propagation distance
X = np.linspace(-x_lim, x_lim, 1000)  # Transverse position
X, Z = np.meshgrid(X, Z, indexing='ij')  # Create a meshgrid for X and Z

fig, ax = plt.subplots(figsize=(10, 6))
ax.imshow(Gaussian_beam_intensity(X, Z-t, w0, wavelength)*np.cos(k0*Z)**2, extent=[d/2-z_lim, d/2+z_lim, -x_lim, x_lim], aspect='auto', cmap='Reds')
ax.axis('off')
plt.tight_layout()
plt.show()