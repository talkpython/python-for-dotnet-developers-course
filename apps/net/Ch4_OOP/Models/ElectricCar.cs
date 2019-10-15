using System;
namespace Ch4_OOP.Models
{
    public class ElectricCar : Car
    {
        public ElectricCar(string modeName, float basePrice) :
            base(modeName, "electric", 0, basePrice)
        {
        }

        public override void Refuel()
        {
            Console.WriteLine($"ElectricCar: The {ModelName} is charging up.");
        }

        public override void Drive()
        {
            Console.WriteLine($"ElectricCar: The electric {ModelName} zooms silently along!");
        }
    }
}
