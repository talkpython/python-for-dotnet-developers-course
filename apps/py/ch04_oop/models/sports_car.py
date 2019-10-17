from models.car import Car


class SportsCar(Car):

    def drive(self):
        print(f"SportsCar: The {self.model_name} tears along the highway!")

    def refuel(self):
        print(f"SportsCar: The {self.model_name} only wants the best gas.")
