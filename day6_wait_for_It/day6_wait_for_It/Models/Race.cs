namespace day6_wait_for_It.Models;

public class Race
{
    public Race(long time, long distance)
    {
        Time = time;
        Distance = distance;
    }

    public long Time { get; set; }
    public long Distance { get; set; }
    public long WaysToWin { get; set; }
}