using System;

namespace Ch3_Lang
{
    class Iteration
    {
        public static void Run()
        {
            // WHILE
            string name = "EMPTY";
            while (name?.Length > 0)
            {
                Console.Write("What is your name? ");
                name = Console.ReadLine();
                Console.WriteLine($"Nice to meet you {name}!");
            }

            // foreach
            int[] nums = { 1, 5, 8, 10, 7, 2 };
            foreach (int n in nums)
            {
                Console.WriteLine($"The next number is {n}.");
            }

            // for
            for (int idx = 0; idx < nums.Length; idx++)
            {
                int n = nums[idx];
                Console.WriteLine($"The {idx + 1}th number is {n}.");
            }
        }
    }
}
