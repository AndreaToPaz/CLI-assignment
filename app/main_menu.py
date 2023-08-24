import click
import pandas as pd
from app.data_in import read_csv_file, dataframe_type
from app.visualizer.main_visualizer import visualization


#Help variables

#Array for menu operation options
option_array = ['Read-CSV-file', 
                'Read-CSV-file-types']

#Dataframe to work with
dataframe_to_visualize = pd.DataFrame 
dataframe_type_to_visualize = pd.DataFrame 

#end Help variables

#Option menu command
@click.command()
@click.option('--option_menu', 
              help = 'Enter your choice', 
              type = click.Choice(option_array))
@click.pass_context
def options(ctx, option_menu):
    click.echo(f"Processing option {option_menu}")
    
    # Store the value of the option in the context
    ctx.obj = {'option_menu': option_menu}

    if option_menu == option_array[0]: 
        
    # Reading CSV File 
    
        # Cacth CSV file path 
        csv_path = click.prompt('Enter path of the CSV file')
        ctx.obj['input_file_path'] = csv_path
        
        # Cacth CSV file data 
        dataframe_to_visualize = read_csv_file ( ctx.obj['input_file_path'] )

        # printing the data
        print ( dataframe_to_visualize )
        
    # Visualizer 

        #Cacth output directory
        Visualizer_output = click.prompt('Enter path of the output files')
        ctx.obj['output_file_path'] = Visualizer_output
        
        #Data Visualizer function 
        visualization( dataframe_to_visualize, ctx.obj['output_file_path'] )
        
    else:
        
        # Cacth CSV file path 
        csv_path = click.prompt('Enter path of the CSV file')
        ctx.obj['file_path'] = csv_path
        
        # Cacth CSV file data 
        dataframe_to_visualize = read_csv_file ( ctx.obj['file_path'] )
        dataframe_type_to_visualize = dataframe_type ( dataframe_to_visualize )
        
        # printing the data
        print ( dataframe_to_visualize )
        print ( dataframe_type_to_visualize )

def process_data(data):
    click.echo(f"Processing data: {data}")