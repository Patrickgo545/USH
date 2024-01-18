using System;

namespace MyApp // Note: actual namespace depends on the project name.
{
    internal class Program
    {
        static void Main(string[] args)
        // {
        //     int num01;
        //     int num02;

        //     Console.Write("Input a number: ");
        //     num01 = Convert.ToInt32(Console.ReadLine());

        //     Console.Write("Input a second number: ");
        //     num02 = Convert.ToInt32(Console.ReadLine());

        //     int result = num01 * num02;
        //     Console.WriteLine($"{num01} * {num02} = {result}");
            
        //     // WAIT TO CLOSE
        //     Console.ReadKey();
        // }

        {
            // CHALLENGE FIND THE AVERAGE OF 3 NUMBERS
            Console.WriteLine("I'm going to help you find the average of 3 numbers");
            
            double num01;
            Console.WriteLine("number 1: ");
            num01 = Convert.ToDouble(Console.ReadLine());

            double num02;
            Console.WriteLine("number 2: ");
            num02 = Convert.ToDouble(Console.ReadLine());

            double num03;
            Console.WriteLine("number 3: ");
            num03 = Convert.ToDouble(Console.ReadLine());

            double result = (num01 + num02 + num03) / 3;
            Console.WriteLine($"The average is {result}");

            // WAIT TO CLOSE
            Console.ReadKey();
        }
    }
}