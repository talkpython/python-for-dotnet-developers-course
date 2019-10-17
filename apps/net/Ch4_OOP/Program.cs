using System;
using Ch4_OOP.Models;

namespace Ch4_OOP
{
    class Program
    {
        static void Main()
        {
            Console.WriteLine("Hello C# Cars!");

            Car[] cars = CreateCars();
            foreach (var car in cars)
            {
                car.Drive();
                car.Refuel();
                Console.WriteLine();
            }

            var lot = ParkingLot.Create(5, 3);
            Console.WriteLine("Free spots");
            foreach (var spot in lot)
            {
                Console.Write($"{spot}, ");
            }

            Console.WriteLine();
            foreach (var car in cars)
            {
                lot.ParkCar(car);
            }
            Console.WriteLine("Taken spots");
            foreach (var spot in lot.TakenSpots())
            {
                Console.Write($"{spot}, ");
            }
            Console.WriteLine();
        }

        static Car[] CreateCars()
        {
            return new Car[]
            {
                new SportsCar("Corvette", "gas", 8, 50_000),
                new BasicCar("Windstar", "gas", 6, 20_000),
                new ElectricCar("Tesla", 60_000),
                new ElectricCar("Bolt", 40_000),
            };
        }
    }
}
