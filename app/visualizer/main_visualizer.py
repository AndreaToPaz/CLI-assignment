import pandas as pd
from app.visualizer.visualizer_function import generate_visualizations, generate_scatter_matrix, generate_html_report


def visualization( dataframe_to_visualize : pd.DataFrame, output_dir : str,) :
    """
    Purpose: call each type of visualization and the HTML report
    """
    # Function to generate visualizations for each column
    generate_visualizations(dataframe_to_visualize, output_dir)

    # Function to generate a scatter matrix for numeric columns
    generate_scatter_matrix(dataframe_to_visualize, output_dir)
        
    # Function to generate an HTML report
    generate_html_report(dataframe_to_visualize, output_dir)
# end def