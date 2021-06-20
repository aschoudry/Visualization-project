import numpy as np

##Open file to write the data

f = open("/home/ashok/Programming_stuff/python/lumisity_data", "w")

for i in range(100):
	itr = ('%0*d' % (4, i))
	data_file_name = '/home/ashok/XYZdata/XYZformatdata/Poynting_flux_data_at_100/visit_ex_db'+itr+'.xyz'

	x, y, z, Px, Py, Pz = np.loadtxt(data_file_name, skiprows=2, usecols=(3,4,5,6,7,8),unpack=True)

	time = 1.0
	PdotRcap = (Px*x + Py*y + Pz*z)/np.sqrt(x*x + y*y +z*z) 
	flux = sum(PdotRcap)

	str = "%25.15e %25.15e\n" % (int(itr), flux)
	f.write(str)
f.close()
