using System;


namespace Ch3_Lang
{
    class FunctionBasics
    {
        public static void Run()
        {
            ShowHeader();

            Random rand = new Random();
            int theNumber = rand.Next(1, 100);
            int count = 0;

            while (true)
            {
                int? guess = GetGuess();
                if (guess == null)
                {
                    continue;
                }

                count++;
                if (EvaluateGuess(guess.Value, theNumber))
                {
                    break;
                }
            }

            Console.WriteLine($"You got the number in {count} attempts. Thanks for playing, bye.");
        }

        private static void ShowHeader()
        {
            Console.WriteLine("-------------------------------------------");
            Console.WriteLine("|                                         |");
            Console.WriteLine("|           C# HIGH / LOW GAME            |");
            Console.WriteLine("|                                         |");
            Console.WriteLine("-------------------------------------------");
            Console.WriteLine();
            Console.WriteLine("I'm thinking of a number between 1 & 100.");
            Console.WriteLine("How many steps can you guess it in?");
            Console.WriteLine();
        }

        private static int? GetGuess()
        {
            Console.Write("What number am I thinking of? ");
            string text = Console.ReadLine();
            if (!int.TryParse(text, out int val))
            {
                Console.WriteLine("That's not a number!");
                return null;
            }

            if (val < 1 || 100 < val)
            {
                Console.WriteLine($"{val} is not between 1 & 100.");
                return null;
            }

            return val;
        }


        private static bool EvaluateGuess(int guess, int number)
        {
            if (guess == number)
            {
                Console.WriteLine($"That's it! I was thinking of {number}.");
            }
            else if (guess < number)
            {
                Console.WriteLine("That's too LOW");
            }
            else
            {
                Console.WriteLine("That's too HIGH");
            }

            return guess == number;
        }
    }
}
