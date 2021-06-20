import numpy as np
import sys
#Specify where visit is installed in your system
sys.path.append("/home/aschoudhary/local/2.12.2/linux-x86_64/lib/site-packages/")

import visit
from visit import*
LaunchNowin()

#Open data files
OpenDatabase("localhost:/datarepo/dataforashok/Aug18_2017_GiRaffedata/blandford_znajeck_studies-giraffe-hr-rot45-redo-Poyn/separation_10p4__nonspinning__vertBfield/Poynxyz.file_* database", 0)

#Define Expressions
DefineScalarExpression("PoynX", "<SMALLBPOYNET--Poynx>")
DefineScalarExpression("PoynY", "<SMALLBPOYNET--Poyny>")
DefineScalarExpression("PoynZ", "<SMALLBPOYNET--Poynz>")
DefineScalarExpression("X", "coord(<Carpet AMR-grid>)[0]")
DefineScalarExpression("Y", "coord(<Carpet AMR-grid>)[1]")
DefineScalarExpression("Z", "coord(<Carpet AMR-grid>)[2]")
DefineScalarExpression("Poynting_flux_through_sphere", "(PoynX*X + PoynY*Y + PoynZ*Z)")

#Add plots to get the data
AddPlot("Pseudocolor", "Poynting_flux_through_sphere", 1, 0)
AddOperator("SphereSlice", 0)
SphereSliceAtts = SphereSliceAttributes()
SphereSliceAtts.origin = (0, 0, 0)
SphereSliceAtts.radius = 50
SetOperatorOptions(SphereSliceAtts, 0)
DrawPlots()

def DoublePrecisionQueryOverTime():	
	for i in range(10,TimeSliderGetNStates()):
		SetTimeSliderState(i)
		Query("Time")
		t = GetQueryOutputValue()
		Query("Weighted Variable Sum")
		t2 = GetQueryOutputValue()
		str = "%25.15e %25.15e\n" %(t, t2)
		f.write(str)
	f.close()
 

extraction_radius = [100, 150 ,200]

for i in extraction_radius:
	SphereSliceAtts = SphereSliceAttributes()
	SphereSliceAtts.origin = (0, 0, 0)
	SphereSliceAtts.radius = i
	SetOperatorOptions(SphereSliceAtts, 0)
	f = open("/home/aschoudhary/Streamline_project/data/Luminosity_query_over_time_radius"+str(i)+".ultra", "w")
	DoublePrecisionQueryOverTime()
