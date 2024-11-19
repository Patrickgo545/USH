from data import ShippingData
from shipping_calculator import ShippingCalculator
import argparse
import json


# # DATAFRAME
# shipping_data = ShippingData()
# shipping_data.load_csv("./shipments_2023.csv","shipments")
# shipping_data.load_csv("./gas_averages - U.S._All_Grades_All_Formulations_Retail_Gasoline_Prices (2) (1).csv", "gas_averages")
# shipping_data.process_data()
# shipping_data.create_dataframe()
    
# shipping_calculator = ShippingCalculator(shipping_data.df)


def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Run the Shipping Calculator.")
    parser.add_argument("--shipments_csv", required=True, help="Path to the shipments CSV file.")
    parser.add_argument("--gas_csv", required=True, help="Path to the gas prices CSV file.")
    parser.add_argument("--output_json", required=False, default="results.json", help="Output JSON file for coefficients.")
    parser.add_argument("--output_pdf", required=False, default="Consolidated_Report.pdf", help="Output PDF report.")

    args = parser.parse_args()

    # Load and process data
    shipping_data = ShippingData()
    shipping_data.load_csv(args.shipments_csv, "shipments")
    shipping_data.load_csv(args.gas_csv, "gas_averages")
    shipping_data.process_data()
    shipping_data.create_dataframe()

    # Run the calculator
    shipping_calculator = ShippingCalculator(shipping_data.df)

    # Output the coefficients and intercepts as JSON
    results = {
        "shipmentCoefficients": shipping_calculator.coefficient_dictionary,
        "intercepts": shipping_calculator.intercept_dictionary
    }
    with open(args.output_json, "w") as f:
        json.dump(results, f, indent=4)
    print(f"Results saved to {args.output_json}")

    # Generate the consolidated PDF report
    shipping_calculator.generate_consolidated_report(output_file=args.output_pdf)
    print(f"PDF report saved to {args.output_pdf}")


if __name__ == "__main__":
    main()