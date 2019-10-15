using System;
using System.Collections.Generic;
using System.IO;
using System.Text;
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
        }
    }
}
