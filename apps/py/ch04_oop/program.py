from pprint import pprint
from typing import List

from models.basic_car import BasicCar
from models.car import Car
from models.electric_car import ElectricCar
from models.parking_lot import ParkingLot
from models.sports_car import SportsCar


def main():
    cars = create_cars()
    use_cars(cars)
    park_cars(cars)


def park_cars(cars: List[Car]):
    lot = ParkingLot.create(5, 3)

    for c in cars:
        lot.park(c)

    # pprint(lot.spots)


def use_cars(cars):
    for car in cars:
        print(f"{car.model_name} is electric? {car.is_electric}")
        car.drive()
        car.refuel()
        print()


def create_cars() -> List[Car]:
    return [
        SportsCar('Corvette', 'gas', 8, 50_000),
        SportsCar('Camaro', 'gas', 8, 40_000),
        BasicCar('Windstar', 'gas', 6, 20_000),
        ElectricCar('Tesla', 60_000),
        ElectricCar('Bolt', 40_000),
        ElectricCar('Leaf', 30_000),
    ]


if __name__ == '__main__':
    main()
