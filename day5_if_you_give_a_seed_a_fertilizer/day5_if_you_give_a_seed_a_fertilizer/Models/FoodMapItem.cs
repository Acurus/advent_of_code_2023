using day5_if_you_give_a_seed_a_fertilizer.Models;

namespace day5_if_you_give_a_seed_a_fertilizer;

public class FoodMaps
{
    public string Type { get; set; }

    public List<FoodMapItem> FoodMap { get; set; }
}

public class FoodMapItem
{
    public long DestinationRangeStart { get; set; }
    public long SourceRangeStart { get; set; }
    public long RangeLength { get; set; }
}