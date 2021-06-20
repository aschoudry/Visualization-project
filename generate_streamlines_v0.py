import numpy as np
import sys
#Specify where visit is installed in your system
sys.path.append("/home/aschoudhary/local/2.12.2/linux-x86_64/lib/site-packages/")

import visit
from visit import*
LaunchNowin()

def Generate_streamlines(Seeds, time_index):
	
	AddPlot("Pseudocolor", "operators/IntegralCurve/Bvec", 1, 1)
	
	SetTimeSliderState(time_index)
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
	IntegralCurveAtts.pointList = Seeds
	IntegralCurveAtts.fieldData = ()
	IntegralCurveAtts.sampleDensity0 = 2
	IntegralCurveAtts.sampleDensity1 = 2
	IntegralCurveAtts.sampleDensity2 = 2
	IntegralCurveAtts.dataValue = IntegralCurveAtts.TimeAbsolute  # Solid, SeedPointID, Speed, Vorticity, ArcLength, TimeAbsolute, TimeRelative, AverageDistanceFromSeed, CorrelationDistance, Difference, Variable
	IntegralCurveAtts.dataVariable = ""
	IntegralCurveAtts.integrationDirection = IntegralCurveAtts.Both  # Forward, Backward, Both, ForwardDirectionless, BackwardDirectionless, BothDirectionless
	IntegralCurveAtts.maxSteps = 10
	IntegralCurveAtts.terminateByDistance = 0
	IntegralCurveAtts.termDistance = 10
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
	IntegralCurveAtts.integrationType = IntegralCurveAtts.DormandPrince  # Euler, Leapfrog, DormandPrince, AdamsBashforth, RK4, M3DC12DIntegrator
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
	SetOperatorOptions(IntegralCurveAtts, 1)

	
	AddOperator("Box", 1)
	BoxAtts = BoxAttributes()
	BoxAtts.amount = BoxAtts.Some  # Some, All
	BoxAtts.minx = -20
	BoxAtts.maxx = 20
	BoxAtts.miny = -20
	BoxAtts.maxy = 20
	BoxAtts.minz = -20
	BoxAtts.maxz = 20
	BoxAtts.inverse = 0
	SetOperatorOptions(BoxAtts, 1)
	
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
	PseudocolorAtts.opacityType = PseudocolorAtts.ColorTable  # ColorTable, FullyOpaque, Constant, Ramp, VariableRange
	PseudocolorAtts.opacityVariable = ""
	PseudocolorAtts.opacity = 0
	PseudocolorAtts.opacityVarMin = 0
	PseudocolorAtts.opacityVarMax = 1
	PseudocolorAtts.opacityVarMinFlag = 0
	PseudocolorAtts.opacityVarMaxFlag = 0
	PseudocolorAtts.pointSize = 0.5
	PseudocolorAtts.pointType = PseudocolorAtts.Point  # Box, Axis, Icosahedron, Octahedron, Tetrahedron, SphereGeometry, Point, Sphere
	PseudocolorAtts.pointSizeVarEnabled = 0
	PseudocolorAtts.pointSizeVar = "default"
	PseudocolorAtts.pointSizePixels = 2
	PseudocolorAtts.lineStyle = PseudocolorAtts.SOLID  # SOLID, DASH, DOT, DOTDASH
	PseudocolorAtts.lineType = PseudocolorAtts.Tube  # Line, Tube, Ribbon
	PseudocolorAtts.lineWidth = 0
	PseudocolorAtts.tubeResolution = 10
	PseudocolorAtts.tubeRadiusSizeType = PseudocolorAtts.FractionOfBBox  # Absolute, FractionOfBBox
	PseudocolorAtts.tubeRadiusAbsolute = 0.925
	PseudocolorAtts.tubeRadiusBBox = 2e-01
	PseudocolorAtts.tubeRadiusVarEnabled = 0
	PseudocolorAtts.tubeRadiusVar = ""
	PseudocolorAtts.tubeRadiusVarRatio = 10
	PseudocolorAtts.tailStyle = PseudocolorAtts.Spheres  # None, Spheres, Cones
	PseudocolorAtts.headStyle = PseudocolorAtts.Spheres  # None, Spheres, Cones
	PseudocolorAtts.endPointRadiusSizeType = PseudocolorAtts.FractionOfBBox  # Absolute, FractionOfBBox
	PseudocolorAtts.endPointRadiusAbsolute = 0.925
	PseudocolorAtts.endPointRadiusBBox = 2e-02
	PseudocolorAtts.endPointResolution = 10
	PseudocolorAtts.endPointRatio = 5
	PseudocolorAtts.endPointRadiusVarEnabled = 0
	PseudocolorAtts.endPointRadiusVar = ""
	PseudocolorAtts.endPointRadiusVarRatio = 10
	PseudocolorAtts.renderSurfaces = 1
	PseudocolorAtts.renderWireframe = 0
	PseudocolorAtts.renderPoints = 0
	PseudocolorAtts.smoothingLevel = 0
	PseudocolorAtts.legendFlag = 1
	PseudocolorAtts.lightingFlag = 1
	PseudocolorAtts.wireframeColor = (0, 0, 0, 0)
	PseudocolorAtts.pointColor = (0, 0, 0, 0)
	SetPlotOptions(PseudocolorAtts)

		

# Set View options
def View_parameter(zoom):	
		
	View3DAtts = View3DAttributes()
	View3DAtts.viewNormal = (0.529666, 0.623902, 0.57463)
	View3DAtts.focus = (21.3333, 21.3333, 21.3333)
	View3DAtts.viewUp = (0, 0, 1)
	View3DAtts.viewAngle = 30
	View3DAtts.parallelScale = 3510.29
	View3DAtts.nearPlane = -7020.58
	View3DAtts.farPlane = 7020.58
	View3DAtts.imagePan = (0, 0)
	View3DAtts.imageZoom = zoom
	View3DAtts.perspective = 1
	View3DAtts.eyeAngle = 2
	View3DAtts.centerOfRotationSet = 0
	View3DAtts.centerOfRotation = (21.3333, 21.3333, 21.3333)
	View3DAtts.axis3DScaleFlag = 0
	View3DAtts.axis3DScales = (1, 1, 1)
	View3DAtts.shear = (0, 0, 1)
	View3DAtts.windowValid = 1
	SetView3D(View3DAtts)

def Annotation_Attributes():
	
	AnnotationAtts = AnnotationAttributes()	
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
	AnnotationAtts.axes3D.bboxLocation = (-20, 20, -20, 20, -20, 20)
	SetAnnotationAttributes(AnnotationAtts)

#Saving the plots 
def Save_Plots():
	 
	SaveWindowAtts = SaveWindowAttributes()
	SaveWindowAtts.outputToCurrentDirectory = 0
	SaveWindowAtts.outputDirectory = "/home/aschoudhary/Plots"
	SaveWindowAtts.fileName = "FigureTest" 
	SaveWindowAtts.family = 1
	SaveWindowAtts.format = SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
	SetSaveWindowAttributes(SaveWindowAtts)
	SaveWindow()

#open database
OpenDatabase("localhost:/datarepo/forashok/Bx.file_* database", 0)

##Load data for initial seeds from data file
Seed_index = 0
Seed = np.loadtxt('/datarepo/forashok/particles.txt', skiprows = 2, unpack = True)
Seed_list = Seed[:, Seed_index]
radius_of_box = 20
Particles_inside_box = []
## coordinates of the particles inside the box

for i in range(0, len(Seed_list)-3, 3):
	particle_distance_from_centre_of_box = np.sqrt(Seed_list[i]*Seed_list[i] + Seed_list[i+1]*Seed_list[i+1] + Seed_list[i+2]*Seed_list[i+2])
	
	if particle_distance_from_centre_of_box < radius_of_box:
		Particles_inside_box.extend([Seed_list[i], Seed_list[i+1], Seed_list[i+2]])
		

len(Particles_inside_box)

Particles_inside_box = tuple(Particles_inside_box)

View_parameter(100)
time_index = 0
Generate_streamlines(Particles_inside_box, time_index)
Annotation_Attributes()
DrawPlots()

OpenDatabase("localhost:/datarepo/forashok/BBH.visit", 0)
AddPlot("Mesh", "mesh", 1, 0)
#SetTimeSliderState(time_index)
MeshAtts = MeshAttributes()
MeshAtts.legendFlag = 0
MeshAtts.lineStyle = MeshAtts.SOLID  # SOLID, DASH, DOT, DOTDASH
MeshAtts.lineWidth = 0
MeshAtts.meshColor = (0, 0, 0, 255)
MeshAtts.meshColorSource = MeshAtts.Foreground  # Foreground, MeshCustom
MeshAtts.opaqueColorSource = MeshAtts.Background  # Background, OpaqueCustom
MeshAtts.opaqueMode = MeshAtts.Auto  # Auto, On, Off
MeshAtts.pointSize = 0.75
MeshAtts.opaqueColor = (255, 255, 255, 255)
MeshAtts.smoothingLevel = MeshAtts.High  # None, Fast, High
MeshAtts.pointSizeVarEnabled = 0
MeshAtts.pointSizeVar = "default"
MeshAtts.pointType = MeshAtts.SphereGeometry  # Box, Axis, Icosahedron, Octahedron, Tetrahedron, SphereGeometry, Point, Sphere
MeshAtts.showInternal = 0
MeshAtts.pointSizePixels = 2
MeshAtts.opacity = 1
SetPlotOptions(MeshAtts)
DrawPlots()

Save_Plots()


