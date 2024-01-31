namespace _11_AdvancedC_Topics;

class Program
{
    // ENUMS (Enumerations) - Define a set of names constants
    enum Months { Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec }
    
    static void Main(string[] args)
    {
        Months jan = Months.Jan;
        Months a = Months.Jan;

        Console.WriteLine(jan == a);
        Console.WriteLine(Months.Feb);
        Console.WriteLine((int)Months.Dec);
        
    }
}
