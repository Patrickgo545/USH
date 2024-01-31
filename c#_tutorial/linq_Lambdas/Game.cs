using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace linq_Lambdas
{
    public class Game : Object
    {
        private string _name;
        private double _steamScore;

        // CONSTRUCTOR
        public Game(string name, double steamScore)
        {
            this._name = name;
            this._steamScore = steamScore;
        }

        // GIVING ACCESS TO PRIVATE FIELDS 
        public string Name
        {
            get { return _name; }
            set { _name = value; }
        }

        public double SteamScore
        {
            get { return _steamScore; }
            set { _steamScore = value; }
        }
    }
}