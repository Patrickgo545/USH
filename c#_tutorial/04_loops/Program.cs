using System;

namespace MyApp // Note: actual namespace depends on the project name.
{
    internal class Program
    {
        static void Main(string[] args)
        {
            // FOR LOOPS   
            
            // 1 - 10 loop
            for (int i = 0; i < 10; i++)
            {
                Console.WriteLine(i + 1);
            }

            // POWER LOOP
            int user_input;
            int user_power;
            Console.WriteLine("Input a number: ");
            user_input = Convert.ToInt32(Console.ReadLine());

            Console.WriteLine("To the power of what? ");
            user_power = Convert.ToInt32(Console.ReadLine());

            for (int i = 0; i < user_power; i++)
            {
                int raised = Convert.ToInt32(Math.Pow(user_input, i));
                Console.WriteLine(raised);
            }

            // WHILE LOOP
            Random numberGen = new Random();

            int roll = 0;
            int attempts = 0;

            Console.WriteLine("Press enter to roll teh die.");

            while (roll != 6) {
                // Console.ReadKey();

                roll = numberGen.Next(1, 7);
                Console.WriteLine($"You rolled: {roll}");
                attempts++;
            }

            Console.WriteLine($"{attempts} attempts to roll a 6");
        

            // PRACTICE
            // ROLL 2 DIE - END LOOP WHEN PLAYER ROLLS 2 OF A KIND

            Random numGenerate = new Random();

            int die_1;
            int die_2;
            int count = 0;

            Boolean match = false;

            // Console.WriteLine("Press Enter to roll die.");

            while (match == false) 
            {
                // Console.ReadLine();

                die_1 = numGenerate.Next(1,7);
                die_2 = numGenerate.Next(1,7);

                Console.WriteLine($"Roll 1: {die_1} \nRoll 2: {die_2}\n");

                count++;

                if (die_1 == die_2) {
                    match = true;
                }
            }

            Console.WriteLine($"{count} attempts.");
        }

    }
}