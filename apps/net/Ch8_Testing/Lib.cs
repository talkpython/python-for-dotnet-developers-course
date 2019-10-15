using System;
using System.Linq;

namespace Ch8_Testing
{
    public class Lib
    {
        private readonly IDb db;
        private readonly ILogger log;

        public Lib(IDb db = null, ILogger log = null)
        {
            if (db == null) db = new Db();
            if (log == null) log = new Logger();

            this.db = db;
            this.log = log;
        }

        public Guitar[] AllGuitars(string style)
        {
            log.Log($"Guitars for {style}...");

            if (string.IsNullOrEmpty(style))
            {
                throw new ArgumentException("Style cannot be empty.");
            }

            var guitars = db.GetGuitarsFromDb();
            if (style == "all")
                return guitars;

            return (from g in guitars
                    where g.Style == style
                    select g
                    ).ToArray();
        }
    }
}
