using System;

namespace MyApp // Note: actual namespace depends on the project name.
{
    // CREATE CAT CLASS
    class Cat
    {
        public string name;
        public int age;

        public void Meow()
        {
            Console.WriteLine($"{this.name} - Meow!");
        }
    }

    // CREATE WIZARD CLASS
    class Wizard
    {
        // CLASS ATTRIBUTES
        public string name;
        public string favoriteSpell;
        private int spellSlots;
        private float experience;

        // STATIC - SHARED BY ALL INSTANCES
        public static int Count;

        // CLASS CONSTRUCTORS
        public Wizard(string _name, string _favoriteSpell)
        {
            name = _name;
            favoriteSpell = _favoriteSpell;
            spellSlots = 2;
            experience = 0;
            Count++;
        }

        public void CastSpell()
        {
            // SPELL SLOT STATUS
            Console.WriteLine($"Spell Slots: {this.spellSlots}");

            if (spellSlots > 0)
            {
                Console.WriteLine($"{this.name} casts {favoriteSpell}");
                spellSlots -= 1;
                experience += 0.3f;
            }

            else
            {
                Console.WriteLine("Out of Spell Slots. Time for melee");
            }
            
            Console.WriteLine("------------------");
        }

        // METHOD - LET WIZARD RESTORE SPELL SLOTS
        public void RestoreSpellSlots()
        {
            Console.WriteLine($"{name} is resting...");
            spellSlots += 1;

            // DISPLAY SPELL SLOTS
            Console.WriteLine($"Spell Slots: {spellSlots}");
        }
    }
    internal class Program
    {
        static void Main(string[] args)
        {
            // CREATE CAT OBJECTS
            Cat cat01 = new Cat();
            cat01.name = "Cat Stevens";
            cat01.age = 1;
            cat01.Meow();

            Cat cat02 = new Cat();
            cat02.name = "Meowly Cyrus";
            cat02.age = 12;
            cat02.Meow();

            Console.WriteLine("------------------");

            Wizard wizard01 = new Wizard("Parry Hopper", "Unexpecto Patronum");
            // wizard01.name = "Parry Hopper";
            // wizard01.favoriteSpell = "Unexpecto Patronum";
            // wizard01.spellSlots = 2;
            // wizard01.experience = 0f;

            wizard01.CastSpell();
            wizard01.CastSpell();
            wizard01.CastSpell();
            wizard01.RestoreSpellSlots();

            Wizard wizard02 = new Wizard("Gandalf the Cray", "The Force");
            wizard02.CastSpell();

            Console.WriteLine("---------------");
            
            Console.WriteLine($"Number of Wizards on the board {Wizard.Count}");
        }
    }
}