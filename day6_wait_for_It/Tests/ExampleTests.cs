using day6_wait_for_It;
using Xunit;

namespace Tests;

public class ExampleTests
{
    [Fact]
    public void TestExampleDataPart1AssertEqual()
    {
        var input = File.ReadAllLines("test_input.txt").ToList();
        var races = InputParser.Races(input);
        var actual = Part1.Process(races);
        const int expected = 288;
        
        Assert.Equal(expected, actual);
    }
    
    [Fact]
    public void TestExampleDataPart2AssertEqual()
    {
        
        Assert.True(false);
    }
}