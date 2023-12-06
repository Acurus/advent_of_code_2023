using day6_wait_for_It;
using Xunit;

namespace Tests;

public class ExampleTests
{
    [Fact]
    public void TestExampleDataPart1AssertEqual()
    {
        var input = File.ReadAllLines("test_input.txt").ToList();
        var races = InputParser.RacesPart1(input);
        var actual = Solution.Process(races);
        const int expected = 288;

        Assert.Equal(expected, actual);
    }

    [Fact]
    public void TestExampleDataPart2AssertEqual()
    {
        var input = File.ReadAllLines("test_input.txt").ToList();
        var races = InputParser.RacesPart2(input);
        var actual = Solution.Process(races);
        const int expected = 71503;

        Assert.Equal(expected, actual);
    }
}