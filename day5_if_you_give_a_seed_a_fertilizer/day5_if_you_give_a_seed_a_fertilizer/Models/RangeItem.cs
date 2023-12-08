using day5_if_you_give_a_seed_a_fertilizer.Models;

namespace day5_if_you_give_a_seed_a_fertilizer;

public class FoodMaps
{
    public string Type { get; set; }

    public List<RangeItem> FoodMap { get; set; }
}

public class RangeItem
{
    public long? DestinationStart { get; set; }
    public long SourceStart { get; set; }
    public long RangeLength { get; set; }
}