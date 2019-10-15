using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;

namespace Ch4_OOP.Models
{
    public class ParkingLot: IEnumerable<string>
    {
        private Dictionary<string, Car> spots;

        public ParkingLot(IEnumerable<string> names)
        {
            spots = names.ToDictionary(n => n, name => (Car)null);
        }

        public static ParkingLot Create(int spotsPerLevel, int levels)
        {
            List<string> names = new List<string>();
            string[] level_names = { "A", "B", "C", "D", "E", "F", "G" };
            foreach(var ln in level_names.Take(levels))
            {
                for (int n = 0; n < spotsPerLevel; n++)
                {
                    names.Add($"{ln}{n+1}");
                }
            }

            return new ParkingLot(names);
        }

        public IEnumerator<string> GetEnumerator()
        {
            foreach (var spot in spots.Keys)
            {
                yield return spot;
            }
        }

        IEnumerator IEnumerable.GetEnumerator()
        {
            foreach (var spot in spots.Keys)
            {
                yield return spot;
            }
        }

        public string[] TakenSpots()
        {
            return (
                from spot in spots
                where spot.Value != null
                select $"{spot.Key} has the {spots[spot.Key].ModelName}"
                ).ToArray();
        }

        public void ParkCar(Car car)
        {
            foreach (var kv in spots)
            {
                if (kv.Value == null)
                {
                    spots[kv.Key] = car;
                    break;
                }
            }
        }
    }
}
