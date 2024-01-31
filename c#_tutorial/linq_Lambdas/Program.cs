using System.Reflection.Metadata.Ecma335;
using System.Linq;
using System.Collections.Generic;
using System.Runtime.InteropServices;
using System.Globalization;
using Microsoft.VisualBasic;

namespace linq_Lambdas;

class Program
{
    static Random _random = new Random();
    static void Main(string[] args)
    {
        // LIST OF NUMBERS
        var myNumbers = new List<int> {0,1,2,3,4,5,6,7,8,9};

        // // CREATE A LIST FOR ALL NUMBERS OVER 5
        // var numbersOver5 = new List<int>();
        // foreach (var number in myNumbers)
        // {
        //     if(number > 5) 
        //         numbersOver5.Add(number);
        // }


        // LAMBDA EXPRESSION
        var numbersOver5 = myNumbers.Where(number => number > 5);
        Console.WriteLine(numbersOver5 + "test");

        foreach(int number in numbersOver5)
        {
            Console.WriteLine(number);
        }

        // BOOLEAN
        bool allPositiveNumbers = myNumbers.All(n => n >= 0);
        Console.WriteLine($"All positive numbers {allPositiveNumbers}");


        // FIND THE FIRST ITEM
        var firstNumberGreaterThan5 = myNumbers.First(n => n > 5);
        Console.WriteLine("test"); 
        Console.WriteLine($"first num > 5 :{firstNumberGreaterThan5}");
        
        // ---------------
        // GAMES CLASS  
        List<Game> myGames = new List<Game>();

        myGames.Add(new Game("Dark Souls", 9.9));
        myGames.Add(new Game("Elden Ring", 10));
        myGames.Add(new Game("Baulder's Gate", 10));
        myGames.Add(new Game("Cyberpunk 2077" , 7));
        myGames.Add(new Game("Mass Effect 3", 7));

        foreach (var game in myGames)
        {
            Console.WriteLine(game.Name);
        }


        // LINQ LAMBDA PULL LIST OF PERFECT GAMES
        List<Game> perfectGames = myGames.Where(games => games.SteamScore >= 10).ToList();
        
        foreach (var game in perfectGames)
        {
            Console.WriteLine(game.Name);
        }

        // STRING TOGETHER MULTIPLE LINQ 
        // SUGGEST A GAME 
        // MUST HAVE A SCORE OF 9 OR ABOVE
        // MUST BE RANDOM

        Console.WriteLine("------------");
        List<Game> suggestedGame = myGames
            .Where(g => g.SteamScore >= 9)
            .OrderBy(g => _random.Next())
            .Take(2)
            .ToList();

        foreach (var game in suggestedGame)
        {
            Console.WriteLine(game.Name);
        }

        Console.ReadKey();
    }
}
