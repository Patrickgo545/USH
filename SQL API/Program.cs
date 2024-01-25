using Microsoft.Data.SqlClient;
using System;
using System.IO;

namespace SQL_API
{
    // PING DATABASE & ESTABLISH A CONNECTION
    public class DatabasePinger
    {
        private readonly String _connectionString;
        private object connection;

        public DatabasePinger(string connectionString)
        {
            _connectionString = connectionString;
        }

        public bool PingServer()
        {
            SqlConnection connection = new SqlConnection(_connectionString);
            {
                Console.WriteLine("Establishing Connection...");

                try
                {
                    connection.Open();
                    return true;
                }
                catch (SqlException ex)
                {
                    Console.WriteLine($"Error connecting to the database: {ex.Message}");
                    return false;
                }

            }
        }

    }

    internal class Program
    {
        private static SqlConnection connection;

        static void Main(string[] args)
        {
            // PING SERVER - TEST TO MAKE SURE CONNECTION CAN BE ESTABLISHED
            string connectionString = "Data Source=localhost;Initial Catalog=api_test;Integrated Security=True;Connect Timeout=30;Encrypt=True;Trust Server Certificate=True;Application Intent=ReadWrite;Multi Subnet Failover=False";

            DatabasePinger databasePinger = new DatabasePinger(connectionString);
            bool isDatabaseReachable = databasePinger.PingServer();

            if (isDatabaseReachable)
            {
                // CONNECTION WITH SERVER WORKS
                Console.WriteLine("Success");
                Console.WriteLine("-------------");

                using (SqlConnection connection = new SqlConnection(connectionString))
                {
                    // SQL QUERY - LAST ROW OF DB
                    string dataBase = "[api_test].[dbo].[Table_1]";
                    string sqlQuery = $"SELECT TOP 1 * FROM {dataBase} ORDER BY test DESC";


                    // READ FROM DB
                    using (SqlCommand command = new SqlCommand(sqlQuery, connection))
                    {
                        connection.Open();

                        using (SqlDataReader reader = command.ExecuteReader())
                        {
                            if (reader.Read())
                            {
                                string columnValue = reader["test"].ToString();

                                Console.WriteLine("Read table");
                                Console.WriteLine($"Previous row value: {columnValue}");
                                Console.WriteLine("-------------");
                            }

                            else
                            {
                                Console.WriteLine("No rows found in table");
                            }
                        }
                    }


                    string csvFilePath = "gas_averages - U.S._All_Grades_All_Formulations_Retail_Gasoline_Prices (2) (1).csv";
                    // Read CSV
                    using (var reader = new StreamReader(csvFilePath))
                    {
                        do
                        {
                            var line = reader.ReadLine();

                            Console.WriteLine(line);
                        } while (reader.EndOfStream == false);
                    }

                    // INSERT INTO DB
                    string tableName = "Table_1";
                    string columnName1 = "date";
                    string columnName2 = "avg_gas_price";
                    string currentDateTime = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss");

                    string sqlInsert = $"INSERT INTO {tableName} ({columnName1}, {columnName2}) VALUES ('{currentDateTime}')";
                    using (SqlCommand command = new SqlCommand(sqlInsert, connection))
                    
                    {

                        using (SqlCommand _command = new SqlCommand (sqlInsert, connection))
                        {
                            // CHECK IF ROW WAS ADDED SUCCESSFULLY
                            int rowsAffected = command.ExecuteNonQuery();

                            if (rowsAffected > 0)
                            {
                                Console.WriteLine("Insert Into Table");
                                Console.WriteLine($"{currentDateTime}");
                            }    
                            else
                            {
                                Console.WriteLine("Failed to add a new row.");
                            }    
                        }
                    }

                }

            }
            else
            {
                // Handle the case when the database is not reachable...
                Console.WriteLine("Something went wrong");
            }

            Console.ReadKey();
        }
    }
}
