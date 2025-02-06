from direct.showbase.ShowBase import ShowBase

class MyApp(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)
        self.SetupScene()
        

    def SetupScene(self):
      texUni = self.loader.loadTexture("./Assets/Universe/Universe.jpg")
      texEarth = self.loader.loadTexture("./Assets/Planets/earth.png")
      texMars = self.loader.loadTexture("./Assets/Planets/mars.png")
      texJupiter = self.loader.loadTexture("./Assets/Planets/jupiter.png")
      texSaturn = self.loader.loadTexture("./Assets/Planets/saturn.png")
      texVenus = self.loader.loadTexture("./Assets/Planets/venus.png")
      texUranus = self.loader.loadTexture("./Assets/Planets/uranus.png")
      texShip = self.loader.loadTexture("./Assets/Spaceships/spacejet_C.png")
      texStation = self.loader.loadTexture("./Assets/SpaceStation/SpaceStation1_Dif2.png")

      self.Universe = self.loader.loadModel("./Assets/Universe/Universe.x")
      self.Universe.reparentTo(self.render)
      self.Universe.setScale(15000)
      self.Universe.setTexture(texUni, 1)

      self.Planet1 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
      self.Planet1.reparentTo(self.render)
      self.Planet1.setPos(150, 5000, 67)
      self.Planet1.setScale(350)
      self.Planet1.setTexture(texEarth, 1)

      self.Planet2 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
      self.Planet2.reparentTo(self.render)
      self.Planet2.setPos(900, 5000, 67)
      self.Planet2.setScale(250)
      self.Planet2.setTexture(texMars, 1)

app = MyApp()
app.run()