using System;
using System.Collections.Generic;

namespace MyApp // Note: actual namespace depends on the project name.
{
    internal class Program
    {
        static void Main(string[] args)
        {
            // // CREATING ARRAYS  
            // string[] movies = {
            //     "Lord of the Rings", 
            //     "Fight Club", 
            //     "Interstellar",
            //     "Gladiator"
            // };

            // for (int i = 0; i < movies.Length; i++)
            // {
            //     int rank = i + 1;
            //     Console.WriteLine($"{rank}. {movies[i]}");
            // }

            // ---------------------------------------------

            // // APPENDING TO AN ARRAY
            // string[] movies = new string[4];

            // Console.WriteLine("Type in 4 movies");

            // for (int i = 0; i < 4; i++)
            // {
            //     movies[i] = Console.ReadLine();
            // }

            // Console.WriteLine("Here they are alphabetically: ");

            // Array.Sort(movies);

            // for (int i = 0; i < movies.Length; i++)
            // {
            //     Console.WriteLine(movies[i]);
            // }

            // ---------------------------------------------

            // CREATING A LIST 
            List<string> shoppingList = new List<string>();

            shoppingList.Add("Dreams");
            shoppingList.Add("Miracles");
            shoppingList.Add("Rainbows");
            shoppingList.Add("Pony");


            for (int i = 0; i < shoppingList.Count; i++)
            {
                Console.WriteLine(shoppingList[i]);
            }

            // REMOVE FROM LIST
            shoppingList.Remove("Dreams");
            shoppingList.RemoveAt(1);

            Console.WriteLine("-------------");

            for (int i = 0; i < shoppingList.Count; i++)
            {
                Console.WriteLine(shoppingList[i]);
            }

            // EXERCISE 
            // LET A TEACHER INPUT NAMES OF THEIR STUDENTS & ARRANGE ALPHABETICALLY 

            List<string> students = new List<string>();
            int studentCount;

            Console.WriteLine("How many students are in your class? ");
            studentCount = Convert.ToInt32(Console.ReadLine());

            Console.WriteLine("Input their names: ");
            for (int i = 0; i < studentCount; i++)
            {
                students.Add(Console.ReadLine());
            }

            students.Sort();

            for (int i = 0; i < students.Count; i++)
            {
                Console.WriteLine(students[i]);
            }

        }
    }
}