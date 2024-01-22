
using MimeKit;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Net.Mail;
using System.Text;
using System.Threading.Tasks;

namespace Mentoring_Session
{
    internal class Program
    {

        static void Main(string[] args)
        {
            
            MailMessage mm = new MailMessage(
                "tech@ushunger.org", "patrick@ushunger.org", "TESTING", "Yayah!");

            // Set up the SMTP client
            using (var client = new SmtpClient("smtp.gmail.com", 587))
            {
                client.EnableSsl = true;
                // Authenticate with your email credentials
                // Replace these values with your actual email credentials
                string username = "tech@ushunger.org";
                string password = "mxhlizlvdrmgeqyn";

                // Create an instance of NetworkCredential
                ICredentialsByHost credentials = new NetworkCredential(username, password);

                client.Credentials = credentials;

                // Send the email
                client.Send(mm);

                // Disconnect from the SMTP server

            }

            Console.WriteLine("Email sent successfully.");
        }
    }
}
