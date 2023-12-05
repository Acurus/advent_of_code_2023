namespace day5_if_you_give_a_seed_a_fertilizer.Models;

public class Seed
{
    public Seed(string seedNumber, List<FoodMapTypes> foodMapTypes)
    {
        SeedNumber = int.Parse(seedNumber);
        Soil = MapSeed2Soil(SeedNumber, foodMapTypes);
        Fertilizer = MapSoil2Fertilizer(Soil, foodMapTypes);
        Water = MapFertilizer2Water(Fertilizer, foodMapTypes);
        Light = MapWater2Light(Water, foodMapTypes);
        Temperature = MapLight2Temperature(Light, foodMapTypes);
        Humidity = MapTemperature2Humidity(Temperature, foodMapTypes);
        Location = Humidity;
    }


    private int SeedNumber { get; set; }
    private int Soil { get; set; }
    private int Fertilizer { get; set; }
    private int Water { get; set; }
    private int Light { get; set; }
    private int Temperature { get; set; }
    private int Humidity { get; set; }
    public int Location { get; set; }

    private static int MapSeed2Soil(int seedNumber, IEnumerable<FoodMapTypes> foodMapTypes)
    {
        var foodMaps = foodMapTypes
            .Where(f => f.Type == "fertilizer");
        return GetMappedValue(seedNumber, foodMaps);
    }

    private static int MapSoil2Fertilizer(int soilNumber, IEnumerable<FoodMapTypes> foodMapTypes)
    {
        var foodMaps = foodMapTypes
            .Where(f => f.Type == "fertilizer");
        return GetMappedValue(soilNumber, foodMaps);
    }

    private static int MapFertilizer2Water(int fertilizerNumber, IEnumerable<FoodMapTypes> foodMapTypes)
    {
        var foodMaps = foodMapTypes
            .Where(f => f.Type == "water");
        return GetMappedValue(fertilizerNumber, foodMaps);
    }

    private static int MapWater2Light(int waterNumber, IEnumerable<FoodMapTypes> foodMapTypes)
    {
        var foodMaps = foodMapTypes
            .Where(f => f.Type == "light");
        return GetMappedValue(waterNumber, foodMaps);
    }

    private static int MapLight2Temperature(int lightNumber, IEnumerable<FoodMapTypes> foodMapTypes)
    {
        var foodMaps = foodMapTypes
            .Where(f => f.Type == "temperature");
        return GetMappedValue(lightNumber, foodMaps);
    }

    private static int MapTemperature2Humidity(int temperatureNumber, IEnumerable<FoodMapTypes> foodMapTypes)
    {
        var foodMaps = foodMapTypes
            .Where(f => f.Type == "humidity");
        return GetMappedValue(temperatureNumber, foodMaps);
    }


    private static int GetMappedValue(int seedNumber, IEnumerable<FoodMapTypes> foodMaps)
    {
        foreach (var foodMap in foodMaps.First().FoodMap)
        {
            if (foodMap.SourceRangeStart + foodMap.RangeLength > seedNumber ||
                foodMap.SourceRangeStart < seedNumber) continue;
            var diff = foodMap.SourceRangeStart - seedNumber;
            return foodMap.DestinationRangeStart + diff;
        }

        return seedNumber;
    }
}