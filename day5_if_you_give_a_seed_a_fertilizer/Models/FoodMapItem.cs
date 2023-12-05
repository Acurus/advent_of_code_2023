using day5_if_you_give_a_seed_a_fertilizer.Models;

namespace day5_if_you_give_a_seed_a_fertilizer;

public class FoodMapTypes
{
    public string Type { get; set; }
    public List<FoodMapItem> FoodMap { get; set; }
}

public class FoodMapItem
{
    public int DestinationRangeStart { get; set; }
    public int SourceRangeStart { get; set; }
    public int RangeLength { get; set; }
}