using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Mentoring_Session_1._30._24
{// LINQ , ET , EVENTBRITE REST API
    public class Dog : Animal 
    {
        private string _name;
        private string _hairColor;
        private string _sound;

        public Dog(string name, string hairColor, string sound) 
        {
            this._name = name;
            this._hairColor = hairColor;
            this._sound = sound;
        }
        public override string ToString()
        {
            return $"I am {_name} & my coat color is {_hairColor} - {_sound}";
        }

        public override string MakeSound()
        {
            return _sound;
        }
    }
    public class Animal : Object
    {
        public Animal() { }
        public override string ToString()
        {
            return "I am an animal";
        }

        public virtual string MakeSound()
        {
            return "Moo";
        }

    }
    internal class Program
    {
        static void Main(string[] args)
        {
            // TEST CLASSES
            Dog gizmo = new Dog("Gizmo", "Black", "Whine");
            Console.WriteLine(gizmo.ToString());
            Console.WriteLine(gizmo.MakeSound());

            Dog spot = new Dog("Spot", "Purple", "Woof");
            Console.WriteLine(spot.ToString());
            Console.WriteLine(spot.MakeSound());

            //Console.ReadKey();


            // PULL TEST TABLE
            using (var db = new TestEntities()) 
            {
                var records = db.testTable.ToList();

                Console.WriteLine(db);

                foreach (var record in records)
                { 
                    Console.WriteLine(record.Name + " " + record.Gender);
                }

                //Console.WriteLine(records);
                //Console.ReadKey();
            }
            Console.WriteLine("---------------");


            // PULL TEST TABLE - SEPARATE GENDERS
            using (var db = new TestEntities())
            {
                Console.WriteLine("\nSeparating M / F");
                var records = db.testTable.ToList();
                var males = db.testTable.Where(person => person.Gender == "M").ToList();
                var females = db.testTable.Where(person => person.Gender == "F").ToList();

                // PRINT MALES
                Console.WriteLine("\nMale:");
                foreach (var person in males)
                {
                    Console.WriteLine(person.Name);
                }

                Console.WriteLine("---------");

                // PRINT FEMALES
                Console.WriteLine("\nFemale:");
                foreach (var person in females)
                {
                    Console.WriteLine(person.Name);
                }
                Console.WriteLine("------------");
                Console.ReadKey();
            }

            // ADD NEW PERSON INTO DATABASE
            using (var db = new TestEntities())
            {
                testTable person = testTable.GeneratePerson();
                db.testTable.Add(person);

                db.SaveChanges();
                
                // INSPECT DATABASE
                var records = db.testTable.ToList();
                foreach (var record in records)
                {
                    Console.WriteLine($"{record.Name} {record.Gender}");
                }

                Console.ReadKey();
            }
        }
    }
}
