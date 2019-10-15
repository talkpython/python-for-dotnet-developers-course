using System;
using System.Text;

namespace Ch3_Lang
{
    class FunctionArgs
    {
        public static void Run()
        {
            Console.WriteLine("SayHello()");
            SayHello();
            Console.WriteLine();

            Console.WriteLine("SayHello(name)");
            SayHello("Zoe");
            Console.WriteLine();

            Console.WriteLine("SayHello(name, times)");
            SayHello("Zoe", 5);
            Console.WriteLine();

            Console.WriteLine("SayHello(name, times, 1, 2, 3)");
            SayHello("Zoe", 5, 1, 2, 3, 4);
            Console.WriteLine();

            Console.WriteLine("SayHello(int)");
            SayHello(7);
            Console.WriteLine();

            Console.WriteLine("SayHello(double)");
            SayHello(5.0);
            Console.WriteLine();
        }
        public static void SayHello(string name, int times = 1, params object[] extras)
        {
            Console.WriteLine($"Hello there {name}, times={times}, extras={PrintArray(extras)}!");
        }

        public static void SayHello()
        {
            SayHello("friend");
        }

        public static void SayHello(int times)
        {
            for (int i = 0; i < times; i++)
            {
                Console.WriteLine("Hello there!");
            }
        }

        public static void SayHello(double times)
        {
            for (int i = 0; i < times; i++)
            {
                Console.WriteLine("Hello there double time!");
            }
        }

        private static string PrintArray(object[] ar)
        {
            var sb = new StringBuilder("[");
            foreach (var o in ar)
            {
                sb.Append("\"");
                sb.Append(o);
                sb.Append("\", ");
            }

            sb.Append("]");

            return sb.ToString();
        }
    }
}
