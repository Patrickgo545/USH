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
    public class CSVManager
    {
        // TARGET CSV
        public string csvFilePath = Path.Combine(AppDomain.CurrentDomain.BaseDirectory, "gas_averages - U.S._All_Grades_All_Formulations_Retail_Gasoline_Prices (2) (1).csv");

        //List<string> _test = ReadCsv<string>(csvFilePath);

    }

    // LIST CSV COLUMNS
    //List<string> GetCsvColumns(string csvFilePath)
    //{
    //    List<string> headers = new List<string>();

    //    using (var reader = new StreamReader(csvFilePath))
    //    using (var csv = new CsvReader(reader, new CsvHelper.Configuration.CsvConfiguration(CultureInfo.InvariantCulture)))
    //    {
    //        csv.Read();
    //        csv.ReadHeader();

    //        foreach (var header in csv.Context.HeaderRecord)
    //        {
    //            headers.Add(header);
    //        }
    //    }

    //    return headers;
    //}

}
