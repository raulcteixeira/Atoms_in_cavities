import numpy as np
import matplotlib.pyplot as plt

def transmission(frequency, f0, FSR, R1, A1, R2, A2):
    delta_f = frequency - f0
    phi = 2 * np.pi * delta_f / FSR
    T = (1 - A1 - R1) * (1 - A2 - R2) / ((1 - np.sqrt(R1 * R2))**2 + 4 * np.sqrt(R1 * R2) * np.sin(phi / 2)**2)
    return T

def maximum_transmission(R1, A1, R2, A2):
    f0 = 1
    FSR = 1
    return transmission(1, 1, 1, R1, A1, R2, A2)

def finesse(R1, R2):
    return np.pi * np.sqrt(np.sqrt(R1 * R2)) / (1 - np.sqrt(R1 * R2))

def resonant_intensity_enhancement( R1, A1, R2, A2):
    return maximum_transmission(R1, A1, R2, A2) / (1 - R2 - A2)

# Cavity transmission

R1 = 0.989
A1 = 0.0
R2 = 0.989
A2 = 0.0
f0 = 400e12  # Center frequency (Hz)
FSR = 1e12   # Free spectral range (Hz)
frequency = np.linspace(f0 - FSR/80, f0 + FSR/80, 1000)

# plt.plot(frequency, transmission(frequency, f0, FSR, R1, A1, R2, A2))
# plt.xlabel('Frequency (Hz)')
# plt.ylabel('Transmission')
# plt.title('FP Cavity Transmission')
# plt.show()

# plt.plot((frequency-f0)/FSR*(2*finesse(R1,R2)), transmission(frequency, f0, FSR, R1, A1, R2, A2), linewidth = 3)
# plt.xlabel('$\Delta_C (\kappa)$',fontsize = 16)
# plt.ylabel('Transmission', fontsize = 16)
# plt.title('FP Cavity Transmission', fontsize = 16)
# plt.tick_params(axis='both', which='major', labelsize=16)
# plt.tight_layout()
# plt.show()

plt.plot((frequency-f0)/FSR*(2*finesse(R1,R2)), transmission(frequency, f0, FSR, R1, A1, R2, A2), linewidth = 3)
plt.xlabel(r'$\frac{\nu - \nu_0}{\delta \nu}$',fontsize = 24)
plt.ylabel('Transmission', fontsize = 16)
plt.title('FP Cavity Transmission', fontsize = 16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.tight_layout()
plt.show()

R1 = 0.99
T2_exp = np.linspace(-1.7, -5, 100)
T2 = 10**T2_exp    
R2 = 1 - T2

# plt.semilogy(R2, finesse(R1, R2), label='Fixed R1 = 0.99')
# plt.semilogy(R2, finesse(R2, R2), 'r--', label='Identical mirrors')
# plt.xlabel('R2', fontsize=16)
# plt.tick_params(axis='both', which='major', labelsize=16)
# plt.ylabel('Finesse', fontsize=16)
# plt.title('Finesse vs R2', fontsize=16)
# plt.legend(fontsize=16)
# plt.tight_layout()
# plt.show()

# plt.semilogy(R2, resonant_intensity_enhancement(R1, 0, R2, 0), label='Fixed R1 = 0.99')
# plt.semilogy(R2, resonant_intensity_enhancement(R2, 0, R2, 0), 'r--', label='Identical mirrors')
# plt.xlabel('R2', fontsize=16)
# plt.tick_params(axis='both', which='major', labelsize=16)
# plt.ylabel('Intensity inside cavity', fontsize=16)
# plt.title('Intensity enhancement vs R2', fontsize=16)
# plt.legend(fontsize=16)
# plt.tight_layout()
# plt.show()

# plt.semilogy(R2, maximum_transmission(R1, 0, R2, 0), label='Fixed R1 = 0.99')
# plt.semilogy(R2, maximum_transmission(R2, 0, R2, 0), 'r--', label='Identical mirrors')
# plt.xlabel('R2', fontsize=16)
# plt.tick_params(axis='both', which='major', labelsize=16)
# plt.ylabel('Transmission', fontsize=16)
# plt.title('Maximum transmission vs R2', fontsize=16)
# plt.legend(fontsize=16)
# plt.tight_layout()
# plt.show()


A = 1e-3
T_exp = np.linspace(-1.7, -5, 100)
Tr = 10**T_exp    
R = 1 - A  - Tr
plt.semilogy(R, maximum_transmission(R, A, R, A), label='A = 1e-3')
A = 0
T_exp = np.linspace(-1.7, -5, 100)
Tr = 10**T_exp    
R = 1 - A  - Tr
plt.semilogy(R, maximum_transmission(R, A, R, A), 'r--',label='No absorption')
plt.xlabel('R', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.ylabel('Cavity transmission', fontsize=16)
plt.title('Maximum transmission vs R', fontsize=16)
plt.legend(fontsize=16)
plt.tight_layout()
plt.show()

A = 1e-3
T_exp = np.linspace(-1, -5, 100)
Tr = 10**T_exp    
R = 1 - A  - Tr
plt.loglog(1-R-A, maximum_transmission(R, A, R, A), label='A = 1e-3')
A = 0
T_exp = np.linspace(-1, -5, 100)
Tr = 10**T_exp    
R = 1 - A  - Tr
plt.loglog(1-R-A, maximum_transmission(R, A, R, A), 'r--',label='No absorption')
plt.xlabel('T', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.ylabel('Cavity transmission', fontsize=16)
plt.title('Maximum transmission vs T', fontsize=16)
plt.legend(fontsize=16)
plt.tight_layout()
plt.show()

A = 1e-3
T_exp = np.linspace(-1.7, -5, 100)
Tr = 10**T_exp    
R = 1 - A  - Tr
plt.semilogy(R, resonant_intensity_enhancement(R, A, R, A), label='A = 1e-3')
A = 0
T_exp = np.linspace(-1.7, -5, 100)
Tr = 10**T_exp    
R = 1 - A  - Tr
plt.semilogy(R, resonant_intensity_enhancement(R, A, R, A), 'r--',label='No absorption')
plt.xlabel('R', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.ylabel('Internal intensity', fontsize=16)
plt.title('Resonant intensity enhancement vs R', fontsize=16)
plt.legend(fontsize=16)
plt.tight_layout()
plt.show()