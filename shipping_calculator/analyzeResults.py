import papermill as pm


# Loop through each shipment type and generate a report
for shipment_type, variables in shipment_variables.items():
    # Generate a notebook for each shipment type
    pm.execute_notebook(
       'template_notebook.ipynb',  # Template notebook
       f'{shipment_type}_report.ipynb',  # Output notebook
       parameters=dict(shipment_type=shipment_type, variables=variables)  # Parameters to pass
    )