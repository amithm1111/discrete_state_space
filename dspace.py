import numpy as np
from scipy.signal import cont2discrete

dt = 0.01
A = np.zeros((6,6))
B = np.zeros((6,3))
C = np.zeros((6,6)) 
D = np.zeros((6,3))

A[0,4] = 1
A[1,5] = 1
A[2,6] = 1
B[3,1] = 1
B[4,2] = 1
B[5,3] = 1

d_system = cont2discrete((A, B, C, D), dt, 'euler')
print('Euler\n')
print('dA =', d_system[0])
print('dB =', d_system[1])

d_system = cont2discrete((A, B, C, D), dt, 'zoh')
print('zoh\n')
print('dA =', d_system[0])
print('dB =', d_system[1])

d_system = cont2discrete((A, B, C, D), dt, 'backward_diff')
print('backward_diff\n')
print('dA =', d_system[0])
print('dB =', d_system[1])

d_system = cont2discrete((A, B, C, D), dt, 'bilinear')
print('bilinear\n')
print('dA =', d_system[0])
print('dB =', d_system[1])
