using System;

namespace Ch3_Lang
{
    class Closuers
    {
        public static void Run()
        {
            var counter1 = CreateCounter(7);
            var counter2 = CreateCounter(-100);
            counter1();
            counter2();

            counter1();
            counter2();

            counter1();
            counter2();
        }

        public delegate void CounterMethod();

        public static CounterMethod CreateCounter(int starterVal)
        {
            var start = starterVal;
            Console.WriteLine($"Creating a counter with start value {starterVal}...");

            CounterMethod counter = delegate ()
            {
                start++;
                Console.WriteLine($"Counting {starterVal}\t-->\t{start}.");
            };

            return counter;
        }
    }
}
