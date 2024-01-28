using Microsoft.Data.SqlClient;
using Microsoft.Identity.Client;
using System;
using System.IO;
using System.Linq;

namespace SQL_API
{
    // PING DATABASE & ESTABLISH A CONNECTION
    //public class DatabasePinger
    //{
    //    private readonly String _connectionString;
    //    private object connection;

    //    public DatabasePinger(string connectionString)
    //    {
    //        _connectionString = connectionString;
    //    }

    //    public bool PingServer()
    //    {
    //        SqlConnection connection = new SqlConnection(_connectionString);
    //        {
    //            Console.WriteLine("Establishing Connection...");

    //            try
    //            {
    //                connection.Open();
    //                Console.WriteLine("Connection Established.");
    //                return true;
    //            }
    //            catch (SqlException ex)
    //            {
    //                Console.WriteLine($"Error connecting to the database: {ex.Message}");
    //                return false;
    //            }

    //        }
    //    }

    //}

    internal class Program
    {
        private static SqlConnection connection;

        static void Main()
        {
            // PING SERVER - TEST TO MAKE SURE CONNECTION CAN BE ESTABLISHED
            //string connectionString = "Data Source=localhost;Initial Catalog=api_test;Integrated Security=True;Connect Timeout=30;Encrypt=True;Trust Server Certificate=True;Application Intent=ReadWrite;Multi Subnet Failover=False";

            //DatabasePinger databasePinger = new DatabasePinger(connectionString);
            //bool isDatabaseReachable = databasePinger.PingServer();

            //if (isDatabaseReachable)
            //{
            //    // CONNECTION WITH SERVER WORKS
            //    Console.WriteLine("Success");
            //    Console.WriteLine("-------------");

            //    using (SqlConnection connection = new SqlConnection(connectionString))
            //    {
            //        // SQL QUERY - LAST ROW OF DB
            //        //string dataBase = "[api_test].[dbo].[Table_1]";
            //        string dataBase = "[testDatabase].[dbo].[testTable]";
            //        string sqlQuery = $"SELECT TOP 1 * FROM {dataBase} ORDER BY test DESC";


            // READ FROM DB
            //using (SqlCommand command = new SqlCommand(sqlQuery, connection))
            //{
            //    connection.Open();

            //    using (SqlDataReader reader = command.ExecuteReader())
            //    {
            //        if (reader.Read())
            //        {
            //            string columnValue = reader["dates"].ToString();

            //            Console.WriteLine("Read table");
            //            Console.WriteLine($"Previous row value: {columnValue}");
            //            Console.WriteLine("-------------");
            //        }

            //        else
            //        {
            //            Console.WriteLine("No rows found in table");
            //        }
            //    }
            //}

            //string connectionString = "Data Source=DESKTOP-7KJIU1U;Integrated Security=True;Connect Timeout=30;Encrypt=True;Trust Server Certificate=True;Application Intent=ReadWrite;Multi Subnet Failover=False";
            //using (SqlConnection connection = new SqlConnection(connectionString)
            //{
            //    connection.Open();
            //}

            //// Read CSV
            //string csvFilePath = "gas_averages - U.S._All_Grades_All_Formulations_Retail_Gasoline_Prices (2) (1).csv";
            //using (var reader = new StreamReader(csvFilePath))
            //{

            //    do
            //    {

            //        var line = reader.ReadLine();
            //        var values = line.Split(',');

            //        string tableName = "testTable";
            //        string columnValue1 = values[0];
            //        string columnValue2 = values[1];
            //        string sqlInsert = $"INSERT INTO {tableName} (dates, avg_gas_price) VALUES ('{columnValue1}', {columnValue2})";


            //        using (SqlCommand command = new SqlCommand(sqlInsert)) ;


            //        Console.WriteLine(sqlInsert);
            //    } while (reader.EndOfStream == false);
            //}
            {
                // SET UP CONNECTION STRINGS
                string connectionString = "Data Source=DESKTOP-7KJIU1U;Initial Catalog=testDatabase;Integrated Security=True;Connect Timeout=30;Encrypt=True;Trust Server Certificate=True;Application Intent=ReadWrite;Multi Subnet Failover=False";
                string csvFilePath = "gas_averages - U.S._All_Grades_All_Formulations_Retail_Gasoline_Prices (2) (1).csv";

                // CONNECT TO DB
                try
                {
                    using (SqlConnection connection = new SqlConnection(connectionString))
                    {
                        connection.Open();

                        // CSV
                        using (var reader = new StreamReader(csvFilePath))
                        {
                            string headerLine = reader.ReadLine(); // EXCLUDING HEADER

                            while (!reader.EndOfStream)
                            {
                                var line = reader.ReadLine();
                                var values = line.Split(',');

                                //string tableName = "testTable";
                                string columnValue1 = values[0];
                                string columnValue2 = values[1];
                                double price = double.Parse(values[1]);


                                // Execute the SQL command
                                using (var orm = new testDatabaseEntities())
                                {
                                    var found = orm.testTable.Where(x=>x.dates == columnValue1 && x.avg_gas_price == price).FirstOrDefault();

                                    if (found == null) 
                                    { 
                                        testTable r = new testTable() { dates = columnValue1, avg_gas_price = price };
                                        orm.testTable.Add(r);
                                        orm.SaveChanges();
                                     }
                                    //else
                                    //{
                                    //    found.avg_gas_price = found.avg_gas_price * 10;
                                    //    orm.SaveChanges();
                                    //}

                                    //command.ExecuteNonQuery();
                                }
                            }
                        }

                    }
                }
                catch (Exception ex)
                {
                    //Console.WriteLine(ex.ToString());
                }
            }
        }
    }
}


//{
//    try
//    {
//        connection.Open();
//        int rowsAffected = command.ExecuteNonQuery();
//        Console.WriteLine($"Rows affected: {rowsAffected}");
//    }
//    catch (Exception ex)
//    {
//        Console.WriteLine("Error executing SQL command: " + ex.Message);
//    }
//}







// INSERT INTO DB
//string tableName = "Table_1";
//string columnName1 = "date";
//string columnName2 = "avg_gas_price";

//string sqlInsert = $"INSERT INTO {tableName} ({columnName1}, {columnName2}) VALUES ('{0}')";



//using (SqlCommand command = new SqlCommand(sqlInsert, connection))

//{


//using (SqlCommand _command = new SqlCommand (sqlInsert, connection))
//{
//    // CHECK IF ROW WAS ADDED SUCCESSFULLY
//    int rowsAffected = command.ExecuteNonQuery();

//    if (rowsAffected > 0)
//    {
//        Console.WriteLine("Insert Into Table");
//        Console.WriteLine($"{currentDateTime}");
//    }    
//    else
//    {
//        Console.WriteLine("Failed to add a new row.");
//    }    
//}
//}

//}

//            }
//            else
//{
//    // Handle the case when the database is not reachable...
//    Console.WriteLine("Something went wrong");
//}

//Console.ReadKey();
//        }
//    }
//}
