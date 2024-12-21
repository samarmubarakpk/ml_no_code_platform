from sklearn.preprocessing import StandardScaler, MinMaxScaler
import pandas as pd
import numpy as np

class DataPreprocessor:
    def __init__(self):
        self.scaler = None
        self.scaling_method = None
        self.fitted = False

    def fit_transform(self, data, method='standard', columns=None):
        """
        Fit and transform data using specified scaling method.
        
        Parameters:
        data (pd.DataFrame): Input dataset
        method (str): Scaling method ('standard' or 'minmax')
        columns (list): Columns to scale. If None, scales all numeric columns
        """
        self.scaling_method = method
        
        # Select numeric columns if none specified
        if columns is None:
            columns = data.select_dtypes(include=[np.number]).columns
        
        # Create scaler based on method
        if method == 'standard':
            self.scaler = StandardScaler()
        elif method == 'minmax':
            self.scaler = MinMaxScaler()
        else:
            raise ValueError("Method must be 'standard' or 'minmax'")

        # Fit and transform
        scaled_data = data.copy()
        scaled_data[columns] = self.scaler.fit_transform(data[columns])
        self.fitted = True
        
        return scaled_data

    def transform(self, data):
        """Transform new data using fitted scaler"""
        if not self.fitted:
            raise ValueError("Preprocessor must be fitted before transform")
        
        scaled_data = data.copy()
        numeric_cols = data.select_dtypes(include=[np.number]).columns
        scaled_data[numeric_cols] = self.scaler.transform(data[numeric_cols])
        
        return scaled_data