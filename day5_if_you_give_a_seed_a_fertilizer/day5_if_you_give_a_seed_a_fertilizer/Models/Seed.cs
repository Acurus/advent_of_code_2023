namespace day5_if_you_give_a_seed_a_fertilizer.Models;

public class Seed
{
    public Seed(long seedNumber, List<FoodMaps> foodMapTypes)
    {
        SeedNumber = new Category() { Value = seedNumber };
        Soil = GetMappedValue(SeedNumber, foodMapTypes.Where(f => f.Type == "seed-to-soil"));
        Fertilizer = GetMappedValue(Soil, foodMapTypes.Where(f => f.Type == "soil-to-fertilizer"));
        Water = GetMappedValue(Fertilizer, foodMapTypes.Where(f => f.Type == "fertilizer-to-water"));
        Light = GetMappedValue(Water, foodMapTypes.Where(f => f.Type == "water-to-light"));
        Temperature = GetMappedValue(Light, foodMapTypes.Where(f => f.Type == "light-to-temperature"));
        Humidity = GetMappedValue(Temperature, foodMapTypes.Where(f => f.Type == "temperature-to-humidity"));
        Location = GetMappedValue(Humidity, foodMapTypes.Where(f => f.Type == "humidity-to-location"));
    }

    private Category SeedNumber { get; set; }
    private Category Soil { get; set; }
    private Category Fertilizer { get; set; }
    private Category Water { get; set; }
    private Category Light { get; set; }
    private Category Temperature { get; set; }
    private Category Humidity { get; set; }
    public Category Location { get; set; }


    private static Category GetMappedValue(Category category, IEnumerable<FoodMaps> foodMaps)
    {
        foreach (var foodMap in foodMaps.First().FoodMap)
        {
            if (category.Value < foodMap.SourceRangeStart ||
                category.Value > foodMap.SourceRangeStart + foodMap.RangeLength) continue;
            var diff = category.Value - foodMap.SourceRangeStart;
            category.Value = foodMap.DestinationRangeStart + diff;
            category.EndOfRange = foodMap.DestinationRangeStart + foodMap.RangeLength;
            return category;
        }

        return category;
    }

    public class Category
    {
        public long Value { get; set; }
        public long EndOfRange { get; set; }
    }
}