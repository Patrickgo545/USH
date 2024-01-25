using CsvHelper;
using System;
using System.Collections.Generic;
using System.Globalization;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Reading_HTML
{
    internal class Program
    {

        static void Main(string[] args)
        {
            // Replace "example.csv" with the actual CSV file path
            string csvFilePath = "gas_averages - U.S._All_Grades_All_Formulations_Retail_Gasoline_Prices (2) (1).csv";

            using (var reader = new StreamReader(csvFilePath))
            {
                do
                {
                    var line = reader.ReadLine();
                    var values = line.Split(',');

                    Console.WriteLine($"Date: {values[0]}, Cost: {values[1]}");
                } while (reader.EndOfStream == false);




            }
            Console.ReadKey();

        }
    }
}
