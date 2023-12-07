using day5_if_you_give_a_seed_a_fertilizer.Models;

namespace day5_if_you_give_a_seed_a_fertilizer;

public static class InputParser
{
    public static List<FoodMaps> FoodMaps(List<string> input)
    {
        var foodMaps = new List<FoodMaps>();
        foreach (var line in input)
        {
            if (line.Length == 0) continue;
            if (line.StartsWith("seeds:"))
            {
            }
            else if (line.EndsWith("map:"))
            {
                var foodMap = new FoodMaps
                {
                    Type = line.Split(" ")[0],
                    FoodMap = new List<FoodMapItem>()
                };
                foodMaps.Add(foodMap);
            }
            else
            {
                if (!char.IsNumber(line[0]))
                {
                    throw new Exception("Unexpected input line: " + line);
                }

                var foodMap = foodMaps.Last();
                var foodMapLine = line.Split(" ");
                var foodMapItem = new FoodMapItem
                {
                    DestinationRangeStart = long.Parse(foodMapLine[0]),
                    SourceRangeStart = long.Parse(foodMapLine[1]),
                    RangeLength = long.Parse(foodMapLine[2])
                };
                foodMap.FoodMap.Add(foodMapItem);
            }
        }

        return foodMaps;
    }

    public static IEnumerable<Seed> SeedsPart1(List<string> input, List<FoodMaps> foodMaps)
    {
        var seeds = new List<Seed>();
        foreach (var line in input)
        {
            if (!line.StartsWith("seeds:")) return seeds;
            var seedNumbers = line.Split(" ").Select(long.Parse);
            seeds.AddRange(seedNumbers.Skip(1).Select(seedNumber => new Seed(seedNumber, foodMaps)));
        }

        return seeds;
    }

    public static long SeedsPart2(List<string> input, List<FoodMaps> foodMaps)
    {
        var smallestLocation = long.MaxValue;

        var seedData = input[0]
            .Split(" ")
            .Skip(1)
            .Select(long.Parse)
            .ToList();

        for (var i = 0; i < seedData.Count; i += 2)
        {
            // Calculate per range
            // split up existing ranges, into new ranges that map to the destination ranges of the level below
            // then calculate the new ranges for the level below
            // At the end we end up with a bunch of ranges that we somehow can use.
            var ranges = new Dictionary<long, Tuple<long, long>>();
            var seedNumber = seedData.ElementAt(i);
            var seedRange = seedData.ElementAt(i + 1);
            for (long j = 0; j < seedRange; j++)
            {
                var seed = new Seed(seedNumber + j, foodMaps);
                if (seed.Location.Value < smallestLocation)
                {
                    smallestLocation = seed.Location.Value;
                }
            }
        }

        return smallestLocation;
    }
}