from typing import List

from models.basic_car import BasicCar
from models.car import Car
from models.electric_car import ElectricCar
from models.sports_car import SportsCar


def main():
    cars = create_cars()
    for car in cars:
        print(f"{car.model_name} is electric? {car.is_electric}")
        car.drive()
        car.refuel()
        print()


def create_cars() -> List[Car]:
    return [
        SportsCar('Corvette', 'gas', 8, 50_000),
        BasicCar('Windstar', 'gas', 6, 20_000),
        ElectricCar('Tesla', 60_000),
        ElectricCar('Bolt', 40_000),
    ]


if __name__ == '__main__':
    main()
