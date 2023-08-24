import pandas as pd

def read_csv_file( csv_path ) -> pd.DataFrame:
    """
    Purpose: read a csv file using its path
    """
    try:
        # Reading csv file from csv_path
        df = pd.read_csv( csv_path, sep=',' )
        # saving the DataFrame data in ctx (context)
        ctx = df
        # returning the read DataFrame 
        return ( df )
    except Exception as e:
        # printing exception
        print( f"Error: { e }" )
# end def

def dataframe_type( input_df : pd.DataFrame) -> pd.DataFrame :
    """
    Purpose: Read a CSV file to determine
             the value type of each column 
    """
    input_df_types = pd.DataFrame
    #detecting each column type and 
    input_df_types = input_df.dtypes.reset_index()
    #saving each column typem in input_df_types
    input_df_types.columns = ['Column Name', 'Data Type']
    return input_df_types
# end def
