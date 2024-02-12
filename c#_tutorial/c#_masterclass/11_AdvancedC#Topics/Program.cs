using System.ComponentModel;
using System.Data;
using System.Diagnostics;

namespace _11_AdvancedC_Topics;

class Program
{
    public static void FortuneTeller()
    {
        Random fortune = new Random();
        List<string> prophecies = new List<string>();

        prophecies.Add("True");
        prophecies.Add("False");
        prophecies.Add("Maybe");
        
        var chosenProphecy = prophecies[fortune.Next(prophecies.Count)];
        Console.WriteLine(chosenProphecy);
    }

    // DATETIME 
    public static DateTime GetTomorrow()
    {
        return DateTime.Now.AddDays(1);
    }

    // FIRST DAY OF YEAR METHOD
    public static DateTime FirstDayOfYear(int year)
    {
        return new DateTime(year, 1, 1);
    }

    // ENUMS (Enumerations) - Define a set of names constants
    enum Months { Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec }
    
    static void Main(string[] args)
    {
        Months jan = Months.Jan;
        Months a = Months.Jan;

        Console.WriteLine(jan == a);
        Console.WriteLine(Months.Feb);
        Console.WriteLine((int)Months.Dec);

        // -------------------------

        // MATHS
        Console.WriteLine("Rounding up " + Math.Ceiling(15.3));
        Console.WriteLine("Round Down " + Math.Floor(15.3)); 

        // HIGHER 
        int num1 = 13;
        int num2 = 9;
        Console.WriteLine("Higher of num1 {0} & num2 {1} is {2}", num1, num2, Math.Max(num1, num2));
        

        // POWER
        Console.WriteLine("3 to the power of 5 is {0}", Math.Pow(3,5));


        // -------------------------
        // RANDOM
        Random dice = new Random();
        int numEyes;


        Console.WriteLine("Dice \n------------");
        for (int i = 0; i < 10; i++)
        {
            numEyes = dice.Next(1,7);
            Console.WriteLine(numEyes);
        }

        // FORTUNE TELLER
        Console.WriteLine("Ask me a True / False Question");
        // Console.ReadLine();

        FortuneTeller();

        //-----------------------

        // DATETIME

        DateTime birthday = new DateTime(1995, 2, 8);
        Console.WriteLine("My birthday is {0}", birthday);

        // WRITE TODAY ON SCREEN 
        Console.WriteLine(DateTime.Now);

        // TOMORROW
        DateTime tomorrow = GetTomorrow();
        Console.WriteLine("Tomorrow will be {0}", tomorrow);

        // WRITE THE DAY OF THE WEEK ON SCREEN
        Console.WriteLine("Today is {0}", DateTime.Today.DayOfWeek);

        // GET THE FIRST DAY OF THE YEAR
        Console.WriteLine("First day of 1995 is {0}", FirstDayOfYear(1995));

        // DISPLAY TIME STRUCTURE IN X'OCLOCK Y MINUTES AND Z SECONDS
        DateTime now = DateTime.Now;
        Console.WriteLine("Current Time: {0}:{1}:{2}", now.Hour, now.Minute, now.Second);

        // DAYS PASSED SINCE BIRTHDAY
        Console.WriteLine("Write your birthday in this format YYYY-MM-DD: ");

        try
        {
            // DateTime birthdayInput = DateTime.Parse(Console.ReadLine());
            // TimeSpan daysPassed = now.Subtract(birthdayInput);
            // Console.WriteLine("Days passed since your birthday: {0}", daysPassed);
        }
        catch (System.Exception)
        {
            Console.WriteLine("Error.");
            throw;
        }

        //--------------
        
        // THE NULL COALESCING OPERATOR "??"
        int? num3 = null;
        int? num4 = 4;
        
        // IF NUM5 IS NULL - ASSIGN 5
        int num5 = num3 ?? 5;
        System.Console.WriteLine(num5);
        
        // IF NUM6 IS NULL - ASSIGN 6
        int num6 = num4 ?? 5;
        System.Console.WriteLine(num6);

        // -----------------

        // MAIN (STRING[] ARGS)
        System.Console.WriteLine("Console App (Type 'help' for instructions): ");
        Console.Read();


        if (args[0] == "help")
        {
            System.Console.WriteLine("Use one of the following commands followed by 2 numbers.");
            System.Console.WriteLine("'add' to add the 2 numbers");
            System.Console.WriteLine("'sub' to subtract the 2 numbers");
        }
        else if (args.Length != 3)
        {
            System.Console.WriteLine("Incorrect number of arguments.");
        }
        else if (args[0] == "add" || args[0] == "sub")
        {
            int consoleNum1 = Convert.ToInt32(args[1]);
            int consoleNum2 = Convert.ToInt16(args[2]);

            if (args[0] == "add")
            {
                int result = consoleNum1 + consoleNum2;
            }
            else
            {
                int result = consoleNum1 - consoleNum2;
            }
        }
        
    }

}
