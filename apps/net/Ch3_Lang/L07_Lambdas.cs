using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Ch3_Lang
{
    class Lambdas
    {
        public static void Run()
        {
            var data = new List<int> { 55, 987, 89, -233, 8, 13, -377, 3, 1, -34, 610, 144, 5, 21, 2, 1 };
            data.Sort((n, m) => Math.Abs(n) - Math.Abs(m));
            Console.WriteLine(PrintCollection(data));

            Console.WriteLine(PrintCollection(data.Select(n => 2 * n)));
        }

        private static string PrintCollection<T>(IEnumerable<T> ar)
        {
            var sb = new StringBuilder("[");
            foreach (var o in ar)
            {
                sb.Append(o);
                sb.Append(", ");
            }

            sb.Append("]");

            return sb.ToString().Replace(", ]", "]");
        }
    }
}
