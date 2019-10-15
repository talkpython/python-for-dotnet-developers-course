using System;
using System.Collections.Generic;
using System.Text;

namespace Ch3_Lang
{
    class Generators
    {
        public static void Run()
        {
            Console.WriteLine("Generators");

            foreach (int n in Fibonacci())
            {
                if (n > 1000)
                {
                    break;
                }

                Console.Write(n);
                Console.Write(", ");
            }
            Console.WriteLine();
        }

        public static IEnumerable<int> Fibonacci()
        {
            int current = 0;
            int next = 1;

            while (true)
            {
                int temp = current;
                current = next;
                next = temp + next;

                yield return current;
            }
            // ReSharper disable once IteratorNeverReturns
        }

        public static IEnumerable<int> Fibonacci(int count)
        {
            List<int> nums = new List<int>();
            int current = 0;
            int next = 1;

            for (int i = 0; i < count; i++)
            {
                int temp = current;
                current = next;
                next = temp + next;

                nums.Add(current);
            }

            return nums;
        }
    }
}
