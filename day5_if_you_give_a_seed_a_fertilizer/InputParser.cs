using day5_if_you_give_a_seed_a_fertilizer.Models;

namespace day5_if_you_give_a_seed_a_fertilizer;

public static class InputParser
{
    public static List<FoodMapTypes> FoodMaps(List<string> input)
    {
        var foodMaps = new List<FoodMapTypes>();
        foreach (var line in input)
        {
            if (line.StartsWith("seeds:"))
            {
            }
            else if (line.EndsWith("map:"))
            {
                var foodMap = new FoodMapTypes
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
                    DestinationRangeStart = int.Parse(foodMapLine[0]),
                    SourceRangeStart = int.Parse(foodMapLine[1]),
                    RangeLength = int.Parse(foodMapLine[2])
                };
                foodMap.FoodMap.Add(foodMapItem);
            }
        }

        return foodMaps;
    }

    public static IEnumerable<Seed> Seeds(List<string> input, List<FoodMapTypes> foodMaps)
    {
        var seeds = new List<Seed>();
        foreach (var line in input)
        {
            if (!line.StartsWith("seeds:")) return seeds;
            var seedNumbers = line.Split(" ");
            seeds.AddRange(seedNumbers.Skip(1).Select(seedNumber => new Seed(seedNumber, foodMaps)));
        }

        return seeds;
    }
}