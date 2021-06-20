import numpy as np
from scipy import integrate, interpolate
from scipy.special import sph_harm,lpmv
#check orthogonality of Spherical harmonics
#th in [0, 2 pi] and ph in [0, pi]

def f(th, ph):
	fx=1.0*sph_harm(-1,5,th,ph)+2.0*sph_harm(0,5,th,ph)+ 3.0*sph_harm(-2,3,th,ph)+ 4.0*sph_harm(-1,3,th,ph)
	return fx

x=integrate.nquad(lambda th, ph: f(th, ph)*sph_harm(2,3,th,ph)*np.sin(ph), [[0, 2*np.pi],[0, np.pi]])
print x

theta = np.linspace(0, 2*np.pi,50)
phi = np.linspace(0, np.pi,25)

thetaa, phii = np.meshgrid(theta, phi)
zr = f(thetaa, phii).real
zi = f(thetaa, phii).imag


#print z[[1],[1]].real
#print z[[1],[1]].imag


fr = interpolate.interp2d(thetaa, phii, zr, kind='cubic')
fi = interpolate.interp2d(thetaa, phii, zi, kind='cubic')

def F(th, ph):
	f=fr(th, ph)[0]+1j*fi(th, ph)[0]
	return f
	

y=integrate.nquad(lambda th, ph: F(th,ph)*sph_harm(1,3,th,ph)*np.sin(ph)*pow(-1,1), [[0, 2*np.pi],[0, np.pi]])
print y



