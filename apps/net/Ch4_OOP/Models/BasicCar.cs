using System;
namespace Ch4_OOP.Models
{
    public class BasicCar : Car
    {
        public BasicCar(string modeName, string engineType, int cylinders, float basePrice) :
            base(modeName, engineType, cylinders, basePrice)
        {
        }

        public override void Refuel()
        {
            Console.WriteLine("BasicCar: Basic cars takes any old fuel.");
        }
    }
}
