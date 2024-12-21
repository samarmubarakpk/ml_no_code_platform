import pandas as pd
from sklearn.model_selection import train_test_split


class DataSplitter:
    def __init__(self):
        self.X_train = None
        self.X_val = None
        self.X_test = None
        self.y_train = None
        self.y_val = None
        self.y_test = None

    def split_data(self, data, target_column, train_size=0.7, val_size=0.15):
        """
        Split data into train, validation and test sets.
        
        Parameters:
        data (pd.DataFrame): Input dataset
        target_column (str): Name of the target column
        train_size (float): Proportion of data for training
        val_size (float): Proportion of data for validation
        """
        # Separate features and target
        X = data.drop(target_column, axis=1)
        y = data[target_column]

        # First split: separate training set
        X_temp, self.X_test, y_temp, self.y_test = train_test_split(
            X, y, test_size=1-train_size, random_state=42
        )

        # Second split: separate validation set from remaining data
        val_adjusted_size = val_size / (train_size)
        self.X_train, self.X_val, self.y_train, self.y_val = train_test_split(
            X_temp, y_temp, test_size=val_adjusted_size, random_state=42
        )

        return {
            'X_train': self.X_train, 'y_train': self.y_train,
            'X_val': self.X_val, 'y_val': self.y_val,
            'X_test': self.X_test, 'y_test': self.y_test
        }

    def get_split_sizes(self):
        """Return the sizes of all splits"""
        if self.X_train is None:
            return None
        
        return {
            'train_size': len(self.X_train),
            'val_size': len(self.X_val),
            'test_size': len(self.X_test)
        }