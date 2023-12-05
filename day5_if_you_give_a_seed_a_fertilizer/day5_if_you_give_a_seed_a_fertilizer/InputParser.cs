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

        foreach (var foodMapTypes in foodMaps)
        {
            foodMapTypes.MinExpansion = foodMapTypes.FoodMap.Min(f => f.DestinationRangeStart );
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

        var seedRanges = input[0].Split(" ").Skip(1).ToList();
        var minExpansion = foodMaps.Min(f => f.MinExpansion);
        for (var i = 0; i < seedRanges.Count; i += 2)
        {
            var seedNumber = long.Parse(seedRanges.ElementAt(i));
            if (seedNumber + minExpansion > smallestLocation) continue;
            var seedRange = long.Parse(seedRanges.ElementAt(i + 1));
            for (long j = 0; j < seedRange; j++)
            {
                if (seedNumber + j + minExpansion >= smallestLocation) break;
                var seed = new Seed(seedNumber + j, foodMaps);
                if (seed.Location.Value < smallestLocation)
                {
                    smallestLocation = seed.Location.Value;
                }
                // if (seed.Location.EndOfRange > smallestLocation)
                // {
                //     break;
                // }
            }
        }


        return smallestLocation;
    }
}