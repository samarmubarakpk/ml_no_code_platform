import pandas as pd
import numpy as np

def validate_dataset(data):
    """Validate input dataset"""
    if not isinstance(data, pd.DataFrame):
        raise ValueError("Data must be a pandas DataFrame")
    
    if data.empty:
        raise ValueError("DataFrame is empty")
    
    if not any(data.select_dtypes(include=[np.number]).columns):
        raise ValueError("DataFrame must contain at least one numeric column")

    return True
