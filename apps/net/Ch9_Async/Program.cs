using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Net;
using System.Net.Http;
using System.Threading.Tasks;
using HtmlAgilityPack;

namespace Ch9_Async
{
    class MainClass
    {
        public static void Main()
        {
            Console.ForegroundColor = ConsoleColor.White;
            Console.WriteLine("C# Concurrent Web Scraper.");
            var sw = Stopwatch.StartNew();

            GetTitleRange().Wait();

            Console.WriteLine($"Done in {sw.ElapsedMilliseconds/1000.0} sec.");
        }

        public async static Task GetTitleRange()
        {
            var tasks = new List<Tuple<int, Task<string>>>();

            // Please keep this range pretty small to not DDoS my site. ;)
            for (int i = 220; i < 231; i++)
            {
                var task = GetEpisodeHtml(i);
                var item = new Tuple<int, Task<string>>(i, task);
                tasks.Add(item);
            }

            foreach (Tuple<int, Task<string>> item in tasks)
            {
                var episodeNumber = item.Item1;
                var task = item.Item2;
                string html = await task;
                string title = GetTitle(html);

                Console.ForegroundColor = ConsoleColor.Cyan;
                Console.WriteLine($"Found title for #{episodeNumber}: {title}");
            }

            Console.ForegroundColor = ConsoleColor.White;
        }

        public async static Task<string> GetEpisodeHtml(int episodeNumber, string url = null)
        {
            if (string.IsNullOrEmpty(url))
            {
                Console.ForegroundColor = ConsoleColor.Yellow;
                Console.WriteLine($"Getting HTML for episode {episodeNumber}");
            }

            if (url == null)
                url = $"https://talkpython.fm/{episodeNumber}";

            HttpClient client = new HttpClient();

            HttpResponseMessage response = await client.GetAsync(url);
            if (response.StatusCode == HttpStatusCode.Moved || response.StatusCode == HttpStatusCode.MovedPermanently)
            {
                url = response.Headers.Location.ToString();
                return await GetEpisodeHtml(episodeNumber, url);
            }

            if (!response.IsSuccessStatusCode)
            {
                throw new Exception($"Invalid request, got code {response.StatusCode}");
            }

            string html = await response.Content.ReadAsStringAsync();
            return html;
        }

        public static string GetTitle(string html)
        {
            HtmlDocument page = new HtmlDocument();
            page.LoadHtml(html);
            HtmlNode h1 = page.DocumentNode.SelectSingleNode("//h1");

            return h1.InnerText.Trim();
        }
    }
}
