using day6_wait_for_It.Models;

namespace day6_wait_for_It;

public static class InputParser
{
    public static List<Race> RacesPart1(List<string> input)
    {
        var times = new List<long>();
        var distance = new List<long>();
        foreach (var line in input)
        {
            if (line.Length == 0) continue;
            if (line.StartsWith("Time:"))
                times.AddRange(line
                    .Split(":")[1]
                    .Trim()
                    .Split(" ")
                    .Where(i => i != "")
                    .Select(long.Parse));
            else if (line.StartsWith("Distance:"))
                distance.AddRange(line
                    .Split(":")[1]
                    .Trim()
                    .Split(" ")
                    .Where(i => i != "")
                    .Select(long.Parse));
        }


        return times
            .Select((t, i) =>
                new Race(t, distance[i]))
            .ToList();
    }

    public static List<Race> RacesPart2(List<string> input)
    {
        long time = 0;
        long distance = 0;
        foreach (var line in input)
        {
            if (line.Length == 0) continue;
            if (line.StartsWith("Time:"))
                time = long.Parse(string.Join("", line
                    .Split(":")[1]
                    .Trim()
                    .Split(" ")
                    .Where(i => i != "")
                ));
            else if (line.StartsWith("Distance:"))
                distance = long.Parse(string.Join("", line
                    .Split(":")[1]
                    .Trim()
                    .Split(" ")
                    .Where(i => i != "")
                ));
        }

        return new List<Race>
        {
            new(time, distance)
        };
    }
}