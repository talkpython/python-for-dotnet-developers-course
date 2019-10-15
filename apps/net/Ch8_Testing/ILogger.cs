using System;
namespace Ch8_Testing
{
    public interface ILogger
    {
        void Log(string message);
    }

    public class Logger : ILogger
    {
        public void Log(string message)
        {
            Console.ForegroundColor = ConsoleColor.Yellow;
            Console.Write("      --> LOGGING THIS TO A FILE, SHOULD NOT SEE IN TEST: ");
            Console.ForegroundColor = ConsoleColor.White;
            Console.WriteLine(message);
        }
    }
}
