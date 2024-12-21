import sys
from src.components.data_splitter import DataSplitter
from src.components.data_preprocessor import DataPreprocessor
from src.utils.validation import validate_dataset
import pandas as pd



def main():
    # Example usage
    # Load your dataset
    data = pd.read_csv('your_dataset.csv')  # Replace with your dataset
    
    try:
        # Validate dataset
        validate_dataset(data)
        
        # Initialize components
        splitter = DataSplitter()
        preprocessor = DataPreprocessor()
        
        # Preprocess data
        scaled_data = preprocessor.fit_transform(
            data,
            method='standard',
            columns=['feature1', 'feature2']  # Replace with your feature columns
        )
        
        # Split data
        splits = splitter.split_data(
            scaled_data,
            target_column='target',  # Replace with your target column
            train_size=0.7,
            val_size=0.15
        )
        
        # Get split sizes
        split_sizes = splitter.get_split_sizes()
        print("Dataset splits:", split_sizes)
        
        # Access individual splits
        X_train = splits['X_train']
        y_train = splits['y_train']
        # ... access other splits as needed
        
    except Exception as e:
        print(f"Error processing dataset: {str(e)}")

if __name__ == "__main__":
    main()



