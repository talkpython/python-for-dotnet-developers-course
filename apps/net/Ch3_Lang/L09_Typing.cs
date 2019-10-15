using System;

namespace Ch3_Lang
{
    class Wizard
    {
        public string Name { get; set; }
        public int Level { get; set; }

        public static Wizard Train(int baseLevel)
        {
            Wizard w = new Wizard();
            w.Level = baseLevel;

            return w;
        }
    }

    class Typing
    {
        public static void Run()
        {
            Wizard gandolf = Wizard.Train(7);
            gandolf.Level++;

            Console.WriteLine($"The level of the wizard is {gandolf.Level}");
        }
    }
}
