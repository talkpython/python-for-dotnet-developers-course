using System;

namespace Ch3_Lang
{
    class Switch
    {
        public static void Run()
        {
            while (true)
            {
                Console.Write("Enter a number 1 -> 4, (blank to exit): ");
                var text = Console.ReadLine();
                if (text == null || text.Trim().Length == 0)
                {
                    Console.WriteLine("Later...");
                    break;
                }

                var num = int.Parse(text);
                switch (num)
                {
                    case 1:
                        Console.WriteLine("One is fun!");
                        break;
                    case 2:
                        Console.WriteLine("2 * 2 = 4");
                        break;
                    case 3:
                        Console.WriteLine("Three and free.");
                        break;
                    case 4:
                        Console.WriteLine("4 more!");
                        break;
                    default:
                        Console.WriteLine($"Say what: {num}?");
                        break;
                }
            }
        }
    }
}
