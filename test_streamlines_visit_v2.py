import numpy as np
import os
from os import*
import sys
sys.path.append("/usr/local/visit/current/linux-x86_64/lib/site-packages")
from os.path import join as pjoin
 
import visit as V
V.LaunchNowin()

##Load data for initial seeds from data file
Seed = np.loadtxt('/home/ashok/Streamline_generation/data/seeds_v1.txt', unpack = True)

V.OpenDatabase("localhost:/home/ashok/Streamline_generation/data/Bx.xz.h5", 0)
V.ToggleCameraViewMode()

# Function that generate Streamlines
 
def Generate_streamlines(Seed_index, Seed_list):

	V.AddPlot("Streamline", "Bvec", 1, 0)

	V.SetTimeSliderState(Seed_index)
	V.StreamlineAtts = V.StreamlineAttributes()
	V.StreamlineAtts.sourceType = V.StreamlineAtts.SpecifiedPointList  # SpecifiedPoint, SpecifiedPointList, SpecifiedLine, SpecifiedCircle, SpecifiedPlane, SpecifiedSphere, SpecifiedBox, Selection

	V.StreamlineAtts.pointSource = (0, 0, 0)
	V.StreamlineAtts.lineStart = (0, 0, 0)
	V.StreamlineAtts.lineEnd = (1, 0, 0)
	V.StreamlineAtts.planeOrigin = (0, 0, 0)
	V.StreamlineAtts.planeNormal = (0, 0, 1)
	V.StreamlineAtts.planeUpAxis = (0, 1, 0)
	V.StreamlineAtts.radius = 1
	V.StreamlineAtts.sphereOrigin = (0, 0, 0)
	V.StreamlineAtts.boxExtents = (0, 1, 0, 1, 0, 1)
	V.StreamlineAtts.useWholeBox = 1
	V.StreamlineAtts.pointList = Seed_list
	V.StreamlineAtts.sampleDensity0 = 2
	V.StreamlineAtts.sampleDensity1 = 2
	V.StreamlineAtts.sampleDensity2 = 2
	V.StreamlineAtts.coloringMethod = V.StreamlineAtts.ColorBySeedPointID  # Solid, ColorBySpeed, ColorByVorticity, ColorByLength, ColorByTime, ColorBySeedPointID, ColorByVariable, ColorByCorrelationDistance, ColorByNumberDomainsVisited
	V.StreamlineAtts.colorTableName = "Default"
	V.StreamlineAtts.singleColor = (0, 0, 0, 255)
	V.StreamlineAtts.legendFlag = 1
	V.StreamlineAtts.lightingFlag = 1
	V.StreamlineAtts.integrationDirection = V.StreamlineAtts.Both  # Forward, Backward, Both
	V.StreamlineAtts.maxSteps = 10000
	V.StreamlineAtts.terminateByDistance = 0
	V.StreamlineAtts.termDistance = 10
	V.StreamlineAtts.terminateByTime = 0
	V.StreamlineAtts.termTime = 10
	V.StreamlineAtts.maxStepLength = 0.1
	V.StreamlineAtts.limitMaximumTimestep = 0
	V.StreamlineAtts.maxTimeStep = 0.1
	V.StreamlineAtts.relTol = 0.0001
	V.StreamlineAtts.absTolSizeType = V.StreamlineAtts.FractionOfBBox  # Absolute, FractionOfBBox
	V.StreamlineAtts.absTolAbsolute = 1e-06
	V.StreamlineAtts.absTolBBox = 1e-06
	V.StreamlineAtts.fieldType = V.StreamlineAtts.Default  # Default, FlashField, M3DC12DField, M3DC13DField, Nek5000Field, NIMRODField
	V.StreamlineAtts.fieldConstant = 1
	V.StreamlineAtts.velocitySource = (0, 0, 0)
	V.StreamlineAtts.integrationType = V.StreamlineAtts.Euler  # Euler, Leapfrog, DormandPrince, AdamsBashforth, RK4, M3DC12DIntegrator
	V.StreamlineAtts.parallelizationAlgorithmType = V.StreamlineAtts.VisItSelects  # LoadOnDemand, ParallelStaticDomains, MasterSlave, VisItSelects
	V.StreamlineAtts.maxProcessCount = 10
	V.StreamlineAtts.maxDomainCacheSize = 3
	V.StreamlineAtts.workGroupSize = 32
	V.StreamlineAtts.pathlines = 0
	V.StreamlineAtts.pathlinesOverrideStartingTimeFlag = 0
	V.StreamlineAtts.pathlinesOverrideStartingTime = 0
	V.StreamlineAtts.pathlinesPeriod = 0
	V.StreamlineAtts.pathlinesCMFE = V.StreamlineAtts.POS_CMFE  # CONN_CMFE, POS_CMFE
	V.StreamlineAtts.coordinateSystem = V.StreamlineAtts.AsIs  # AsIs, CylindricalToCartesian, CartesianToCylindrical
	V.StreamlineAtts.phiScalingFlag = 0
	V.StreamlineAtts.phiScaling = 1
	V.StreamlineAtts.coloringVariable = ""
	V.StreamlineAtts.legendMinFlag = 0
	V.StreamlineAtts.legendMaxFlag = 0
	V.StreamlineAtts.legendMin = 0
	V.StreamlineAtts.legendMax = 1
	V.StreamlineAtts.displayBegin = 0
	V.StreamlineAtts.displayEnd = 1
	V.StreamlineAtts.displayBeginFlag = 0
	V.StreamlineAtts.displayEndFlag = 0
	V.StreamlineAtts.referenceTypeForDisplay = V.StreamlineAtts.Distance  # Distance, Time, Step
	V.StreamlineAtts.displayMethod = V.StreamlineAtts.Tubes  # Lines, Tubes, Ribbons
	V.StreamlineAtts.tubeSizeType = V.StreamlineAtts.FractionOfBBox  # Absolute, FractionOfBBox
	V.StreamlineAtts.tubeRadiusAbsolute = 0.125
	V.StreamlineAtts.tubeRadiusBBox = 0.00385
	V.StreamlineAtts.ribbonWidthSizeType = V.StreamlineAtts.FractionOfBBox  # Absolute, FractionOfBBox
	V.StreamlineAtts.ribbonWidthAbsolute = 0.125
	V.StreamlineAtts.ribbonWidthBBox = 0.01
	V.StreamlineAtts.lineWidth = 2
	V.StreamlineAtts.showSeeds = 1
	V.StreamlineAtts.seedRadiusSizeType = V.StreamlineAtts.FractionOfBBox  # Absolute, FractionOfBBox
	V.StreamlineAtts.seedRadiusAbsolute = 1
	V.StreamlineAtts.seedRadiusBBox = 0.0075
	V.StreamlineAtts.showHeads = 0
	V.StreamlineAtts.headDisplayType = V.StreamlineAtts.Sphere  # Sphere, Cone
	V.StreamlineAtts.headRadiusSizeType = V.StreamlineAtts.FractionOfBBox  # Absolute, FractionOfBBox
	V.StreamlineAtts.headRadiusAbsolute = 0.25
	V.StreamlineAtts.headRadiusBBox = 0.02
	V.StreamlineAtts.headHeightRatio = 2
	V.StreamlineAtts.opacityType = V.StreamlineAtts.FullyOpaque  # FullyOpaque, Constant, Ramp, VariableRange
	V.StreamlineAtts.opacityVariable = ""
	V.StreamlineAtts.opacity = 1
	V.StreamlineAtts.opacityVarMin = 0
	V.StreamlineAtts.opacityVarMax = 1
	V.StreamlineAtts.opacityVarMinFlag = 0
	V.StreamlineAtts.opacityVarMaxFlag = 0
	V.StreamlineAtts.tubeDisplayDensity = 10
	V.StreamlineAtts.geomDisplayQuality = V.StreamlineAtts.Medium  # Low, Medium, High, Super
	V.StreamlineAtts.sampleDistance0 = 10
	V.StreamlineAtts.sampleDistance1 = 10
	V.StreamlineAtts.sampleDistance2 = 10
	V.StreamlineAtts.fillInterior = 1
	V.StreamlineAtts.randomSamples = 0
	V.StreamlineAtts.randomSeed = 0
	V.StreamlineAtts.numberOfRandomSamples = 1
	V.StreamlineAtts.forceNodeCenteredData = 0
	V.StreamlineAtts.issueTerminationWarnings = 1
	V.StreamlineAtts.issueStiffnessWarnings = 1
	V.StreamlineAtts.issueCriticalPointsWarnings = 1
	V.StreamlineAtts.criticalPointThreshold = 0.001
	V.StreamlineAtts.varyTubeRadius = V.StreamlineAtts.None  # None, Scalar
	V.StreamlineAtts.varyTubeRadiusFactor = 10
	V.StreamlineAtts.varyTubeRadiusVariable = ""
	V.StreamlineAtts.correlationDistanceAngTol = 5
	V.StreamlineAtts.correlationDistanceMinDistAbsolute = 1
	V.StreamlineAtts.correlationDistanceMinDistBBox = 0.005
	V.StreamlineAtts.correlationDistanceMinDistType = V.StreamlineAtts.FractionOfBBox  # Absolute, FractionOfBBox
	V.StreamlineAtts.selection = ""
	V.SetPlotOptions(V.StreamlineAtts)
	V.DrawPlots()

#Saving the plots 
def Save_Plots():
	 
	V.SaveWindowAtts = V.SaveWindowAttributes()
	V.SaveWindowAtts.outputToCurrentDirectory = 0
	V.SaveWindowAtts.outputDirectory = "/home/ashok/Streamline_generation/tests/plots"
	V.SaveWindowAtts.fileName = "FigureTest" #+str(Seed_index)
	V.SaveWindowAtts.family = 1
	V.SaveWindowAtts.format = V.SaveWindowAtts.PNG  # BMP, CURVE, JPEG, OBJ, PNG, POSTSCRIPT, POVRAY, PPM, RGB, STL, TIFF, ULTRA, VTK, PLY
	V.SaveWindowAtts.width = 4096
	V.SaveWindowAtts.height = 1024
	V.SaveWindowAtts.screenCapture = 0
	V.SaveWindowAtts.saveTiled = 0
	V.SaveWindowAtts.quality = 100
	V.SaveWindowAtts.progressive = 0
	V.SaveWindowAtts.binary = 0
	V.SaveWindowAtts.stereo = 0
	V.SaveWindowAtts.compression = V.SaveWindowAtts.None  # None, PackBits, Jpeg, Deflate
	V.SaveWindowAtts.forceMerge = 0
	V.SaveWindowAtts.resConstraint = V.SaveWindowAtts.EqualWidthHeight  # NoConstraint, EqualWidthHeight, ScreenProportions
	V.SaveWindowAtts.advancedMultiWindowSave = 0
	V.SetSaveWindowAttributes(V.SaveWindowAtts)
	V.SaveWindow()

## Set View options
def View_parameter(Zoom, angle_theta, angle_phi):
	
	x = np.cos(angle_theta)*np.sin(angle_phi)
	y = np.sin(angle_theta)*np.sin(angle_phi)
	z = np.cos(angle_phi)

	V.ViewCurveAtts = V.ViewCurveAttributes()
	V.ViewCurveAtts.domainCoords = (0, 1)
	V.ViewCurveAtts.rangeCoords = (0, 1)
	V.ViewCurveAtts.viewportCoords = (0.2, 0.95, 0.15, 0.95)
	V.ViewCurveAtts.domainScale = V.ViewCurveAtts.LINEAR  # LINEAR, LOG
	V.ViewCurveAtts.rangeScale = V.ViewCurveAtts.LINEAR  # LINEAR, LOG
	V.SetViewCurve(V.ViewCurveAtts)
	V.View2DAtts = V.View2DAttributes()
	V.View2DAtts.windowCoords = (0, 1, 0, 1)
	V.View2DAtts.viewportCoords = (0.2, 0.95, 0.15, 0.95)
	V.View2DAtts.fullFrameActivationMode = V.View2DAtts.Auto  # On, Off, Auto
	V.View2DAtts.fullFrameAutoThreshold = 100
	V.View2DAtts.xScale = V.View2DAtts.LINEAR  # LINEAR, LOG
	V.View2DAtts.yScale = V.View2DAtts.LINEAR  # LINEAR, LOG
	V.View2DAtts.windowValid = 0
	V.SetView2D(V.View2DAtts)
	V.View3DAtts = V.View3DAttributes()
	V.View3DAtts.viewNormal = (0, 0, 1)
	V.View3DAtts.focus = (3.7632, 3.7632, 0)
	V.View3DAtts.viewUp = (x, y, z)
	V.View3DAtts.viewAngle = 30
	V.View3DAtts.parallelScale = 1059.07
	V.View3DAtts.nearPlane = -2118.14
	V.View3DAtts.farPlane = 2118.14
	V.View3DAtts.imagePan = (0, 0)
	V.View3DAtts.imageZoom = Zoom
	V.View3DAtts.perspective = 0
	V.View3DAtts.eyeAngle = 2
	V.View3DAtts.centerOfRotationSet = 0
	V.View3DAtts.centerOfRotation = (3.7632, 3.7632, 0)
	V.View3DAtts.axis3DScaleFlag = 0
	V.View3DAtts.axis3DScales = (1, 1, 1)
	V.View3DAtts.shear = (0, 0, 1)
	V.View3DAtts.windowValid = 1
	V.SetView3D(V.View3DAtts)
	V.ViewAxisArrayAtts = V.ViewAxisArrayAttributes()
	V.ViewAxisArrayAtts.domainCoords = (0, 1)
	V.ViewAxisArrayAtts.rangeCoords = (0, 1)
	V.ViewAxisArrayAtts.viewportCoords = (0.15, 0.9, 0.1, 0.85)
	V.SetViewAxisArray(V.ViewAxisArrayAtts)

def annotations():

	# Logging for SetAnnotationObjectOptions is not implemented yet.
	V.AnnotationAtts = V.AnnotationAttributes()
	V.AnnotationAtts.axes2D.visible = 0
	V.AnnotationAtts.axes2D.autoSetTicks = 1
	V.AnnotationAtts.axes2D.autoSetScaling = 1
	V.AnnotationAtts.axes2D.lineWidth = 0
	V.AnnotationAtts.axes2D.tickLocation = V.AnnotationAtts.axes2D.Outside  # Inside, Outside, Both
	V.AnnotationAtts.axes2D.tickAxes = V.AnnotationAtts.axes2D.BottomLeft  # Off, Bottom, Left, BottomLeft, All
	V.AnnotationAtts.axes2D.xAxis.title.visible = 1
	V.AnnotationAtts.axes2D.xAxis.title.font.font = V.AnnotationAtts.axes2D.xAxis.title.font.Courier  # Arial, Courier, Times
	V.AnnotationAtts.axes2D.xAxis.title.font.scale = 1
	V.AnnotationAtts.axes2D.xAxis.title.font.useForegroundColor = 1
	V.AnnotationAtts.axes2D.xAxis.title.font.color = (0, 0, 0, 255)
	V.AnnotationAtts.axes2D.xAxis.title.font.bold = 1
	V.AnnotationAtts.axes2D.xAxis.title.font.italic = 1
	V.AnnotationAtts.axes2D.xAxis.title.userTitle = 0
	V.AnnotationAtts.axes2D.xAxis.title.userUnits = 0
	V.AnnotationAtts.axes2D.xAxis.title.title = "X-Axis"
	V.AnnotationAtts.axes2D.xAxis.title.units = ""
	V.AnnotationAtts.axes2D.xAxis.label.visible = 1
	V.AnnotationAtts.axes2D.xAxis.label.font.font = V.AnnotationAtts.axes2D.xAxis.label.font.Courier  # Arial, Courier, Times
	V.AnnotationAtts.axes2D.xAxis.label.font.scale = 1
	V.AnnotationAtts.axes2D.xAxis.label.font.useForegroundColor = 1
	V.AnnotationAtts.axes2D.xAxis.label.font.color = (0, 0, 0, 255)
	V.AnnotationAtts.axes2D.xAxis.label.font.bold = 1
	V.AnnotationAtts.axes2D.xAxis.label.font.italic = 1
	V.AnnotationAtts.axes2D.xAxis.label.scaling = 0
	V.AnnotationAtts.axes2D.xAxis.tickMarks.visible = 1
	V.AnnotationAtts.axes2D.xAxis.tickMarks.majorMinimum = 0
	V.AnnotationAtts.axes2D.xAxis.tickMarks.majorMaximum = 1
	V.AnnotationAtts.axes2D.xAxis.tickMarks.minorSpacing = 0.02
	V.AnnotationAtts.axes2D.xAxis.tickMarks.majorSpacing = 0.2
	V.AnnotationAtts.axes2D.xAxis.grid = 0
	V.AnnotationAtts.axes2D.yAxis.title.visible = 1
	V.AnnotationAtts.axes2D.yAxis.title.font.font = V.AnnotationAtts.axes2D.yAxis.title.font.Courier  # Arial, Courier, Times
	V.AnnotationAtts.axes2D.yAxis.title.font.scale = 1
	V.AnnotationAtts.axes2D.yAxis.title.font.useForegroundColor = 1
	V.AnnotationAtts.axes2D.yAxis.title.font.color = (0, 0, 0, 255)
	V.AnnotationAtts.axes2D.yAxis.title.font.bold = 1
	V.AnnotationAtts.axes2D.yAxis.title.font.italic = 1
	V.AnnotationAtts.axes2D.yAxis.title.userTitle = 0
	V.AnnotationAtts.axes2D.yAxis.title.userUnits = 0
	V.AnnotationAtts.axes2D.yAxis.title.title = "Y-Axis"
	V.AnnotationAtts.axes2D.yAxis.title.units = ""
	V.AnnotationAtts.axes2D.yAxis.label.visible = 1
	V.AnnotationAtts.axes2D.yAxis.label.font.font = V.AnnotationAtts.axes2D.yAxis.label.font.Courier  # Arial, Courier, Times
	V.AnnotationAtts.axes2D.yAxis.label.font.scale = 1
	V.AnnotationAtts.axes2D.yAxis.label.font.useForegroundColor = 1
	V.AnnotationAtts.axes2D.yAxis.label.font.color = (0, 0, 0, 255)
	V.AnnotationAtts.axes2D.yAxis.label.font.bold = 1
	V.AnnotationAtts.axes2D.yAxis.label.font.italic = 1
	V.AnnotationAtts.axes2D.yAxis.label.scaling = 0
	V.AnnotationAtts.axes2D.yAxis.tickMarks.visible = 1
	V.AnnotationAtts.axes2D.yAxis.tickMarks.majorMinimum = 0
	V.AnnotationAtts.axes2D.yAxis.tickMarks.majorMaximum = 1
	V.AnnotationAtts.axes2D.yAxis.tickMarks.minorSpacing = 0.02
	V.AnnotationAtts.axes2D.yAxis.tickMarks.majorSpacing = 0.2
	V.AnnotationAtts.axes2D.yAxis.grid = 0
	V.AnnotationAtts.axes3D.visible = 0
	V.AnnotationAtts.axes3D.autoSetTicks = 1
	V.AnnotationAtts.axes3D.autoSetScaling = 1
	V.AnnotationAtts.axes3D.lineWidth = 0
	V.AnnotationAtts.axes3D.tickLocation = V.AnnotationAtts.axes3D.Inside  # Inside, Outside, Both
	V.AnnotationAtts.axes3D.axesType = V.AnnotationAtts.axes3D.ClosestTriad  # ClosestTriad, FurthestTriad, OutsideEdges, StaticTriad, StaticEdges
	V.AnnotationAtts.axes3D.triadFlag = 0
	V.AnnotationAtts.axes3D.bboxFlag = 1
	V.AnnotationAtts.axes3D.xAxis.title.visible = 1
	V.AnnotationAtts.axes3D.xAxis.title.font.font = V.AnnotationAtts.axes3D.xAxis.title.font.Arial  # Arial, Courier, Times
	V.AnnotationAtts.axes3D.xAxis.title.font.scale = 1
	V.AnnotationAtts.axes3D.xAxis.title.font.useForegroundColor = 1
	V.AnnotationAtts.axes3D.xAxis.title.font.color = (0, 0, 0, 255)
	V.AnnotationAtts.axes3D.xAxis.title.font.bold = 0
	V.AnnotationAtts.axes3D.xAxis.title.font.italic = 0
	V.AnnotationAtts.axes3D.xAxis.title.userTitle = 0
	V.AnnotationAtts.axes3D.xAxis.title.userUnits = 0
	V.AnnotationAtts.axes3D.xAxis.title.title = "X-Axis"
	V.AnnotationAtts.axes3D.xAxis.title.units = ""
	V.AnnotationAtts.axes3D.xAxis.label.visible = 1
	V.AnnotationAtts.axes3D.xAxis.label.font.font = V.AnnotationAtts.axes3D.xAxis.label.font.Arial  # Arial, Courier, Times
	V.AnnotationAtts.axes3D.xAxis.label.font.scale = 1
	V.AnnotationAtts.axes3D.xAxis.label.font.useForegroundColor = 1
	V.AnnotationAtts.axes3D.xAxis.label.font.color = (0, 0, 0, 255)
	V.AnnotationAtts.axes3D.xAxis.label.font.bold = 0
	V.AnnotationAtts.axes3D.xAxis.label.font.italic = 0
	V.AnnotationAtts.axes3D.xAxis.label.scaling = 0
	V.AnnotationAtts.axes3D.xAxis.tickMarks.visible = 1
	V.AnnotationAtts.axes3D.xAxis.tickMarks.majorMinimum = 0
	V.AnnotationAtts.axes3D.xAxis.tickMarks.majorMaximum = 1
	V.AnnotationAtts.axes3D.xAxis.tickMarks.minorSpacing = 0.02
	V.AnnotationAtts.axes3D.xAxis.tickMarks.majorSpacing = 0.2
	V.AnnotationAtts.axes3D.xAxis.grid = 0
	V.AnnotationAtts.axes3D.yAxis.title.visible = 1
	V.AnnotationAtts.axes3D.yAxis.title.font.font = V.AnnotationAtts.axes3D.yAxis.title.font.Arial  # Arial, Courier, Times
	V.AnnotationAtts.axes3D.yAxis.title.font.scale = 1
	V.AnnotationAtts.axes3D.yAxis.title.font.useForegroundColor = 1
	V.AnnotationAtts.axes3D.yAxis.title.font.color = (0, 0, 0, 255)
	V.AnnotationAtts.axes3D.yAxis.title.font.bold = 0
	V.AnnotationAtts.axes3D.yAxis.title.font.italic = 0
	V.AnnotationAtts.axes3D.yAxis.title.userTitle = 0
	V.AnnotationAtts.axes3D.yAxis.title.userUnits = 0
	V.AnnotationAtts.axes3D.yAxis.title.title = "Y-Axis"
	V.AnnotationAtts.axes3D.yAxis.title.units = ""
	V.AnnotationAtts.axes3D.yAxis.label.visible = 1
	V.AnnotationAtts.axes3D.yAxis.label.font.font = V.AnnotationAtts.axes3D.yAxis.label.font.Arial  # Arial, Courier, Times
	V.AnnotationAtts.axes3D.yAxis.label.font.scale = 1
	V.AnnotationAtts.axes3D.yAxis.label.font.useForegroundColor = 1
	V.AnnotationAtts.axes3D.yAxis.label.font.color = (0, 0, 0, 255)
	V.AnnotationAtts.axes3D.yAxis.label.font.bold = 0
	V.AnnotationAtts.axes3D.yAxis.label.font.italic = 0
	V.AnnotationAtts.axes3D.yAxis.label.scaling = 0
	V.AnnotationAtts.axes3D.yAxis.tickMarks.visible = 1
	V.AnnotationAtts.axes3D.yAxis.tickMarks.majorMinimum = 0
	V.AnnotationAtts.axes3D.yAxis.tickMarks.majorMaximum = 1
	V.AnnotationAtts.axes3D.yAxis.tickMarks.minorSpacing = 0.02
	V.AnnotationAtts.axes3D.yAxis.tickMarks.majorSpacing = 0.2
	V.AnnotationAtts.axes3D.yAxis.grid = 0
	V.AnnotationAtts.axes3D.zAxis.title.visible = 1
	V.AnnotationAtts.axes3D.zAxis.title.font.font = V.AnnotationAtts.axes3D.zAxis.title.font.Arial  # Arial, Courier, Times
	V.AnnotationAtts.axes3D.zAxis.title.font.scale = 1
	V.AnnotationAtts.axes3D.zAxis.title.font.useForegroundColor = 1
	V.AnnotationAtts.axes3D.zAxis.title.font.color = (0, 0, 0, 255)
	V.AnnotationAtts.axes3D.zAxis.title.font.bold = 0
	V.AnnotationAtts.axes3D.zAxis.title.font.italic = 0
	V.AnnotationAtts.axes3D.zAxis.title.userTitle = 0
	V.AnnotationAtts.axes3D.zAxis.title.userUnits = 0
	V.AnnotationAtts.axes3D.zAxis.title.title = "Z-Axis"
	V.AnnotationAtts.axes3D.zAxis.title.units = ""
	V.AnnotationAtts.axes3D.zAxis.label.visible = 1
	V.AnnotationAtts.axes3D.zAxis.label.font.font = V.AnnotationAtts.axes3D.zAxis.label.font.Arial  # Arial, Courier, Times
	V.AnnotationAtts.axes3D.zAxis.label.font.scale = 1
	V.AnnotationAtts.axes3D.zAxis.label.font.useForegroundColor = 1
	V.AnnotationAtts.axes3D.zAxis.label.font.color = (0, 0, 0, 255)
	V.AnnotationAtts.axes3D.zAxis.label.font.bold = 0
	V.AnnotationAtts.axes3D.zAxis.label.font.italic = 0
	V.AnnotationAtts.axes3D.zAxis.label.scaling = 0
	V.AnnotationAtts.axes3D.zAxis.tickMarks.visible = 1
	V.AnnotationAtts.axes3D.zAxis.tickMarks.majorMinimum = 0
	V.AnnotationAtts.axes3D.zAxis.tickMarks.majorMaximum = 1
	V.AnnotationAtts.axes3D.zAxis.tickMarks.minorSpacing = 0.02
	V.AnnotationAtts.axes3D.zAxis.tickMarks.majorSpacing = 0.2
	V.AnnotationAtts.axes3D.zAxis.grid = 0
	V.AnnotationAtts.axes3D.setBBoxLocation = 1
	V.AnnotationAtts.axes3D.bboxLocation = (-200, 200, -200, 200, 0, 0)
	V.AnnotationAtts.userInfoFlag = 0
	V.AnnotationAtts.userInfoFont.font = V.AnnotationAtts.userInfoFont.Arial  # Arial, Courier, Times
	V.AnnotationAtts.userInfoFont.scale = 1
	V.AnnotationAtts.userInfoFont.useForegroundColor = 1
	V.AnnotationAtts.userInfoFont.color = (0, 0, 0, 255)
	V.AnnotationAtts.userInfoFont.bold = 0
	V.AnnotationAtts.userInfoFont.italic = 0
	V.AnnotationAtts.databaseInfoFlag = 0
	V.AnnotationAtts.timeInfoFlag = 1
	V.AnnotationAtts.databaseInfoFont.font = V.AnnotationAtts.databaseInfoFont.Arial  # Arial, Courier, Times
	V.AnnotationAtts.databaseInfoFont.scale = 1
	V.AnnotationAtts.databaseInfoFont.useForegroundColor = 1
	V.AnnotationAtts.databaseInfoFont.color = (0, 0, 0, 255)
	V.AnnotationAtts.databaseInfoFont.bold = 0
	V.AnnotationAtts.databaseInfoFont.italic = 0
	V.AnnotationAtts.databaseInfoExpansionMode = V.AnnotationAtts.File  # File, Directory, Full, Smart, SmartDirectory
	V.AnnotationAtts.databaseInfoTimeScale = 1
	V.AnnotationAtts.databaseInfoTimeOffset = 0
	V.AnnotationAtts.legendInfoFlag = 0
	V.AnnotationAtts.backgroundColor = (255, 255, 255, 255)
	V.AnnotationAtts.foregroundColor = (0, 0, 0, 255)
	V.AnnotationAtts.gradientBackgroundStyle = V.AnnotationAtts.Radial  # TopToBottom, BottomToTop, LeftToRight, RightToLeft, Radial
	V.AnnotationAtts.gradientColor1 = (0, 0, 255, 255)
	V.AnnotationAtts.gradientColor2 = (0, 0, 0, 255)
	V.AnnotationAtts.backgroundMode = V.AnnotationAtts.Solid  # Solid, Gradient, Image, ImageSphere
	V.AnnotationAtts.backgroundImage = ""
	V.AnnotationAtts.imageRepeatX = 1
	V.AnnotationAtts.imageRepeatY = 1
	V.AnnotationAtts.axesArray.visible = 1
	V.AnnotationAtts.axesArray.ticksVisible = 1
	V.AnnotationAtts.axesArray.autoSetTicks = 1
	V.AnnotationAtts.axesArray.autoSetScaling = 1
	V.AnnotationAtts.axesArray.lineWidth = 0
	V.AnnotationAtts.axesArray.axes.title.visible = 1
	V.AnnotationAtts.axesArray.axes.title.font.font = V.AnnotationAtts.axesArray.axes.title.font.Arial  # Arial, Courier, Times
	V.AnnotationAtts.axesArray.axes.title.font.scale = 1
	V.AnnotationAtts.axesArray.axes.title.font.useForegroundColor = 1
	V.AnnotationAtts.axesArray.axes.title.font.color = (0, 0, 0, 255)
	V.AnnotationAtts.axesArray.axes.title.font.bold = 0
	V.AnnotationAtts.axesArray.axes.title.font.italic = 0
	V.AnnotationAtts.axesArray.axes.title.userTitle = 0
	V.AnnotationAtts.axesArray.axes.title.userUnits = 0
	V.AnnotationAtts.axesArray.axes.title.title = ""
	V.AnnotationAtts.axesArray.axes.title.units = ""
	V.AnnotationAtts.axesArray.axes.label.visible = 1
	V.AnnotationAtts.axesArray.axes.label.font.font = V.AnnotationAtts.axesArray.axes.label.font.Arial  # Arial, Courier, Times
	V.AnnotationAtts.axesArray.axes.label.font.scale = 1
	V.AnnotationAtts.axesArray.axes.label.font.useForegroundColor = 1
	V.AnnotationAtts.axesArray.axes.label.font.color = (0, 0, 0, 255)
	V.AnnotationAtts.axesArray.axes.label.font.bold = 0
	V.AnnotationAtts.axesArray.axes.label.font.italic = 0
	V.AnnotationAtts.axesArray.axes.label.scaling = 0
	V.AnnotationAtts.axesArray.axes.tickMarks.visible = 1
	V.AnnotationAtts.axesArray.axes.tickMarks.majorMinimum = 0
	V.AnnotationAtts.axesArray.axes.tickMarks.majorMaximum = 1
	V.AnnotationAtts.axesArray.axes.tickMarks.minorSpacing = 0.02
	V.AnnotationAtts.axesArray.axes.tickMarks.majorSpacing = 0.2
	V.AnnotationAtts.axesArray.axes.grid = 0
	V.SetAnnotationAttributes(V.AnnotationAtts)




for Seed_index in range(20):
	
	zoom_idx = (Seed_index)/5.0 + 1.0
	angle_theta = (np.pi/2)*(1.0 + Seed_index/40.0)
	angle_phi = np.pi/2	
	
	Seed_list = Seed[:, Seed_index]
	Seed_list = tuple(Seed_list)
	View_parameter(zoom_idx, angle_theta, angle_phi )
	Generate_streamlines(Seed_index, Seed_list)
	annotations()
	Save_Plots()
	V.DeleteActivePlots()


