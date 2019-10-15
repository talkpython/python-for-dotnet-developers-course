using System;
using Ch8_Testing;

namespace Ch8_Testing_App
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Welcome to the guitar app!");
            var lib = new Lib();
            while (true)
            {
                Console.Write("What style of guitar do you want to see? ");
                string style = Console.ReadLine();
                if (string.IsNullOrWhiteSpace(style))
                {
                    Console.WriteLine("Bye!");
                    break;
                }
                Guitar[] guitars = lib.AllGuitars(style);

                Console.WriteLine($"We found {guitars.Length} guitars of type {style}");
                int idx = 0;
                foreach (var g in guitars)
                {
                    idx++;
                    Console.WriteLine($"{idx}. {g.Name} for ${g.Price} ({g.Style})");
                }

            }
            
        }
    }
}
