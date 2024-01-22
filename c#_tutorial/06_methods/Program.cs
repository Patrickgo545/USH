using System;
using System.ComponentModel.DataAnnotations;
using System.Globalization;

namespace MyApp // Note: actual namespace depends on the project name.
{
    internal class Program
    {
        static void Main(string[] args)
        {
            PrintNumber();
            Console.WriteLine("----------------");

            MeetAlien();
            Console.WriteLine("----------------");

            Multiply(5, 5);
            Console.WriteLine("----------------");

            EvenOrOdd(PrintNumber());
            Console.WriteLine("----------------");

            WordCount();

        }


        // FUNCTION - PRINT A RANDOM NUMBER
        static int PrintNumber()
        {
            Random numGen = new Random();
            int number = numGen.Next(0,10);
            Console.WriteLine(number);
            return number;
        }

        // FUNCTION - MEET AN ALIEN
        static void MeetAlien()
        {
            Random numberGen = new Random();
            
            string name = "X-" + numberGen.Next(10,9999);
            int age = numberGen.Next(10,500);

            Console.WriteLine($"Hi, im {name}\nI'm {age} years old \nOh, & i'm an alien");
        }

        // FUNCTION - SQUARE A NUMBER
        static int Square(int number)
        {
            int result = number * number;
            return result;
        }

        // FUNCTION - MULTIPLY 2 NUMBERS
        static void Multiply (int num1, int num2)
        {
            int result = num1 * num2;
            Console.WriteLine($"Result: {result}");
        }

        // FUNCTION - CHECK IF NUMBER IS EVEN OR ODD
        static void EvenOrOdd(int number)
        {
            if (number % 2 == 0)
            {
                Console.WriteLine($"{number} is even.");
            }
            
            else
            {
                Console.WriteLine($"{number} is odd");
            }
        }

        // FUNCTION(CHALLENGE) - CHECK # OF WORDS IN A USER INPUT SENTENCE
        static void WordCount()
        {
            Console.WriteLine("Enter a sentence: ");

            string sentence = Console.ReadLine();
            int length_sentence = sentence.Split(" ").Length;

            Console.WriteLine($"Your sentence \"{sentence}\"\nHas {length_sentence} words.");
        }

    }
}