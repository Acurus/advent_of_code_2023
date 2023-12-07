// See https://aka.ms/new-console-template for more information

// Read input file and parse into a list of integers

using day5_if_you_give_a_seed_a_fertilizer;

var input = File.ReadAllLines("input.txt").ToList();
var foodMaps = InputParser.FoodMaps(input);
var seedsPart1 = InputParser.SeedsPart1(input, foodMaps);
var seedsPart2 = InputParser.SeedsPart2(input, foodMaps);
Console.WriteLine(seedsPart1.Min(s=>s.SmallestLocation));
Console.WriteLine(seedsPart2);

