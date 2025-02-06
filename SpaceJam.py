from direct.showbase.ShowBase import ShowBase

class MyApp(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)
        self.SetupScene()
        

    def SetupScene(self):
      texUni = self.loader.loadTexture("./Assets/Universe/universebackdrop.jpg")
      texEarth = self.loader.loadTexture("./Assets/Planets/earth.jpg")
      texMars = self.loader.loadTexture("./Assets/Planets/mars.jpg")
      texJupiter = self.loader.loadTexture("./Assets/Planets/jupiter.jpg")
      texSaturn = self.loader.loadTexture("./Assets/Planets/saturn.jpg")
      texVenus = self.loader.loadTexture("./Assets/Planets/venus.jpg")
      texUranus = self.loader.loadTexture("./Assets/Planets/uranus.jpg")
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

      self.Planet3 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
      self.Planet3.reparentTo(self.render)
      self.Planet3.setPos(-850, 5000, 67)
      self.Planet3.setScale(500)
      self.Planet3.setTexture(texJupiter, 1)

      self.Planet4 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
      self.Planet4.reparentTo(self.render)
      self.Planet4.setPos(1750, 5000, 67)
      self.Planet4.setScale(400)
      self.Planet4.setTexture(texSaturn, 1)

      self.Planet5 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
      self.Planet5.reparentTo(self.render)
      self.Planet5.setPos(2700, 5000, 67)
      self.Planet5.setScale(350)
      self.Planet5.setTexture(texVenus, 1)

      self.Planet6 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
      self.Planet6.reparentTo(self.render)
      self.Planet6.setPos(-1800, 5000, 67)
      self.Planet6.setScale(250)
      self.Planet6.setTexture(texUranus, 1)

      self.Spaceship = self.loader.loadModel("./Assets/Spaceships/Dumbledore.x")
      self.Spaceship.reparentTo(self.render)
      self.Spaceship.setPos(150, 6000, 1500)
      self.Spaceship.setScale(200)
      self.Spaceship.setTexture(texShip, 1)

      self.Station = self.loader.loadModel("./Assets/SpaceStation/spaceStation.x")
      self.Station.reparentTo(self.render)
      self.Station.setPos(150, 8000, 3000)
      self.Station.setScale(50)
      self.Station.setTexture(texStation, 1)

app = MyApp()
app.run()