using System;
namespace Ch4_OOP.Models
{
    public abstract class Car
    {
        public string ModelName { get; }
        public string EngineType { get; }
        public int Cylinders { get; }
        public float BasePrice { get; }

        public Car(string modelName, string engineType, int cylinders, float basePrice)
        {
            ModelName = modelName;
            EngineType = engineType;
            Cylinders = cylinders;
            BasePrice = basePrice;
        }

        public bool IsElectric
        {
            get
            {
                return EngineType == "electric";
            }
        }

        public virtual void Drive()
        {
            Console.WriteLine($"Car: The {ModelName} goes vroom!");
        }

        public abstract void Refuel();
    }
}
