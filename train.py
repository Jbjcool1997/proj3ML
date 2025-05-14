import argparse
import sklearn
from sklearn.linear_model import LogisticRegression
import os
import numpy as np
from sklearn.metrics import mean_squared_error
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
import pandas as pd
from azureml.core.run import Run
from azureml.data.dataset_factory import TabularDatasetFactory

def clean_data(data):
    #Cleaning data with dropna, expected value from outcome should be 1 and 0, in otherwords only numbers.
    x_df = data.dropna()
    y_df = x_df['Outcome']
    return x_df, y_df

def main():
    # Add arguments to script
    parser = argparse.ArgumentParser()

    parser.add_argument('--C', type=float, default=1.0, help="Inverse of regularization strength. Smaller values cause stronger regularization")
    parser.add_argument('--max_iter', type=int, default=100, help="Maximum number of iterations to converge")

    args = parser.parse_args()

    run = Run.get_context()

    run.log("Regularization Strength:", float(args.C))
    run.log("Max iterations:", int(args.max_iter))

    # TODO: Create TabularDataset using TabularDatasetFactory
    # Data is located at:
    ds = pd.read_csv('heart_failure_clinical_records_dataset')

    
    x, y = clean_data(ds)

    # TODO: Split data into train and test sets.

    x_train, x_test, y_train, y_test = train_test_split(x, y)

    model = LogisticRegression(C=args.C, max_iter=args.max_iter).fit(x_train, y_train)

    accuracy = model.score(x_test, y_test)

    run.log("Accuracy", float(accuracy))

    #save the model
    os.makedirs('outputs', exist_ok=True)
    joblib.dump(model, 'outputs/model.joblib')

if __name__ == '__main__':
    main()
