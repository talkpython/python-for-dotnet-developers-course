from models.car import Car


class ElectricCar(Car):

    def __init__(self, model_name: str, base_price: float):
        # first!
        super().__init__(model_name, 'electric', 0, base_price)
        # then other stuff..

    def drive(self):
        print(f"ElectricCar: The electric {self.model_name} zooms silently along!")

    def refuel(self):
        print(f'ElectricCar: The {self.model_name} is charging up.')
