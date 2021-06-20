import numpy as np
import spinweighted_sphericalharmonics as gp

# parameter values
s = -2
l = 4
m = 2

#domain
x = np.linspace(-100, 100, 100)
y = np.linspace(-100, 100, 100)
z = np.linspace(0, 100, 100)

R = np.sqrt(x**2 + y**2 + z**2)



gp.Y_slm(s, l, m, theta, phi)
