using day6_wait_for_It;

var input = File.ReadAllLines("input.txt").ToList();

var racesPart1 = InputParser.RacesPart1(input);
Console.WriteLine(Solution.Process(racesPart1));

var racesPart2 = InputParser.RacesPart2(input);
Console.WriteLine(Solution.Process(racesPart2));