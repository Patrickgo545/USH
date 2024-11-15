import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import matplotlib.pyplot as plt
import seaborn as sns
from fpdf import FPDF

class ShipmentReport:
    def __init__(self, shipment_type, coefficient_dictionary, df):
        self.shipment_type = shipment_type
        self.coefficients = coefficient_dictionary
        self.df = df
        self.filtered_df = None
        self.total_error = None
        self.mean_absolute_error = None
        self.interpret_coefficients()
        self.Calculate_Metrics()
        
        

    def interpret_coefficients(self):
        # Filter the DataFrame for the shipment type
        self.filtered_df = self.df[self.df['shipmentType'] == self.shipment_type].copy()

        # Calculate predicted prices
        self.filtered_df['predicted_price'] = self.filtered_df.apply(
            lambda row: sum(row[variable] * coef for variable, coef in self.coefficients.items()),
            axis=1
        )



    def Calculate_Metrics(self):
        self.total_error = sum(self.filtered_df['predicted_price']) - sum(self.filtered_df['quote']) 
        self.mean_absolute_error = metrics.mean_absolute_error(self.filtered_df['quote'], self.filtered_df['predicted_price'])
        
        


    def result_line_graph(self, output_file=None):
        """Plots the actual vs. predicted prices as a line graph."""
        if self.filtered_df is None:
            raise ValueError("Run interpret_coefficients() before calling result_line_graph().")

        # Plot results
        plt.figure(figsize=(12, 6))
        plt.plot(self.filtered_df.index, self.filtered_df['quote'], label='Actual')
        plt.plot(self.filtered_df.index, self.filtered_df['predicted_price'], label='Predicted')

        plt.xlabel('Index')
        plt.ylabel('Price ($)')
        plt.title(f'MACHINE LEARNING CALCULATOR: {self.shipment_type}')
        plt.legend()
        plt.grid(axis='y', linestyle='-', linewidth='0.5', color='gray', alpha=0.75)

        # Save graph to file if output_file is provided
        if output_file:
            plt.savefig(output_file)
            print(f"Graph saved to {output_file}")

    def generate_report(self, output_file=None):

        # Save graph as an image
        graph_file = f"{self.shipment_type}_graph.png"
        self.result_line_graph(output_file=graph_file)

        # Generate PDF report
        if output_file:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)

            # Add metrics to PDF
            pdf.cell(200, 10, txt=f"--- Report for {self.shipment_type} ---", ln=True, align='L')
            pdf.cell(200, 10, txt=f"Total Error: {self.total_error:.2f}", ln=True, align='L')
            pdf.cell(200, 10, txt=f"Mean Absolute Error: {self.mean_absolute_error:.2f}", ln=True, align='L')

            # Add the graph to the PDF
            pdf.image(graph_file, x=10, y=50, w=190)  # Adjust dimensions as needed

            # Save PDF
            pdf.output(output_file)

# test = ShipmentTypePredictor('LTL', result['LTL'], df=df)
# print(test.total_error, test.mean_absolute_error)
# test.generate_report("LTL_Report.pdf")
# test.result_line_graph()