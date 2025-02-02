import os
import pandas as pd
from utils import pylog

class FileExcel:
    def __init__(self):
        pass
    
    def search_excel_file(self, *, path_file:str):
        """
        Check if the Excel file exists.

        Args:
            path_file (str): The path to the Excel file.

        Returns:
            bool: True if the file exists, False otherwise.

        Raises:
            None
        """
        if os.path.isfile(path_file):
            pylog(f"The file '{path_file}' exists.")
            return True
        else:
            pylog(f"The file '{path_file}' does not exist.")
            return False

    def open_excel_file(self, *, path_file:str):
        """
        Open the Excel file and return a DataFrame.

        Args:
            path_file (str): The path to the Excel file.

        Returns:
            pd.DataFrame: The DataFrame containing the Excel file data.

        Raises:
            Exception: If the file cannot be opened.
        """
        try:
            dataframe = pd.read_excel(path_file, index_col=False)
            return dataframe
        except Exception as error:
            pylog(f"Failed to open Excel file: {error}")
            raise

    def get_column_names(self, path_file:str):
        """
        Get the column names from the Excel file.

        Args:
            path_file (str): The path to the Excel file.

        Returns:
            list: A list of column names.

        Raises:
            Exception: If the column names cannot be retrieved.
        """
        try:
            dataframe = pd.read_excel(path_file, index_col=False)
            fields    = dataframe.columns.tolist()
            return fields
        except Exception as error:
            pylog(f"Failed to get column names: {error}")
            raise

    def convert_to_dict(self, *, path_file:str, type_orient:str="records"):
        """
        Convert the Excel file to a dictionary.

        Args:
            path_file (str): The path to the Excel file.
            type_orient (str, optional): The orientation of the dictionary. Defaults to "records".

        Returns:
            dict: The dictionary representation of the Excel file.

        Raises:
            Exception: If the file cannot be converted to a dictionary.
        """
        try:
            dataframe_format = pd.read_excel(path_file, index_col=False).to_dict(orient=type_orient)
            return dataframe_format
        except Exception as error:
            pylog(f"Failed to convert to dictionary: {error}")
            raise
