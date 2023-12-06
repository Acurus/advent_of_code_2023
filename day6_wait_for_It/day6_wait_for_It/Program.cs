using day6_wait_for_It;

var input = File.ReadAllLines("input.txt").ToList();
var races = InputParser.Races(input);
Console.WriteLine(Part1.Process(races));