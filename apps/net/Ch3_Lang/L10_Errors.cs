using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Net.Sockets;

namespace Ch3_Lang
{
    class Errors
    {
        public static void Run()
        {
            var values = new List<int>();
            for (int i = 0; i < 20; i++)
            {
                values.Add(i + 1);
            }
            values.AddRange(new int[] { 0, 1, 1, 2, 3, 5, 8 });

            foreach (var v in values)
            {
                try
                {
                    Console.ForegroundColor = ConsoleColor.Gray;
                    Console.WriteLine($"Calling sketchy_method with {v}...");
                    Console.ForegroundColor = ConsoleColor.Yellow;
                    SketchyMethod(v);
                }
                catch (SocketException)
                {
                    Console.ForegroundColor = ConsoleColor.Cyan;
                    Console.WriteLine($" ****  Network error, check your network connection.");
                }
                catch (ValidationException)
                {
                    Console.ForegroundColor = ConsoleColor.Cyan;
                    Console.WriteLine($" ****  We cannot compute with that value.");
                }
                catch (Exception e)
                {
                    Console.ForegroundColor = ConsoleColor.Cyan;
                    Console.WriteLine($" **** Error: {e.GetType().Name} --> {e.Message}");
                }
            }

            Console.ForegroundColor = ConsoleColor.White;
        }


        public static void SketchyMethod(int value)
        {
            var r = new Random();

            if (value == 0)
                throw new ValidationException($"{value} is not valid.");
            else if (value % 6 == 0)
                throw new ArithmeticException();
            else if (r.Next(1, 10) == 3)
                throw new SocketException(-7);

            Console.WriteLine("SketchyMethod() actually worked!");
        }
    }
}
