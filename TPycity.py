import vtk

# create a rendering window and renderer
ren = vtk.vtkRenderer()
renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren)

# create a renderwindowinteractor
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)

# create source
cube=vtk.vtkCubeSource()
cube.SetXLength(60)
cube.SetYLength(7)
cube.SetZLength(50)

cube2=vtk.vtkCubeSource()
cube2.SetXLength(20)
cube2.SetYLength(35)
cube2.SetZLength(10)

cube3=vtk.vtkCubeSource()
cube3.SetXLength(20)
cube3.SetYLength(25)
cube3.SetZLength(15)

cube4=vtk.vtkCubeSource()
cube4.SetXLength(5)
cube4.SetYLength(10)
cube4.SetZLength(8)


cube5=vtk.vtkCubeSource()
cube5.SetXLength(5)
cube5.SetYLength(10)
cube5.SetZLength(8)


cube6=vtk.vtkCubeSource()
cube6.SetXLength(5)
cube6.SetYLength(10)
cube6.SetZLength(8)


cube7=vtk.vtkCubeSource()
cube7.SetXLength(15)
cube7.SetYLength(30)
cube7.SetZLength(8)

# mapper

cubeMapper = vtk.vtkPolyDataMapper()
cubeMapper.SetInputConnection(cube.GetOutputPort())

cube2Mapper = vtk.vtkPolyDataMapper()
cube2Mapper.SetInputConnection(cube2.GetOutputPort())

cube3Mapper = vtk.vtkPolyDataMapper()
cube3Mapper.SetInputConnection(cube3.GetOutputPort())

cube4Mapper = vtk.vtkPolyDataMapper()
cube4Mapper.SetInputConnection(cube4.GetOutputPort())

cube5Mapper = vtk.vtkPolyDataMapper()
cube5Mapper.SetInputConnection(cube5.GetOutputPort())

cube6Mapper = vtk.vtkPolyDataMapper()
cube6Mapper.SetInputConnection(cube6.GetOutputPort())


cube7Mapper = vtk.vtkPolyDataMapper()
cube7Mapper.SetInputConnection(cube7.GetOutputPort())

# actor

cubeActor = vtk.vtkActor()
cubeActor.SetMapper(cubeMapper)
cubeActor.SetPosition(-2,0,0)

cubeActor2 = vtk.vtkActor()
cubeActor2.SetMapper(cube2Mapper)
cubeActor2.GetProperty().SetColor(0.5,1,0.5)
cubeActor2.SetPosition(16,22,0)

cubeActor3 = vtk.vtkActor()
cubeActor3.SetMapper(cube3Mapper)
cubeActor3.GetProperty().SetColor(0.5,1,0.5)
cubeActor3.SetPosition(-20,15,0)

cubeActor4 = vtk.vtkActor()
cubeActor4.SetMapper(cube4Mapper)
cubeActor4.GetProperty().SetColor(0,0,255)
cubeActor4.SetPosition(20,40,0)

cubeActor5 = vtk.vtkActor()
cubeActor5.SetMapper(cube5Mapper)
cubeActor5.GetProperty().SetColor(255,0,0)
cubeActor5.SetPosition(-20,30,0)

cubeActor6 = vtk.vtkActor()
cubeActor6.SetMapper(cube6Mapper)
cubeActor6.GetProperty().SetColor(255,255,0)
cubeActor6.SetPosition(-30,9,20)

cubeActor7 = vtk.vtkActor()
cubeActor7.SetMapper(cube7Mapper)
cubeActor7.GetProperty().SetColor(64,128,128)
cubeActor7.SetPosition(20,19,-20)

# assign actor to the renderer
ren.AddActor(cubeActor)
ren.AddActor(cubeActor2)
ren.AddActor(cubeActor3)
ren.AddActor(cubeActor4)
ren.AddActor(cubeActor5)
ren.AddActor(cubeActor6)
ren.AddActor(cubeActor7)

# enable user interface interactor
iren.Initialize()
renWin.Render()
renWin.SetSize(1300, 680)
ren.SetBackground(0,0,0)
iren.Start()


