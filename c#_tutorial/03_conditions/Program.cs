using System;

namespace MyApp // Note: actual namespace depends on the project name.
{
    internal class Program
    {
        static void Main(string[] args)
        {
            // TICKETS
            // Console.WriteLine("Welcome! Tickets are $5. Please insert cash.");

            // int cash = Convert.ToInt32(Console.ReadLine());

            // if (cash < 5) 
            // {  
            //     Console.WriteLine("That's not enough money.");
            // }
            // else if (cash == 5)
            // {
            //     Console.WriteLine("Here is your ticket");
            // }

            // else 
            // {
            //     int change = cash - 5;
            //     Console.WriteLine($"Here is your Ticket & your change ${change}");
            // }

            
            // ROLLER COASTER
            int age;
            int height;

            int min_age = 18;
            int min_height = 160;

            Console.Write("What is your age? ");
            age = Convert.ToInt32(Console.ReadLine());

            Console.Write("What is your height? ");
            height = Convert.ToInt16(Console.ReadLine());

            if (age >= min_age && height >= min_height) 
            {
                Console.Write("You may enter.");
            }

            else if (age < min_age && height >= min_height)
            {
                Console.WriteLine("Not old enough.");
            }

            else if (height < min_height && age >= min_age)
            {
                Console.WriteLine("Not tall enough.");
            }

            else
            {
                Console.Write("Get out of here.");
            }
        }
    }
}