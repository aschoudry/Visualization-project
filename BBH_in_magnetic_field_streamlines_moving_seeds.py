import numpy as np
import sys
#Specify where visit is installed in your system
sys.path.append("/home/aschoudhary/local/2.12.2/linux-x86_64/lib/site-packages/")

import visit
from visit import*
Launch()

##########################################################################################################
#################### Specify the location of data ########################################################

Bfield_data = "localhost:/datarepo/forashok/zero_Degrees_Rotation/Bxyz.file_* database"
Black_hole_horizon = "localhost:/datarepo/forashok/zero_Degrees_Rotation/BH_data/BBH.visit"
Black_hole1_centre = "/datarepo/forashok/zero_Degrees_Rotation/BH_data/BH1_origin-parsed.txt"
Black_hole2_centre = "/datarepo/forashok/zero_Degrees_Rotation/BH_data/BH2_origin-parsed.txt"

##########################################################################################################
##################### Open data files ####################################################################

OpenDatabase(Bfield_data, 0, "CarpetHDF5")
OpenDatabase(Black_hole_horizon, 0, "PlainText")

BH1_centre_x, BH1_centre_y, BH1_centre_z = np.loadtxt(Black_hole1_centre, unpack=True)
BH2_centre_x, BH2_centre_y, BH2_centre_z = np.loadtxt(Black_hole2_centre, unpack=True)

#########################################################################################################
#######create expressions to define each componets of normailzed magnetic ffield ########################
#1) B_field data
ActivateDatabase(Bfield_data)
DefineScalarExpression("Bx", "<GIRAFFE--Bx>")
DefineScalarExpression("By", "<GIRAFFE--By>")
DefineScalarExpression("Bz", "<GIRAFFE--Bz>")
DefineScalarExpression("Bnorm", "sqrt(Bx*Bx + By*By + Bz*Bz)")
DefineVectorExpression("Bvec", "{Bx/Bnorm, By/Bnorm, Bz/Bnorm}")
#2) BBH data
ActivateDatabase(Black_hole_horizon)
DefineScalarExpression("BBH_mesh", "var00")


#############################################################################################################
############## get seed points around Blackholes given it's centre and radius ###############################

def Stationary_seeds_around_BBH(BH_x, BH_y, BH_z, BH_radius):
	N = 64 		               #total number of seeds desired within circle
	Neff = int(np.sqrt(N*(4/np.pi)))       #number of seeds needed across each side of circumscribing square
	domain = np.linspace(-BH_radius, BH_radius, (Neff))

	x = np.zeros((Neff, Neff))        
	y = np.zeros((Neff, Neff))
	z = np.ones((Neff, Neff))
	for i in range(Neff):
		for j in range(Neff):
			if domain[i]*domain[i] + domain[j]*domain[j] <= BH_radius*BH_radius:
				x[i,j] = BH_x + domain[i]
				y[i,j] = BH_y + domain[j]
			else:
				x[i,j] = float('nan')
				y[i,j] = float('nan')
	
	X = []
	Y = []

	for i in range(Neff):
		for j in range(Neff):
			X.extend([x[i,j]])
			Y.extend([y[i,j]])
	Z = np.ones(len(X))

	seeds = []
	
	for i in range(len(X)):
		seeds.extend([X[i], Y[i], Z[i]])	



	return seeds
############################################################################################################
########### get particle inside a spherical volume around each blackhole ###################################

def Moving_seeds_around_BBH(BH_x, BH_y, BH_z, BH_radius, Seed_list): 
	
	inner_radius_for_seeds = BH_radius
	outer_radius_for_seeds = 4*BH_radius

	particles_around_BH = []

	for i in range(0, len(Seed_list)-3, 3):
		
		particle_distance_from_centre_of_BH = np.sqrt((Seed_list[i]-BH_x)**2 + (Seed_list[i+1]-BH_y)**2 + (Seed_list[i+2]-BH_z)**2)
		
		if particle_distance_from_centre_of_BH > inner_radius_for_seeds and particle_distance_from_centre_of_BH < outer_radius_for_seeds:
			particles_around_BH.extend([Seed_list[i], Seed_list[i+1], Seed_list[i+2]])
	
	#particles_around_BH = tuple(particles_around_BH)
	
	return particles_around_BH



################################################################################################################################################
################################### functions that computer streamlines from data ##############################################################
################################################################################################################################################


#Generate integral curves 
ActivateDatabase(Bfield_data)

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
	IntegralCurveAtts.integrationDirection = IntegralCurveAtts.Forward  # Forward, Backward, Both, ForwardDirectionless, BackwardDirectionless, BothDirectionless
	IntegralCurveAtts.maxSteps = 150
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
	ReflectAtts.reflections = (1, 0, 0, 0, 0, 0, 0, 1)
	SetOperatorOptions(ReflectAtts, 0)
	DrawPlots()
				
def add_blackholes():
	ActivateDatabase(Black_hole_horizon)
	AddPlot("Pseudocolor", "BBH_mesh", 1, 0)
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
	PseudocolorAtts.pointSize = 0.95
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
			
def side_view(zoom, scale_axis_x, scale_axis_y, scale_axis_z):
	View3DAtts = View3DAttributes()
	View3DAtts.viewNormal = (-0.751802, -0.533877, 0.387)
	View3DAtts.focus = (-0.000119686, 0, 0)
	View3DAtts.viewUp = (0.160992, 0.42053, 0.892881)
	View3DAtts.viewAngle = 30
	View3DAtts.parallelScale = 25.02
	View3DAtts.nearPlane = -50.04
	View3DAtts.farPlane = 50.04
	View3DAtts.imagePan = (0, 0)
	View3DAtts.imageZoom = zoom
	View3DAtts.perspective = 1
	View3DAtts.eyeAngle = 2
	View3DAtts.centerOfRotationSet = 0
	View3DAtts.centerOfRotation = (-0.000119686, 0, 0)
	View3DAtts.axis3DScaleFlag = 1
	View3DAtts.axis3DScales = (scale_axis_x, scale_axis_y, scale_axis_z)
	View3DAtts.shear = (0, 0, 1)
	View3DAtts.windowValid = 1
	SetView3D(View3DAtts)

def Annotations(xmin, xmax, ymin, ymax, zmin, zmax):
	AnnotationAtts = AnnotationAttributes()
	AnnotationAtts.axes2D.visible = 1
	AnnotationAtts.axes2D.autoSetTicks = 1
	AnnotationAtts.axes2D.autoSetScaling = 1
	AnnotationAtts.axes2D.lineWidth = 0
	AnnotationAtts.axes2D.tickLocation = AnnotationAtts.axes2D.Outside  # Inside, Outside, Both
	AnnotationAtts.axes2D.tickAxes = AnnotationAtts.axes2D.BottomLeft  # Off, Bottom, Left, BottomLeft, All
	AnnotationAtts.axes2D.xAxis.title.visible = 1
	AnnotationAtts.axes2D.xAxis.title.font.font = AnnotationAtts.axes2D.xAxis.title.font.Courier  # Arial, Courier, Times
	AnnotationAtts.axes2D.xAxis.title.font.scale = 1
	AnnotationAtts.axes2D.xAxis.title.font.useForegroundColor = 1
	AnnotationAtts.axes2D.xAxis.title.font.color = (0, 0, 0, 255)
	AnnotationAtts.axes2D.xAxis.title.font.bold = 1
	AnnotationAtts.axes2D.xAxis.title.font.italic = 1
	AnnotationAtts.axes2D.xAxis.title.userTitle = 0
	AnnotationAtts.axes2D.xAxis.title.userUnits = 0
	AnnotationAtts.axes2D.xAxis.title.title = "X-Axis"
	AnnotationAtts.axes2D.xAxis.title.units = ""
	AnnotationAtts.axes2D.xAxis.label.visible = 1
	AnnotationAtts.axes2D.xAxis.label.font.font = AnnotationAtts.axes2D.xAxis.label.font.Courier  # Arial, Courier, Times
	AnnotationAtts.axes2D.xAxis.label.font.scale = 1
	AnnotationAtts.axes2D.xAxis.label.font.useForegroundColor = 1
	AnnotationAtts.axes2D.xAxis.label.font.color = (0, 0, 0, 255)
	AnnotationAtts.axes2D.xAxis.label.font.bold = 1
	AnnotationAtts.axes2D.xAxis.label.font.italic = 1
	AnnotationAtts.axes2D.xAxis.label.scaling = 0
	AnnotationAtts.axes2D.xAxis.tickMarks.visible = 1
	AnnotationAtts.axes2D.xAxis.tickMarks.majorMinimum = 0
	AnnotationAtts.axes2D.xAxis.tickMarks.majorMaximum = 1
	AnnotationAtts.axes2D.xAxis.tickMarks.minorSpacing = 0.02
	AnnotationAtts.axes2D.xAxis.tickMarks.majorSpacing = 0.2
	AnnotationAtts.axes2D.xAxis.grid = 0
	AnnotationAtts.axes2D.yAxis.title.visible = 1
	AnnotationAtts.axes2D.yAxis.title.font.font = AnnotationAtts.axes2D.yAxis.title.font.Courier  # Arial, Courier, Times
	AnnotationAtts.axes2D.yAxis.title.font.scale = 1
	AnnotationAtts.axes2D.yAxis.title.font.useForegroundColor = 1
	AnnotationAtts.axes2D.yAxis.title.font.color = (0, 0, 0, 255)
	AnnotationAtts.axes2D.yAxis.title.font.bold = 1
	AnnotationAtts.axes2D.yAxis.title.font.italic = 1
	AnnotationAtts.axes2D.yAxis.title.userTitle = 0
	AnnotationAtts.axes2D.yAxis.title.userUnits = 0
	AnnotationAtts.axes2D.yAxis.title.title = "Y-Axis"
	AnnotationAtts.axes2D.yAxis.title.units = ""
	AnnotationAtts.axes2D.yAxis.label.visible = 1
	AnnotationAtts.axes2D.yAxis.label.font.font = AnnotationAtts.axes2D.yAxis.label.font.Courier  # Arial, Courier, Times
	AnnotationAtts.axes2D.yAxis.label.font.scale = 1
	AnnotationAtts.axes2D.yAxis.label.font.useForegroundColor = 1
	AnnotationAtts.axes2D.yAxis.label.font.color = (0, 0, 0, 255)
	AnnotationAtts.axes2D.yAxis.label.font.bold = 1
	AnnotationAtts.axes2D.yAxis.label.font.italic = 1
	AnnotationAtts.axes2D.yAxis.label.scaling = 0
	AnnotationAtts.axes2D.yAxis.tickMarks.visible = 1
	AnnotationAtts.axes2D.yAxis.tickMarks.majorMinimum = 0
	AnnotationAtts.axes2D.yAxis.tickMarks.majorMaximum = 1
	AnnotationAtts.axes2D.yAxis.tickMarks.minorSpacing = 0.02
	AnnotationAtts.axes2D.yAxis.tickMarks.majorSpacing = 0.2
	AnnotationAtts.axes2D.yAxis.grid = 0
	AnnotationAtts.axes3D.visible = 1
	AnnotationAtts.axes3D.autoSetTicks = 1
	AnnotationAtts.axes3D.autoSetScaling = 1
	AnnotationAtts.axes3D.lineWidth = 0
	AnnotationAtts.axes3D.tickLocation = AnnotationAtts.axes3D.Inside  # Inside, Outside, Both
	AnnotationAtts.axes3D.axesType = AnnotationAtts.axes3D.ClosestTriad  # ClosestTriad, FurthestTriad, OutsideEdges, StaticTriad, StaticEdges
	AnnotationAtts.axes3D.triadFlag = 1
	AnnotationAtts.axes3D.bboxFlag = 1
	AnnotationAtts.axes3D.xAxis.title.visible = 1
	AnnotationAtts.axes3D.xAxis.title.font.font = AnnotationAtts.axes3D.xAxis.title.font.Arial  # Arial, Courier, Times
	AnnotationAtts.axes3D.xAxis.title.font.scale = 1
	AnnotationAtts.axes3D.xAxis.title.font.useForegroundColor = 1
	AnnotationAtts.axes3D.xAxis.title.font.color = (0, 0, 0, 255)
	AnnotationAtts.axes3D.xAxis.title.font.bold = 0
	AnnotationAtts.axes3D.xAxis.title.font.italic = 0
	AnnotationAtts.axes3D.xAxis.title.userTitle = 0
	AnnotationAtts.axes3D.xAxis.title.userUnits = 0
	AnnotationAtts.axes3D.xAxis.title.title = "X-Axis"
	AnnotationAtts.axes3D.xAxis.title.units = ""
	AnnotationAtts.axes3D.xAxis.label.visible = 1
	AnnotationAtts.axes3D.xAxis.label.font.font = AnnotationAtts.axes3D.xAxis.label.font.Arial  # Arial, Courier, Times
	AnnotationAtts.axes3D.xAxis.label.font.scale = 1
	AnnotationAtts.axes3D.xAxis.label.font.useForegroundColor = 1
	AnnotationAtts.axes3D.xAxis.label.font.color = (0, 0, 0, 255)
	AnnotationAtts.axes3D.xAxis.label.font.bold = 0
	AnnotationAtts.axes3D.xAxis.label.font.italic = 0
	AnnotationAtts.axes3D.xAxis.label.scaling = 0
	AnnotationAtts.axes3D.xAxis.tickMarks.visible = 1
	AnnotationAtts.axes3D.xAxis.tickMarks.majorMinimum = 0
	AnnotationAtts.axes3D.xAxis.tickMarks.majorMaximum = 1
	AnnotationAtts.axes3D.xAxis.tickMarks.minorSpacing = 0.02
	AnnotationAtts.axes3D.xAxis.tickMarks.majorSpacing = 0.2
	AnnotationAtts.axes3D.xAxis.grid = 0
	AnnotationAtts.axes3D.yAxis.title.visible = 1
	AnnotationAtts.axes3D.yAxis.title.font.font = AnnotationAtts.axes3D.yAxis.title.font.Arial  # Arial, Courier, Times
	AnnotationAtts.axes3D.yAxis.title.font.scale = 1
	AnnotationAtts.axes3D.yAxis.title.font.useForegroundColor = 1
	AnnotationAtts.axes3D.yAxis.title.font.color = (0, 0, 0, 255)
	AnnotationAtts.axes3D.yAxis.title.font.bold = 0
	AnnotationAtts.axes3D.yAxis.title.font.italic = 0
	AnnotationAtts.axes3D.yAxis.title.userTitle = 0
	AnnotationAtts.axes3D.yAxis.title.userUnits = 0
	AnnotationAtts.axes3D.yAxis.title.title = "Y-Axis"
	AnnotationAtts.axes3D.yAxis.title.units = ""
	AnnotationAtts.axes3D.yAxis.label.visible = 1
	AnnotationAtts.axes3D.yAxis.label.font.font = AnnotationAtts.axes3D.yAxis.label.font.Arial  # Arial, Courier, Times
	AnnotationAtts.axes3D.yAxis.label.font.scale = 1
	AnnotationAtts.axes3D.yAxis.label.font.useForegroundColor = 1
	AnnotationAtts.axes3D.yAxis.label.font.color = (0, 0, 0, 255)
	AnnotationAtts.axes3D.yAxis.label.font.bold = 0
	AnnotationAtts.axes3D.yAxis.label.font.italic = 0
	AnnotationAtts.axes3D.yAxis.label.scaling = 0
	AnnotationAtts.axes3D.yAxis.tickMarks.visible = 1
	AnnotationAtts.axes3D.yAxis.tickMarks.majorMinimum = 0
	AnnotationAtts.axes3D.yAxis.tickMarks.majorMaximum = 1
	AnnotationAtts.axes3D.yAxis.tickMarks.minorSpacing = 0.02
	AnnotationAtts.axes3D.yAxis.tickMarks.majorSpacing = 0.2
	AnnotationAtts.axes3D.yAxis.grid = 0
	AnnotationAtts.axes3D.zAxis.title.visible = 1
	AnnotationAtts.axes3D.zAxis.title.font.font = AnnotationAtts.axes3D.zAxis.title.font.Arial  # Arial, Courier, Times
	AnnotationAtts.axes3D.zAxis.title.font.scale = 1
	AnnotationAtts.axes3D.zAxis.title.font.useForegroundColor = 1
	AnnotationAtts.axes3D.zAxis.title.font.color = (0, 0, 0, 255)
	AnnotationAtts.axes3D.zAxis.title.font.bold = 0
	AnnotationAtts.axes3D.zAxis.title.font.italic = 0
	AnnotationAtts.axes3D.zAxis.title.userTitle = 0
	AnnotationAtts.axes3D.zAxis.title.userUnits = 0
	AnnotationAtts.axes3D.zAxis.title.title = "Z-Axis"
	AnnotationAtts.axes3D.zAxis.title.units = ""
	AnnotationAtts.axes3D.zAxis.label.visible = 1
	AnnotationAtts.axes3D.zAxis.label.font.font = AnnotationAtts.axes3D.zAxis.label.font.Arial  # Arial, Courier, Times
	AnnotationAtts.axes3D.zAxis.label.font.scale = 1
	AnnotationAtts.axes3D.zAxis.label.font.useForegroundColor = 1
	AnnotationAtts.axes3D.zAxis.label.font.color = (0, 0, 0, 255)
	AnnotationAtts.axes3D.zAxis.label.font.bold = 0
	AnnotationAtts.axes3D.zAxis.label.font.italic = 0
	AnnotationAtts.axes3D.zAxis.label.scaling = 0
	AnnotationAtts.axes3D.zAxis.tickMarks.visible = 1
	AnnotationAtts.axes3D.zAxis.tickMarks.majorMinimum = 0
	AnnotationAtts.axes3D.zAxis.tickMarks.majorMaximum = 1
	AnnotationAtts.axes3D.zAxis.tickMarks.minorSpacing = 0.02
	AnnotationAtts.axes3D.zAxis.tickMarks.majorSpacing = 0.2
	AnnotationAtts.axes3D.zAxis.grid = 0
	AnnotationAtts.axes3D.setBBoxLocation = 1
	AnnotationAtts.axes3D.bboxLocation = (xmin, xmax, ymin, ymax, zmin, zmax)
	AnnotationAtts.userInfoFlag = 1
	AnnotationAtts.userInfoFont.font = AnnotationAtts.userInfoFont.Arial  # Arial, Courier, Times
	AnnotationAtts.userInfoFont.scale = 1
	AnnotationAtts.userInfoFont.useForegroundColor = 1
	AnnotationAtts.userInfoFont.color = (0, 0, 0, 255)
	AnnotationAtts.userInfoFont.bold = 0
	AnnotationAtts.userInfoFont.italic = 0
	AnnotationAtts.databaseInfoFlag = 1
	AnnotationAtts.timeInfoFlag = 1
	AnnotationAtts.databaseInfoFont.font = AnnotationAtts.databaseInfoFont.Arial  # Arial, Courier, Times
	AnnotationAtts.databaseInfoFont.scale = 1
	AnnotationAtts.databaseInfoFont.useForegroundColor = 1
	AnnotationAtts.databaseInfoFont.color = (0, 0, 0, 255)
	AnnotationAtts.databaseInfoFont.bold = 0
	AnnotationAtts.databaseInfoFont.italic = 0
	AnnotationAtts.databaseInfoExpansionMode = AnnotationAtts.File  # File, Directory, Full, Smart, SmartDirectory
	AnnotationAtts.databaseInfoTimeScale = 1
	AnnotationAtts.databaseInfoTimeOffset = 0
	AnnotationAtts.legendInfoFlag = 1
	AnnotationAtts.backgroundColor = (255, 255, 255, 255)
	AnnotationAtts.foregroundColor = (0, 0, 0, 255)
	AnnotationAtts.gradientBackgroundStyle = AnnotationAtts.Radial  # TopToBottom, BottomToTop, LeftToRight, RightToLeft, Radial
	AnnotationAtts.gradientColor1 = (0, 0, 255, 255)
	AnnotationAtts.gradientColor2 = (0, 0, 0, 255)
	AnnotationAtts.backgroundMode = AnnotationAtts.Solid  # Solid, Gradient, Image, ImageSphere
	AnnotationAtts.backgroundImage = ""
	AnnotationAtts.imageRepeatX = 1
	AnnotationAtts.imageRepeatY = 1
	AnnotationAtts.axesArray.visible = 1
	AnnotationAtts.axesArray.ticksVisible = 1
	AnnotationAtts.axesArray.autoSetTicks = 1
	AnnotationAtts.axesArray.autoSetScaling = 1
	AnnotationAtts.axesArray.lineWidth = 0
	AnnotationAtts.axesArray.axes.title.visible = 1
	AnnotationAtts.axesArray.axes.title.font.font = AnnotationAtts.axesArray.axes.title.font.Arial  # Arial, Courier, Times
	AnnotationAtts.axesArray.axes.title.font.scale = 1
	AnnotationAtts.axesArray.axes.title.font.useForegroundColor = 1
	AnnotationAtts.axesArray.axes.title.font.color = (0, 0, 0, 255)
	AnnotationAtts.axesArray.axes.title.font.bold = 0
	AnnotationAtts.axesArray.axes.title.font.italic = 0
	AnnotationAtts.axesArray.axes.title.userTitle = 0
	AnnotationAtts.axesArray.axes.title.userUnits = 0
	AnnotationAtts.axesArray.axes.title.title = ""
	AnnotationAtts.axesArray.axes.title.units = ""
	AnnotationAtts.axesArray.axes.label.visible = 1
	AnnotationAtts.axesArray.axes.label.font.font = AnnotationAtts.axesArray.axes.label.font.Arial  # Arial, Courier, Times
	AnnotationAtts.axesArray.axes.label.font.scale = 1
	AnnotationAtts.axesArray.axes.label.font.useForegroundColor = 1
	AnnotationAtts.axesArray.axes.label.font.color = (0, 0, 0, 255)
	AnnotationAtts.axesArray.axes.label.font.bold = 0
	AnnotationAtts.axesArray.axes.label.font.italic = 0
	AnnotationAtts.axesArray.axes.label.scaling = 0
	AnnotationAtts.axesArray.axes.tickMarks.visible = 1
	AnnotationAtts.axesArray.axes.tickMarks.majorMinimum = 0
	AnnotationAtts.axesArray.axes.tickMarks.majorMaximum = 1
	AnnotationAtts.axesArray.axes.tickMarks.minorSpacing = 0.02
	AnnotationAtts.axesArray.axes.tickMarks.majorSpacing = 0.2
	AnnotationAtts.axesArray.axes.grid = 0
	SetAnnotationAttributes(AnnotationAtts)



for time_index in range(393):
#time_index = 392
	zoom = 1
	scale_axis_x = 1
	scale_axis_y = 1
	scale_axis_z = 1
	BH_frequency = int(time_index*4)
	Particles_around_BH1 = Stationary_seeds_around_BBH(BH1_centre_x[BH_frequency], BH1_centre_y[BH_frequency], BH1_centre_z[BH_frequency], 1.4)
	Particles_around_BH2 = Stationary_seeds_around_BBH(BH2_centre_x[BH_frequency], BH2_centre_y[BH_frequency], BH2_centre_z[BH_frequency], 1.4)
	Particle_seeds = Particles_around_BH1 + Particles_around_BH2
	Particle_seeds= tuple(Particle_seeds)
	ActivateDatabase(Bfield_data)
	SetTimeSliderState(time_index)
	generate_streamlines(Particle_seeds)
	Annotations(-9, 9, -9, 9, -16, 16)
	side_view(zoom,scale_axis_x, scale_axis_y, scale_axis_z )
	ActivateDatabase(Black_hole_horizon)
	SetTimeSliderState(BH_frequency)
	add_blackholes()


#	SaveWindowAtts = SaveWindowAttributes()
#	SaveWindowAtts.outputToCurrentDirectory = 0
#	SaveWindowAtts.outputDirectory = "/home/aschoudhary/Streamline_project/plots/side_view_v1"
#	SaveWindowAtts.fileName = "FigureTest" 
#	SaveWindowAtts.family = 1
#	SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
#	SetSaveWindowAttributes(SaveWindowAtts)
#	SaveWindow()
#	DeleteActivePlots()
#	DeleteActivePlots()




	

	






