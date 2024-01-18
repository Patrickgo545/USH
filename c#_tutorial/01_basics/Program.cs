// See https://aka.ms/new-console-template for more information
using System;

namespace my_awesome_program
{
    class Program
    {
        static void Main(string[] args)
        // {
        //     // CHANGE APPEARANCE
        //     Console.Title = "Skynet";
        //     Console.ForegroundColor = ConsoleColor.Green;
        //     Console.WindowHeight = 40;

        //     // DIALOGUE
        //     Console.WriteLine("Hello, what's your name?");
        //     string userName = Console.ReadLine();

        //     Console.WriteLine($"Hello {userName} My name is RX-9000, im an AI here to destroy your race. \nWhat is your favorite color?");
        //     string userColor = Console.ReadLine();
 
        //     Console.WriteLine("Very nice. Mine is destruction.");

        //     // END PROGRAM
        //     Console.ReadKey();
        // }

        {
            // PRACTICE
            Console.Title = "Last Light Inn";
            Console.WindowHeight = 40;
            Console.ForegroundColor = ConsoleColor.White;

            // DIALOGUE
            Console.WriteLine("Ayy Traveller, what be thy name?");
            string travellerName = Console.ReadLine();

            Console.WriteLine($"Ay {travellerName} How many beasts did ye slay today?");
            string travellerKillCount = Console.ReadLine(); 

            Console.WriteLine($"Ayy.. well I killed more beasts than {travellerKillCount}. \nDo better");

            // KEEP WINDOW OPEN
            Console.ReadKey();
        }
    }
}
