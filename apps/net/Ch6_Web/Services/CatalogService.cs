using System.Linq;
using Ch6_Web.Data;

namespace Ch6_Web.Services
{
    public static class CatalogService
    {
        public static Guitar[] AllGuitars(string style = null)
        {
            var guitars =
                new[] {
                    new Guitar("AX Black", 499, "/img/guitars/ax-black.jpg", "electric"),
                    new Guitar("Acoustic Black", 299, "/img/guitars/black-acoustic.jpg",  "acoustic"),
                    new Guitar("Weezer Classic", 1499, "/img/guitars/weezer-classic.jpg",  "electric"),
                    new Guitar("Jet Black Electric", 599, "/img/guitars/jet-black-electric.jpg",  "electric"),
                    new Guitar("Mellow Yellow", 799, "/img/guitars/mellow-yellow.jpg",  "electric"),
                    new Guitar("White Vibes", 699, "/img/guitars/white-vibes.jpg",  "electric"),
                    new Guitar("Brush Riffs", 599, "/img/guitars/brushed-black-electric.jpg",  "electric"),
                    new Guitar("Nature''s Song", 799, "/img/guitars/natures-song.jpg", "electric"),
                    new Guitar("Electric Wood Grain", 399, "/img/guitars/woodgrain-electric.jpg", "electric"),
                };

            if (style == null || style == "all")
                return guitars;

            return (from g in guitars
                    where g.Style == style
                    select g
                    ).ToArray();
        }
    }
}
