using System.Linq;
using Ch7_Db.Data;

namespace Ch7_Db.Services
{
    public static class CatalogService
    {
        public static Guitar[] AllGuitars(string style = null)
        {
            using (var db = new AppDbContext())
            {
                if (style == null || style == "all")
                {
                    return db.Guitars.OrderByDescending(g => g.Price).ToArray();
                }

                return (from g in db.Guitars
                        where g.Style == style
                        orderby g.Price descending
                        select g
                    ).ToArray();

            }
        }
    }
}
