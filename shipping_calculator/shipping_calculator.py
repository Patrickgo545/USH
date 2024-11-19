from regressor_module import Regressor
from data_report import ShipmentReport
from fpdf import FPDF

class ShippingCalculator:
    def __init__(self, df):
        self.df = df
        self.shipment_variables = {
            "LTL": ["pallets", "weight", "distance", "avg_gas_price"],
            "FTL": ["distance", "avg_gas_price"],
            "Box Truck": ["weight", "distance", "avg_gas_price"],
            "Sprinter Van": ["distance", "avg_gas_price"]
        }
        self.shipment_regressors = {}
        self.coefficient_dictionary =  {}
        self.intercept_dictionary = {}
        self.shipment_reports = {}
        self.extract_all_coefficients()
        self.Shipment_Reports()
        self.generate_consolidated_report()


    def extract_coefficients(self, shipment_type):
            if shipment_type not in self.shipment_variables:
                raise ValueError(f"Shipment type {shipment_type} not found in shipment_variables.")

            # Get the list of variables for the shipment type
            variable_list = self.shipment_variables[shipment_type]

            # Create and train the regressor
            regressor = Regressor(shipment_type, variable_list, self.df)
            regressor.TrainRegressor(shipment_type)
            self.intercept_dictionary[shipment_type] = regressor.intercept
            self.shipment_regressors[shipment_type] = regressor

            # Extract and return the coefficients
            coefficient_dict = regressor.results_dictionary
            self.coefficient_dictionary[shipment_type] = coefficient_dict  # Store coefficients in the class
            return coefficient_dict


    def extract_all_coefficients(self):
        for shipment_type in self.shipment_variables:
            self.extract_coefficients(shipment_type)
        return self.coefficient_dictionary
    
    
    def Shipment_Reports(self):
        for shipment_type, coefficients in self.coefficient_dictionary.items():
            self.shipment_reports[shipment_type] = ShipmentReport(shipment_type, coefficients, self.df, self.intercept_dictionary[shipment_type])

    
    def generate_consolidated_report(self, output_file="Consolidated_Report.pdf"):
        """
        Generates a consolidated PDF report containing graphs and metrics
        for all shipment types.
        """
        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        
        for shipment_type, report in self.shipment_reports.items():
            # Add a new page for each shipment type
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            
            # Add shipment type title
            pdf.cell(200, 10, txt=f"--- Report for {shipment_type} ---", ln=True, align='L')
            
            # Add metrics
            pdf.cell(200, 10, txt=f"Total Error: {report.total_error:.2f}", ln=True, align='L')
            pdf.cell(200, 10, txt=f"Mean Absolute Error: {report.mean_absolute_error:.2f}", ln=True, align='L')
            
            # Generate graph and save it as an image
            graph_file = f"{shipment_type}_graph.png"
            report.result_line_graph(output_file=graph_file)
            
            # Add the graph to the PDF
            pdf.image(graph_file, x=10, y=50, w=190)  # Adjust position and size as needed
        
        # Save the PDF
        pdf.output(output_file)