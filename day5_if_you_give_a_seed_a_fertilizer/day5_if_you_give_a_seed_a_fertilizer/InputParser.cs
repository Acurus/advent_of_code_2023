using day5_if_you_give_a_seed_a_fertilizer.Models;

namespace day5_if_you_give_a_seed_a_fertilizer;

public static class InputParser
{
    public static List<FoodMaps?> FoodMaps(List<string> input)
    {
        var foodMaps = new List<FoodMaps?>();
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
                    FoodMap = new List<RangeItem>()
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
                var foodMapItem = new RangeItem
                {
                    DestinationStart = long.Parse(foodMapLine[0]),
                    SourceStart = long.Parse(foodMapLine[1]),
                    RangeLength = long.Parse(foodMapLine[2])
                };
                foodMap.FoodMap.Add(foodMapItem);
            }
        }

        return foodMaps;
    }

    public static IEnumerable<SeedRange> SeedsPart1(List<string> input, List<FoodMaps?> foodMaps)
    {
        var seeds = new List<SeedRange>();
        foreach (var line in input)
        {
            if (!line.StartsWith("seeds:")) return seeds;
            var seedNumbers = line.Split(" ").Select(long.Parse);
            seeds.AddRange(seedNumbers.Skip(1).Select(seedNumber => new SeedRange(new RangeItem()
            {
                DestinationStart = 0,
                SourceStart = seedNumber,
                RangeLength = 0
            }, foodMaps)));
        }

        return seeds;
    }

    public static long SeedsPart2(List<string> input, List<FoodMaps?> foodMaps)
    {
        var smallestLocation = long.MaxValue;

        var seedData = input[0]
            .Split(" ")
            .Skip(1)
            .Select(long.Parse)
            .ToList();

        for (var i = 0; i < seedData.Count; i += 2)
        {
            var seedNumber = seedData.ElementAt(i);
            var seedRange = seedData.ElementAt(i + 1);
            var seedRangeItem = new RangeItem
            {
                DestinationStart = null,
                SourceStart = seedNumber,
                RangeLength = seedRange
            };
            var seed = new SeedRange(seedRangeItem, foodMaps);
            if (seed.SmallestLocation.SourceStart < smallestLocation)
            {
                smallestLocation = seed.SmallestLocation.SourceStart;
            }
        }
        return smallestLocation;
    }
}