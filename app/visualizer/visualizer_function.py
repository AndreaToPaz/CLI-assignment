import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix

# Function to generate visualizations for each column
def generate_visualizations(data, output_dir):
    for column in data.columns:
        plt.figure(figsize=(10, 6))
        
        if pd.api.types.is_numeric_dtype(data[column]):
            # Histogram for numeric columns
            data[column].plot(kind='hist', title=f'Histogram of {column}')
        elif pd.api.types.is_categorical_dtype(data[column]):
            # Bar plot for categorical columns
            data[column].value_counts().plot(kind='bar', title=f'Bar Plot of {column}')
        else:
            # Skip non-numeric and non-categorical columns
            continue
        
        plt.savefig(f'{output_dir}/{column}_visualization.png')
        plt.close()

# Function to generate a scatter matrix for numeric columns
def generate_scatter_matrix(data, output_dir):
    numeric_columns = data.select_dtypes(include=['number'])
    scatter_matrix(numeric_columns, figsize=(12, 8))
    plt.savefig(f'{output_dir}/scatter_matrix.png')
    plt.close()
    
# Function to generate an HTML report
def generate_html_report(data, output_dir):
    report_content = '<html><body>'
    
    for column in data.columns:
        report_content += f'<h2>{column}</h2>'
        report_content += f'<img src="{column}_visualization.png"><br>'
    
    report_content += f'<h2>Scatter Matrix</h2>'
    report_content += f'<img src="scatter_matrix.png"><br>'
    
    report_content += '</body></html>'
    
    with open(f'{output_dir}/report.html', 'w') as f:
        f.write(report_content)
