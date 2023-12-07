namespace day5_if_you_give_a_seed_a_fertilizer.Models;

public class Seed
{
    public Seed(RangeItem seedRange, List<FoodMaps?> foodMapTypes)
    {
        Soil = GetMappedValue(new List<RangeItem> { seedRange },
            foodMapTypes.FirstOrDefault(f => f?.Type == "seed-to-soil"));
        Fertilizer = GetMappedValue(Soil, foodMapTypes.FirstOrDefault(f => f?.Type == "soil-to-fertilizer"));
        Water = GetMappedValue(Fertilizer, foodMapTypes.FirstOrDefault(f => f?.Type == "fertilizer-to-water"));
        Light = GetMappedValue(Water, foodMapTypes.FirstOrDefault(f => f?.Type == "water-to-light"));
        Temperature = GetMappedValue(Light, foodMapTypes.FirstOrDefault(f => f?.Type == "light-to-temperature"));
        Humidity = GetMappedValue(Temperature,
            foodMapTypes.FirstOrDefault(f => f?.Type == "temperature-to-humidity"));
        Location = GetMappedValue(Humidity, foodMapTypes.FirstOrDefault(f => f?.Type == "humidity-to-location"));
        SmallestLocation = Location.Min(l => l.SourceRangeStart);
    }

    private List<RangeItem> Soil { get; set; }
    private List<RangeItem> Fertilizer { get; set; }
    private List<RangeItem> Water { get; set; }
    private List<RangeItem> Light { get; set; }
    private List<RangeItem> Temperature { get; set; }
    private List<RangeItem> Humidity { get; set; }
    public List<RangeItem> Location { get; set; }
    public long SmallestLocation { get; set; }


    private static List<RangeItem> GetMappedValue(List<RangeItem> rangeItems, FoodMaps foodMaps)
    {
        var mappedValues = new List<RangeItem>();
        foreach (var rangeItem in rangeItems)
        {
            foreach (var foodMap in foodMaps.FoodMap)
            {
                if (rangeItem.SourceRangeStart >= foodMap.SourceRangeStart &&
                    rangeItem.SourceRangeStart < foodMap.SourceRangeStart + foodMap.RangeLength)
                {
                    // The whole source range is contained in the food map range
                    var offset = rangeItem.SourceRangeStart - foodMap.SourceRangeStart;
                    mappedValues.Add(new RangeItem
                    {
                        SourceRangeStart = foodMap.DestinationRangeStart + offset ?? 0,
                        RangeLength = rangeItem.RangeLength
                    });
                    break;
                }


                if (rangeItem.SourceRangeStart < foodMap.SourceRangeStart &&
                    (rangeItem.SourceRangeStart + rangeItem.RangeLength) > foodMap.SourceRangeStart)
                {
                    // The source range starts before the food map range and ends inside the food map range
                    mappedValues.Add(new RangeItem
                    {
                        SourceRangeStart = foodMap.DestinationRangeStart ?? 0,
                        RangeLength = (rangeItem.SourceRangeStart + rangeItem.RangeLength) - foodMap.SourceRangeStart
                    });
                    mappedValues.Add(new RangeItem
                    {
                        SourceRangeStart = rangeItem.SourceRangeStart,
                        RangeLength = foodMap.SourceRangeStart - foodMap.SourceRangeStart
                    });
                }

                if (rangeItem.SourceRangeStart > foodMap.SourceRangeStart &&
                    (rangeItem.SourceRangeStart + rangeItem.RangeLength) <
                    (foodMap.SourceRangeStart + foodMap.RangeLength))
                {
                    // The source range starts inside the food map range and ends after the food map range
                    var offset = rangeItem.SourceRangeStart - foodMap.SourceRangeStart;
                    mappedValues.Add(new RangeItem
                    {
                        SourceRangeStart = foodMap.DestinationRangeStart + offset ?? 0,
                        RangeLength = (foodMap.SourceRangeStart + foodMap.RangeLength) - rangeItem.SourceRangeStart
                    });
                    mappedValues.Add(new RangeItem
                    {
                        SourceRangeStart = foodMap.SourceRangeStart + foodMap.RangeLength,
                        RangeLength = (rangeItem.SourceRangeStart + rangeItem.RangeLength) -
                                      (foodMap.SourceRangeStart + foodMap.RangeLength)
                    });
                }
            }

            if (mappedValues.Count == 0)
            {
                // The whole destination range is outside the food map range
                mappedValues.Add(rangeItem);
            }
        }

        return mappedValues;
    }

    public class Category
    {
        public long Value { get; set; }
        public long EndOfRange { get; set; }
    }
}