from models.car import Car


class BasicCar(Car):
    def refuel(self):
        print("BasicCar: Basic cars take any old gas.")
