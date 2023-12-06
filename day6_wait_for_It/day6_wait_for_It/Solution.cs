using day6_wait_for_It.Models;

namespace day6_wait_for_It;

public static class Solution
{
    public static long Process(List<Race> races)
    {
        foreach (var race in races)
            for (var i = 0; i <= race.Time; i++)
                if (i * (race.Time - i) > race.Distance)
                    race.WaysToWin++;

        long waysToWin = 0;
        foreach (var race in races)
            if (waysToWin == 0)
                waysToWin = race.WaysToWin;
            else waysToWin *= race.WaysToWin;

        return waysToWin;
    }
}