using System;
namespace Ch8_Testing
{
    public interface IDb
    {
        Guitar[] GetGuitarsFromDb();
    }

    public class Db : IDb
    {
        public Guitar[] GetGuitarsFromDb()
        {
            Console.ForegroundColor = ConsoleColor.Yellow;
            Console.WriteLine("      --> GETTING GUITARS FROM DB! Should not see in test.");
            Console.ForegroundColor = ConsoleColor.White;

            var guitars =
                new[] {
                    new Guitar("AX Black", 499, "/img/guitars/ax-black.jpg", "electric"),
                    new Guitar("Jet Black Electric", 599, "/img/guitars/jet-black-electric.jpg",  "electric"),
                    new Guitar("Weezer Classic", 1499, "/img/guitars/weezer-classic.jpg",  "electric"),
                    new Guitar("Acoustic Black", 299, "/img/guitars/black-acoustic.jpg",  "acoustic"),
                    new Guitar("Mellow Yellow", 799, "/img/guitars/mellow-yellow.jpg",  "electric"),
                    new Guitar("White Vibes", 699, "/img/guitars/white-vibes.jpg",  "electric"),
                    new Guitar("Brush Riffs", 599, "/img/guitars/brushed-black-electric.jpg",  "electric"),
                    new Guitar("Nature''s Song", 799, "/img/guitars/natures-song.jpg", "electric"),
                    new Guitar("Electric Wood Grain", 399, "/img/guitars/woodgrain-electric.jpg", "electric"),
                };

            return guitars;
        }
    }
}
