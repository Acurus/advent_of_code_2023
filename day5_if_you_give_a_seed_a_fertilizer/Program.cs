// See https://aka.ms/new-console-template for more information

// Read input file and parse into a list of integers

using day5_if_you_give_a_seed_a_fertilizer;

var input = File.ReadAllLines("input.txt").ToList();
var foodMaps = InputParser.FoodMaps(input);
var seeds = InputParser.Seeds(input, foodMaps);
Console.WriteLine(seeds.Min(s=>s.Location));


