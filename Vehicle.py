class Vehicle:
    def __init__(self,regNo, color):
        self.color = color
        self.regNo = regNo
      #  self.vehicleType = vehicleType

class TwoWheeler(Vehicle):
    def __init__(self, regNo, color):
        Vehicle.__init__(self,regNo, color)

    def getType(self):
        return "TwoWheeler"

class HatchBack(Vehicle):
    def __init__(self, regNo, color):
        Vehicle.__init__(self,regNo, color)

    def getType(self):
        return "HatchBack"

class SuvCar(Vehicle):
    def __init__(self, regNo, color):
        Vehicle.__init__(self,regNo, color)

    def getType(self):
        return "SuvCar"
