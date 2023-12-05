using day5_if_you_give_a_seed_a_fertilizer.Models;

namespace day5_if_you_give_a_seed_a_fertilizer;

public class FoodMaps
{
    public string Type { get; set; }
    public List<FoodMap> FoodMap { get; set; }
}

public class FoodMap
{
    public int SourceRangeStart { get; set; }
    public int SourceRangeEnd { get; set; }
    public int RangeLength { get; set; }
}