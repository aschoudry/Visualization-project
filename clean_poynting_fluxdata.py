import numpy as np

##Open file to write the data


for i in range(100):
	itr = ('%0*d' % (4, i))
	data_file_name = '/home/ashok/XYZdata/XYZformatdata/Poynting_flux_data_at_100/visit_ex_db'+itr+'.xyz'
	x, y, z, Px, Py, Pz = np.loadtxt(data_file_name, skiprows=4, usecols=(4,5,6,7,8,9),unpack=True)
	f = open("/home/ashok/Cleaned_poynting_flux_data/poynting_data_"+itr+"r100", "w")
	for i in range(len(x)):
		str = "%f %f %f %25.15e %25.15e %25.15e\n" % (x[i], y[i], z[i], Px[i], Py[i], Pz[i])
		f.write(str)

	f.close()
