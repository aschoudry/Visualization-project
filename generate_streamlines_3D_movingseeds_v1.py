import numpy as np
import sys
#Specify where visit is installed in your system
sys.path.append("/home/aschoudhary/local/2.12.2/linux-x86_64/lib/site-packages/")

import visit
from visit import*
LaunchNowin()

#Open data files
OpenDatabase("localhost:/datarepo/forashok/Bx.file_* database", 0)
OpenDatabase("localhost:/datarepo/forashok/BBH.visit", 0)

#################################################################################################################################################
########################################## Finding particle inside the box of length 20 #########################################################
#################################################################################################################################################
ActivateDatabase("localhost:/datarepo/forashok/Bx.file_* database")
print 'pseudocolour'
AddPlot("Pseudocolor", "GIRAFFE--Bx", 1, 0)
DrawPlots()

time_for_particle_data_output = []
#cycle_index = []


for state in range(1,TimeSliderGetNStates(),1):
	SetActivePlots(0)
	SetTimeSliderState(state)
	Query("Time") 
	time=GetQueryOutputValue()
	Query("Cycle") 
	cycle=GetQueryOutputValue()
	time_for_particle_data_output.extend([time])
#	cycle_index.extend([cycle])
#	print time
DeleteActivePlots()

Seed = np.loadtxt('/datarepo/forashok/particles.txt', skiprows = 2, unpack = True)
#Seed_list = Seed[:, time_index]

particle_location_index = []

for i in range(len(time_for_particle_data_output)):
	for j in range(len(Seed[0,:])):
		if abs(time_for_particle_data_output[i] - Seed[0,j]) < 0.1:
			particle_location_index.extend([j])




#################################################################################################################################################
#################################################################################################################################################


# Generate integral curves 
ActivateDatabase("localhost:/datarepo/forashok/Bx.file_* database")
SetTimeSliderState(22)

############################################################################################################################################
seeds = (-10, -10, 0, -10, -8, 0, -10, -6, 0, -10, -4, 0, -10, -2, 0, -10, 0, 0, -10, 2, 0, -10, 4, 0, -10, 6, 0, -10, 8, 0, -10, 10, 0, -8, -10, 0, -8, -8, 0, -8, -6, 0, -8, -4, 0, -8, -2, 0, -8, 0, 0, -8, 2, 0, -8, 4, 0, -8, 6, 0, -8, 8, 0, -8, 10, 0, -6, -10, 0, -6, -8, 0, -6, -6, 0, -6, -4, 0, -6, -2, 0, -6, 0, 0, -6, 2, 0, -6, 4, 0, -6, 6, 0, -6, 8, 0, -6, 10, 0, -4, -10, 0, -4, -8, 0, -4, -6, 0, -4, -4, 0, -4, -2, 0, -4, 0, 0, -4, 2, 0, -4, 4, 0, -4, 6, 0, -4, 8, 0, -4, 10, 0, -2, -10, 0, -2, -8, 0, -2, -6, 0, -2, -4, 0, -2, -2, 0, -2, 0, 0, -2, 2, 0, -2, 4, 0, -2, 6, 0, -2, 8, 0, -2, 10, 0, 0, -10, 0, 0, -8, 0, 0, -6, 0, 0, -4, 0, 0, -2, 0, 0, 0, 0, 0, 2, 0, 0, 4, 0, 0, 6, 0, 0, 8, 0, 0, 10, 0, 2, -10, 0, 2, -8, 0, 2, -6, 0, 2, -4, 0, 2, -2, 0, 2, 0, 0, 2, 2, 0, 2, 4, 0, 2, 6, 0, 2, 8, 0, 2, 10, 0, 4, -10, 0, 4, -8, 0, 4, -6, 0, 4, -4, 0, 4, -2, 0, 4, 0, 0, 4, 2, 0, 4, 4, 0, 4, 6, 0, 4, 8, 0, 4, 10, 0, 6, -10, 0, 6, -8, 0, 6, -6, 0, 6, -4, 0, 6, -2, 0, 6, 0, 0, 6, 2, 0, 6, 4, 0, 6, 6, 0, 6, 8, 0, 6, 10, 0, 8, -10, 0, 8, -8, 0, 8, -6, 0, 8, -4, 0, 8, -2, 0, 8, 0, 0, 8, 2, 0, 8, 4, 0, 8, 6, 0, 8, 8, 0, 8, 10, 0, 10, -10, 0, 10, -8, 0, 10, -6, 0, 10, -4, 0, 10, -2, 0, 10, 0, 0, 10, 2, 0, 10, 4, 0, 10, 6, 0, 10, 8, 0, 10, 10, 0)

############################################################################################################################################

def generate_streamlines(seeds):
	AddPlot("Pseudocolor", "operators/IntegralCurve/Bvec", 1, 0)
	IntegralCurveAtts = IntegralCurveAttributes()
	IntegralCurveAtts.sourceType = IntegralCurveAtts.PointList  # SpecifiedPoint, PointList, SpecifiedLine, Circle, SpecifiedPlane, SpecifiedSphere, SpecifiedBox, Selection, FieldData
	IntegralCurveAtts.pointSource = (0, 0, 0)
	IntegralCurveAtts.lineStart = (0, 0, 0)
	IntegralCurveAtts.lineEnd = (1, 0, 0)
	IntegralCurveAtts.planeOrigin = (0, 0, 0)
	IntegralCurveAtts.planeNormal = (0, 0, 1)
	IntegralCurveAtts.planeUpAxis = (0, 1, 0)
	IntegralCurveAtts.radius = 1
	IntegralCurveAtts.sphereOrigin = (0, 0, 0)
	IntegralCurveAtts.boxExtents = (0, 1, 0, 1, 0, 1)
	IntegralCurveAtts.useWholeBox = 1
	IntegralCurveAtts.pointList = seeds 
	IntegralCurveAtts.fieldData = ()
	IntegralCurveAtts.sampleDensity0 = 2
	IntegralCurveAtts.sampleDensity1 = 2
	IntegralCurveAtts.sampleDensity2 = 2
	IntegralCurveAtts.dataValue = IntegralCurveAtts.TimeAbsolute  # Solid, SeedPointID, Speed, Vorticity, ArcLength, TimeAbsolute, TimeRelative, AverageDistanceFromSeed, CorrelationDistance, Difference, Variable
	IntegralCurveAtts.dataVariable = ""
	IntegralCurveAtts.integrationDirection = IntegralCurveAtts.Both  # Forward, Backward, Both, ForwardDirectionless, BackwardDirectionless, BothDirectionless
	IntegralCurveAtts.maxSteps = 1000
	IntegralCurveAtts.terminateByDistance = 1
	IntegralCurveAtts.termDistance = 20
	IntegralCurveAtts.terminateByTime = 0
	IntegralCurveAtts.termTime = 10
	IntegralCurveAtts.maxStepLength = 0.1
	IntegralCurveAtts.limitMaximumTimestep = 0
	IntegralCurveAtts.maxTimeStep = 0.1
	IntegralCurveAtts.relTol = 0.0001
	IntegralCurveAtts.absTolSizeType = IntegralCurveAtts.FractionOfBBox  # Absolute, FractionOfBBox
	IntegralCurveAtts.absTolAbsolute = 1e-06
	IntegralCurveAtts.absTolBBox = 1e-06
	IntegralCurveAtts.fieldType = IntegralCurveAtts.Default  # Default, FlashField, M3DC12DField, M3DC13DField, Nek5000Field, NektarPPField, NIMRODField
	IntegralCurveAtts.fieldConstant = 1
	IntegralCurveAtts.velocitySource = (0, 0, 0)
	IntegralCurveAtts.integrationType = IntegralCurveAtts.AdamsBashforth  # Euler, Leapfrog, DormandPrince, AdamsBashforth, RK4, M3DC12DIntegrator
	IntegralCurveAtts.parallelizationAlgorithmType = IntegralCurveAtts.VisItSelects  # LoadOnDemand, ParallelStaticDomains, MasterSlave, VisItSelects
	IntegralCurveAtts.maxProcessCount = 10
	IntegralCurveAtts.maxDomainCacheSize = 3
	IntegralCurveAtts.workGroupSize = 32
	IntegralCurveAtts.pathlines = 0
	IntegralCurveAtts.pathlinesOverrideStartingTimeFlag = 0
	IntegralCurveAtts.pathlinesOverrideStartingTime = 0
	IntegralCurveAtts.pathlinesPeriod = 0
	IntegralCurveAtts.pathlinesCMFE = IntegralCurveAtts.POS_CMFE  # CONN_CMFE, POS_CMFE
	IntegralCurveAtts.displayGeometry = IntegralCurveAtts.Lines  # Lines, Tubes, Ribbons
	IntegralCurveAtts.cleanupMethod = IntegralCurveAtts.NoCleanup  # NoCleanup, Merge, Before, After
	IntegralCurveAtts.cleanupThreshold = 1e-08
	IntegralCurveAtts.cropBeginFlag = 0
	IntegralCurveAtts.cropBegin = 0
	IntegralCurveAtts.cropEndFlag = 0
	IntegralCurveAtts.cropEnd = 0
	IntegralCurveAtts.cropValue = IntegralCurveAtts.Time  # Distance, Time, StepNumber
	IntegralCurveAtts.sampleDistance0 = 10
	IntegralCurveAtts.sampleDistance1 = 10
	IntegralCurveAtts.sampleDistance2 = 10
	IntegralCurveAtts.fillInterior = 1
	IntegralCurveAtts.randomSamples = 0
	IntegralCurveAtts.randomSeed = 0
	IntegralCurveAtts.numberOfRandomSamples = 1
	IntegralCurveAtts.issueAdvectionWarnings = 1
	IntegralCurveAtts.issueBoundaryWarnings = 1
	IntegralCurveAtts.issueTerminationWarnings = 1
	IntegralCurveAtts.issueStepsizeWarnings = 1
	IntegralCurveAtts.issueStiffnessWarnings = 1
	IntegralCurveAtts.issueCriticalPointsWarnings = 1
	IntegralCurveAtts.criticalPointThreshold = 0.001
	IntegralCurveAtts.correlationDistanceAngTol = 5
	IntegralCurveAtts.correlationDistanceMinDistAbsolute = 1
	IntegralCurveAtts.correlationDistanceMinDistBBox = 0.005
	IntegralCurveAtts.correlationDistanceMinDistType = IntegralCurveAtts.FractionOfBBox  # Absolute, FractionOfBBox
	IntegralCurveAtts.selection = ""
	SetOperatorOptions(IntegralCurveAtts, 0)
	AddOperator("Reflect", 0)
	ReflectAtts = ReflectAttributes()
	ReflectAtts.octant = ReflectAtts.PXPYPZ  # PXPYPZ, NXPYPZ, PXNYPZ, NXNYPZ, PXPYNZ, NXPYNZ, PXNYNZ, NXNYNZ
	ReflectAtts.useXBoundary = 0
	ReflectAtts.specifiedX = 0
	ReflectAtts.useYBoundary = 0
	ReflectAtts.specifiedY = 0
	ReflectAtts.useZBoundary = 0
	ReflectAtts.specifiedZ = 0
	ReflectAtts.reflections = (1, 0, 1, 0, 0, 0, 1, 0)
	SetOperatorOptions(ReflectAtts, 0)
	DrawPlots()



# End spontaneous state
def View_parameters():
	ViewCurveAtts = ViewCurveAttributes()
	ViewCurveAtts.domainCoords = (0, 1)
	ViewCurveAtts.rangeCoords = (0, 1)
	ViewCurveAtts.viewportCoords = (0.2, 0.95, 0.15, 0.95)
	ViewCurveAtts.domainScale = ViewCurveAtts.LINEAR  # LINEAR, LOG
	ViewCurveAtts.rangeScale = ViewCurveAtts.LINEAR  # LINEAR, LOG
	SetViewCurve(ViewCurveAtts)
	View2DAtts = View2DAttributes()
	View2DAtts.windowCoords = (0, 1, 0, 1)
	View2DAtts.viewportCoords = (0.2, 0.95, 0.15, 0.95)
	View2DAtts.fullFrameActivationMode = View2DAtts.Auto  # On, Off, Auto
	View2DAtts.fullFrameAutoThreshold = 100
	View2DAtts.xScale = View2DAtts.LINEAR  # LINEAR, LOG
	View2DAtts.yScale = View2DAtts.LINEAR  # LINEAR, LOG
	View2DAtts.windowValid = 0
	SetView2D(View2DAtts)
	View3DAtts = View3DAttributes()
	View3DAtts.viewNormal = (0, 0, 1)
	View3DAtts.focus = (0, 0, 0)
	View3DAtts.viewUp = (0, 1, 0)
	View3DAtts.viewAngle = 30
	View3DAtts.parallelScale = 24.4949
	View3DAtts.nearPlane = -48.9898
	View3DAtts.farPlane = 48.9898
	View3DAtts.imagePan = (0, 0)
	View3DAtts.imageZoom = 1
	View3DAtts.perspective = 1
	View3DAtts.eyeAngle = 2
	View3DAtts.centerOfRotationSet = 0
	View3DAtts.centerOfRotation = (0, 0, 0)
	View3DAtts.axis3DScaleFlag = 0
	View3DAtts.axis3DScales = (1, 1, 1)
	View3DAtts.shear = (0, 0, 1)
	View3DAtts.windowValid = 1
	SetView3D(View3DAtts)
	ViewAxisArrayAtts = ViewAxisArrayAttributes()
	ViewAxisArrayAtts.domainCoords = (0, 1)
	ViewAxisArrayAtts.rangeCoords = (0, 1)
	ViewAxisArrayAtts.viewportCoords = (0.15, 0.9, 0.1, 0.85)
	SetViewAxisArray(ViewAxisArrayAtts)

generate_streamlines(seeds)
View_parameters()

ActivateDatabase("localhost:/datarepo/forashok/BBH.visit")
SetTimeSliderState(22)

def add_blackholes():
	AddPlot("Pseudocolor", "BBH_mesh", 1, 0)
	# Begin spontaneous state
	# End spontaneous state

	PseudocolorAtts = PseudocolorAttributes()
	PseudocolorAtts.scaling = PseudocolorAtts.Linear  # Linear, Log, Skew
	PseudocolorAtts.skewFactor = 1
	PseudocolorAtts.limitsMode = PseudocolorAtts.OriginalData  # OriginalData, CurrentPlot
	PseudocolorAtts.minFlag = 0
	PseudocolorAtts.min = 0
	PseudocolorAtts.maxFlag = 0
	PseudocolorAtts.max = 1
	PseudocolorAtts.centering = PseudocolorAtts.Natural  # Natural, Nodal, Zonal
	PseudocolorAtts.colorTableName = "hot"
	PseudocolorAtts.invertColorTable = 0
	PseudocolorAtts.opacityType = PseudocolorAtts.FullyOpaque  # ColorTable, FullyOpaque, Constant, Ramp, VariableRange
	PseudocolorAtts.opacityVariable = ""
	PseudocolorAtts.opacity = 1
	PseudocolorAtts.opacityVarMin = 0
	PseudocolorAtts.opacityVarMax = 1
	PseudocolorAtts.opacityVarMinFlag = 0
	PseudocolorAtts.opacityVarMaxFlag = 0
	PseudocolorAtts.pointSize = 0.05
	PseudocolorAtts.pointType = PseudocolorAtts.Point  # Box, Axis, Icosahedron, Octahedron, Tetrahedron, SphereGeometry, Point, Sphere
	PseudocolorAtts.pointSizeVarEnabled = 0
	PseudocolorAtts.pointSizeVar = "default"
	PseudocolorAtts.pointSizePixels = 2
	PseudocolorAtts.lineStyle = PseudocolorAtts.SOLID  # SOLID, DASH, DOT, DOTDASH
	PseudocolorAtts.lineType = PseudocolorAtts.Line  # Line, Tube, Ribbon
	PseudocolorAtts.lineWidth = 0
	PseudocolorAtts.tubeResolution = 10
	PseudocolorAtts.tubeRadiusSizeType = PseudocolorAtts.FractionOfBBox  # Absolute, FractionOfBBox
	PseudocolorAtts.tubeRadiusAbsolute = 0.125
	PseudocolorAtts.tubeRadiusBBox = 0.005
	PseudocolorAtts.tubeRadiusVarEnabled = 0
	PseudocolorAtts.tubeRadiusVar = ""
	PseudocolorAtts.tubeRadiusVarRatio = 10
	PseudocolorAtts.tailStyle = PseudocolorAtts.None  # None, Spheres, Cones
	PseudocolorAtts.headStyle = PseudocolorAtts.None  # None, Spheres, Cones
	PseudocolorAtts.endPointRadiusSizeType = PseudocolorAtts.FractionOfBBox  # Absolute, FractionOfBBox
	PseudocolorAtts.endPointRadiusAbsolute = 0.125
	PseudocolorAtts.endPointRadiusBBox = 0.05
	PseudocolorAtts.endPointResolution = 10
	PseudocolorAtts.endPointRatio = 5
	PseudocolorAtts.endPointRadiusVarEnabled = 0
	PseudocolorAtts.endPointRadiusVar = ""
	PseudocolorAtts.endPointRadiusVarRatio = 10
	PseudocolorAtts.renderSurfaces = 1
	PseudocolorAtts.renderWireframe = 1
	PseudocolorAtts.renderPoints = 1
	PseudocolorAtts.smoothingLevel = 0
	PseudocolorAtts.legendFlag = 0
	PseudocolorAtts.lightingFlag = 1
	PseudocolorAtts.wireframeColor = (0, 0, 0, 0)
	PseudocolorAtts.pointColor = (0, 0, 0, 0)
	SetPlotOptions(PseudocolorAtts)
	DrawPlots()

add_blackholes()
View_parameters()

SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/home/aschoudhary/Streamline_project/plots/top_view"
SaveWindowAtts.fileName = "FigureTest" 
SaveWindowAtts.family = 1
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()

ActivateDatabase("localhost:/datarepo/forashok/Bx.file_* database")
SetTimeSliderState(25)
# The AnimationPlay RPC is not supported in the VisIt module so it will not be logged.
# Begin spontaneous state
def side_view():
	View3DAtts = View3DAttributes()
	View3DAtts.viewNormal = (-0.751802, -0.533877, 0.387)
	View3DAtts.focus = (-0.000119686, 0, 0)
	View3DAtts.viewUp = (0.160992, 0.42053, 0.892881)
	View3DAtts.viewAngle = 30
	View3DAtts.parallelScale = 25.02
	View3DAtts.nearPlane = -50.04
	View3DAtts.farPlane = 50.04
	View3DAtts.imagePan = (0, 0)
	View3DAtts.imageZoom = 0.5
	View3DAtts.perspective = 1
	View3DAtts.eyeAngle = 2
	View3DAtts.centerOfRotationSet = 0
	View3DAtts.centerOfRotation = (-0.000119686, 0, 0)
	View3DAtts.axis3DScaleFlag = 0
	View3DAtts.axis3DScales = (1, 1, 1)
	View3DAtts.shear = (0, 0, 1)
	View3DAtts.windowValid = 1
	SetView3D(View3DAtts)
	# End spontaneous state

def top_view():
	View3DAtts = View3DAttributes()
	View3DAtts.viewNormal = (0, 0, 1)
	View3DAtts.focus = (0, 0, 0)
	View3DAtts.viewUp = (0, 1, 0)
	View3DAtts.viewAngle = 30
	View3DAtts.parallelScale = 24.4949
	View3DAtts.nearPlane = -48.9898
	View3DAtts.farPlane = 48.9898
	View3DAtts.imagePan = (0, 0)
	View3DAtts.imageZoom = 0.5
	View3DAtts.perspective = 1
	View3DAtts.eyeAngle = 2
	View3DAtts.centerOfRotationSet = 0
	View3DAtts.centerOfRotation = (0, 0, 0)
	View3DAtts.axis3DScaleFlag = 0
	View3DAtts.axis3DScales = (1, 1, 1)
	View3DAtts.shear = (0, 0, 1)
	View3DAtts.windowValid = 1
	SetView3D(View3DAtts)



side_view()


ActivateDatabase("localhost:/datarepo/forashok/BBH.visit")
SetTimeSliderState(25)
# The AnimationPlay RPC is not supported in the VisIt module so it will not be logged.
# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (-0.751802, -0.533877, 0.387)
View3DAtts.focus = (-0.000119686, 0, 0)
View3DAtts.viewUp = (0.160992, 0.42053, 0.892881)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 24.9997
View3DAtts.nearPlane = -49.9994
View3DAtts.farPlane = 49.9994
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (-0.000119686, 0, 0)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
# End spontaneous state

# The AnimationStop RPC is not supported in the VisIt module so it will not be logged.

SaveWindowAtts = SaveWindowAttributes()
SaveWindowAtts.outputToCurrentDirectory = 0
SaveWindowAtts.outputDirectory = "/home/aschoudhary/Streamline_project/plots/side_view"
SaveWindowAtts.fileName = "FigureTest" 
SaveWindowAtts.family = 1
SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
SetSaveWindowAttributes(SaveWindowAtts)
SaveWindow()
ActivateDatabase("localhost:/datarepo/forashok/Bx.file_* database")
DeleteActivePlots()
ActivateDatabase("localhost:/datarepo/forashok/BBH.visit")
DeleteActivePlots()


for time_index in range(90):
	print time_index
	Seed_list = Seed[:,particle_location_index[time_index]]
	radius_of_box = 20
	Particles_inside_box = []
	## coordinates of the particles inside the box

	for i in range(1, len(Seed_list)-3, 3):
		particle_distance_from_centre_of_box = np.sqrt(Seed_list[i]*Seed_list[i] + Seed_list[i+1]*Seed_list[i+1] + Seed_list[i+2]*Seed_list[i+2])
		
		if particle_distance_from_centre_of_box < radius_of_box:
			Particles_inside_box.extend([Seed_list[i], Seed_list[i+1], Seed_list[i+2]])
	Particles_inside_box = tuple(Particles_inside_box)

	ActivateDatabase("localhost:/datarepo/forashok/Bx.file_* database")
	SetTimeSliderState(time_index + 1)
	generate_streamlines(Particles_inside_box)
	
	# The AnimationPlay RPC is not supported in the VisIt module so it will not be logged.
	# Begin spontaneous state
	side_view()

	# End spontaneous state
	#################################
	Query("Time") 
	time=GetQueryOutputValue()
	print time
	print Seed[0,particle_location_index[time_index]]
	######################################


	ActivateDatabase("localhost:/datarepo/forashok/BBH.visit")
	SetTimeSliderState(time_index +1 )
	add_blackholes()

	# The AnimationPlay RPC is not supported in the VisIt module so it will not be logged.
	# Begin spontaneous state
	
	side_view()
	SaveWindowAtts = SaveWindowAttributes()
	SaveWindowAtts.outputToCurrentDirectory = 0
	SaveWindowAtts.outputDirectory = "/home/aschoudhary/Streamline_project/plots/side_view_movingSeeds"
	SaveWindowAtts.fileName = "FigureTest" 
	SaveWindowAtts.family = 1
	SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
	SetSaveWindowAttributes(SaveWindowAtts)
	SaveWindow()

	top_view()
	SaveWindowAtts = SaveWindowAttributes()
	SaveWindowAtts.outputToCurrentDirectory = 0
	SaveWindowAtts.outputDirectory = "/home/aschoudhary/Streamline_project/plots/top_view_movingSeeds"
	SaveWindowAtts.fileName = "FigureTest" 
	SaveWindowAtts.family = 1
	SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
	SetSaveWindowAttributes(SaveWindowAtts)
	SaveWindow() 
	ActivateDatabase("localhost:/datarepo/forashok/Bx.file_* database")
	DeleteActivePlots()
	ActivateDatabase("localhost:/datarepo/forashok/BBH.visit")
	DeleteActivePlots()



	

