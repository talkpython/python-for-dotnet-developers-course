using System.Diagnostics;
using System.Linq;

namespace Ch7_Db.Data
{
    public static class DataLoader
    {
        public static void LoadIfNeeded()
        {
            var db = new AppDbContext();
            db.Database.EnsureCreated();

            using (db)
            {
                Debug.WriteLine(db.Database.CanConnect());
                if (db.Guitars.Any())
                {
                    Debug.WriteLine("Skipping data load, already has guitars loaded.");
                    return;
                }

                Debug.WriteLine("No data found. Loading new guitars...");

                var guitars =
                new[] {
                    new Guitar("AX Black", 499, "/img/guitars/ax-black.jpg", "electric"),
                    new Guitar("Jet Black Electric", 599, "/img/guitars/jet-black-electric.jpg",  "electric"),
                    new Guitar("Weezer Classic", 1499, "/img/guitars/weezer-classic.jpg",  "electric"),
                    new Guitar("Acoustic Black", 1299, "/img/guitars/black-acoustic.jpg",  "acoustic"),
                    new Guitar("Mellow Yellow", 799, "/img/guitars/mellow-yellow.jpg",  "electric"),
                    new Guitar("White Vibes", 699, "/img/guitars/white-vibes.jpg",  "electric"),
                    new Guitar("Brush Riffs", 599, "/img/guitars/brushed-black-electric.jpg",  "electric"),
                    new Guitar("Nature''s Song", 799, "/img/guitars/natures-song.jpg", "electric"),
                    new Guitar("Electric Wood Grain", 399, "/img/guitars/woodgrain-electric.jpg", "electric"),
                };

                foreach (var g in guitars)
                {
                    db.Guitars.Add(g);
                }
                db.SaveChanges();
            }

        }
    }
}
