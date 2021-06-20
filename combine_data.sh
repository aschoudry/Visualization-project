#!/bin/bash
file_locations=/datarepo/forashok/zero_Degrees_Rotation
Bx_0=$file_locations/Bx.file_0.h5
Bx_1=$file_locations/Bx.file_1.h5
Bx_2=$file_locations/Bx.file_2.h5
Bx_3=$file_locations/Bx.file_3.h5
Bx_4=$file_locations/Bx.file_4.h5
Bx_5=$file_locations/Bx.file_5.h5
Bx_6=$file_locations/Bx.file_6.h5
Bx_7=$file_locations/Bx.file_7.h5

By_0=$file_locations/By.file_0.h5
By_1=$file_locations/By.file_1.h5
By_2=$file_locations/By.file_2.h5
By_3=$file_locations/By.file_3.h5
By_4=$file_locations/By.file_4.h5
By_5=$file_locations/By.file_5.h5
By_6=$file_locations/By.file_6.h5
By_7=$file_locations/By.file_7.h5


Bz_0=$file_locations/Bz.file_0.h5
Bz_1=$file_locations/Bz.file_1.h5
Bz_2=$file_locations/Bz.file_2.h5
Bz_3=$file_locations/Bz.file_3.h5
Bz_4=$file_locations/Bz.file_4.h5
Bz_5=$file_locations/Bz.file_5.h5
Bz_6=$file_locations/Bz.file_6.h5
Bz_7=$file_locations/Bz.file_7.h5


./hdf5_merge $Bx_0 $By_0 $Bz_0  $file_locations/Bxyz.file_0.h5
./hdf5_merge $Bx_1 $By_1 $Bz_1  $file_locations/Bxyz.file_1.h5
./hdf5_merge $Bx_2 $By_2 $Bz_2  $file_locations/Bxyz.file_2.h5
./hdf5_merge $Bx_3 $By_3 $Bz_3  $file_locations/Bxyz.file_3.h5
./hdf5_merge $Bx_4 $By_4 $Bz_4  $file_locations/Bxyz.file_4.h5
./hdf5_merge $Bx_5 $By_5 $Bz_5  $file_locations/Bxyz.file_5.h5
./hdf5_merge $Bx_6 $By_6 $Bz_6  $file_locations/Bxyz.file_6.h5
./hdf5_merge $Bx_7 $By_7 $Bz_7  $file_locations/Bxyz.file_7.h5




