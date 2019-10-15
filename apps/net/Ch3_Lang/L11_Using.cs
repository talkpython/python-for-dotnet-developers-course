using System.Collections.Generic;
using System.IO;
using Newtonsoft.Json;

namespace Ch3_Lang
{
    class Using
    {
        public static void Run()
        {
            var data = new Dictionary<string, string>();
            data.Add("Name", "Michael");
            data.Add("Language", "C#");

            using (StreamWriter file = File.CreateText(@"file.json"))
            {
                JsonSerializer serializer = new JsonSerializer();
                serializer.Serialize(file, data);
            }

            System.Console.WriteLine($"Created file.json in working directory.");
        }
    }
}
