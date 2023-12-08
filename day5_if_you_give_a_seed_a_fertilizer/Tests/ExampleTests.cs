using day5_if_you_give_a_seed_a_fertilizer;
using Xunit;

namespace Tests;

public class ExampleTests
{
    [Fact]
    public void TestExampleDataPart1AssertEqual()
    {
        const int expected = 35;

        var input = File.ReadAllLines("test_input2.txt").ToList();
        var foodMaps = InputParser.FoodMaps(input);
        var seeds = InputParser.SeedsPart1(input, foodMaps).ToList();
        var minimumLocation = seeds.Min(s => s.SmallestLocation.SourceStart);
        Assert.Equal(expected, minimumLocation);
    }

    [Fact]
    public void TestExampleDataPart2AssertEqual()
    {
        const int expected = 46;

        var input = File.ReadAllLines("test_input2.txt").ToList();
        var foodMaps = InputParser.FoodMaps(input);
        var smallestLocation = InputParser.SeedsPart2(input, foodMaps);
        Assert.Equal(expected, smallestLocation);
    }
}