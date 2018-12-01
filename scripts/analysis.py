# Talha A. Siddiqui, Nov 2018
#
# This script analyzes the data and makes predictions.
# It creates a decision tree classifier with ideal hyperparameters
# (maximum depth and minimum samples split). These hyperparameters
# are calculated over the 80% training data using 3-fold cross validation.
# The predictions are made on the 20% test data. Argument variables of
# the script are an input data file, a features importance data file, and
# a detailed data file containing all the data along with predictions and
# train/test label.
#
# Dependencies: argparse, pandas, numpy, sklearn.tree,
# sklearn.model_selection
#
# Usage: python analysis.py data_file importance_file detailed_file

# package import for parsing arguments
import argparse
import pandas as pd
import numpy as np
from sklearn import tree
from sklearn.model_selection import train_test_split, cross_val_score

# variable for parsing
parser = argparse.ArgumentParser()

# adding argument for input file
parser.add_argument('input_file')
parser.add_argument('importance_file')
parser.add_argument('output_file')
args = parser.parse_args()

def main():
    # read the data
    df = pd.read_csv(args.input_file)

    # specify feature and target columns
    feature_cols = df.columns.values[:-1]
    target = df.columns.values[-1]

    # create X and y
    X = df.loc[:, feature_cols]
    y = df.loc[:, target]

    # split the training data 80/20
    Xtrain, Xtest, ytrain, ytest = train_test_split(X,y,test_size=0.2)

    depth = best_depth(Xtrain, ytrain)
    split = best_samples_split(Xtrain, ytrain)

    model = tree.DecisionTreeClassifier(max_depth = depth, min_samples_split = split, random_state=42)
    model.fit(Xtrain,ytrain)

    results = pd.DataFrame(np.vstack((feature_cols, model.feature_importances_)))
    results = results.T
    results.columns = ['Features', 'Importance']
    results = results.sort_values(by='Importance', ascending=False)
    results = results[results['Importance']>0]
    results.to_csv(args.importance_file, index=False)

    # make predictions on test and training data
    predictions_test = model.predict(Xtest)
    predictions_train = model.predict(Xtrain)

    # combine all the data to save for output
    Xtr = Xtrain.copy()
    Xtr['Classification'] = ytrain
    Xte = Xtest.copy()
    Xte['Classification'] = ytest

    Xte['Predictions'] = predictions_test
    Xtr['Predictions'] = predictions_train

    Xtr['Type'] = "train"
    Xte['Type'] = "test"

    output = Xtr.append(other=Xte)
    output.to_csv(args.output_file, index=False)

def best_depth(X, y):
    '''
    ideitifies the best value for maximum depth in a decision tree
    by iterating over values 1 to 40 and returns value that gave the best
    average accuracy over 3-fold cross-validation
    '''
    depths = np.linspace(1, 40, 40, endpoint=True)
    train_accuracy = []

    for i in depths:
        model = tree.DecisionTreeClassifier(max_depth=i, random_state=42)
        avg_score = np.mean(cross_val_score(model, X, y, cv=3))
        train_accuracy.append(avg_score)

    return depths[np.argmax(train_accuracy)]

def best_samples_split(X, y):
    '''
    ideitifies the best value for minimum samples split in a decision tree
    by iterating over values 0.1 to 1.0 and returns value that gave the best
    average accuracy over 3-fold cross-validation
    '''
    splits = range(2,21,1)
    train_accuracy = []

    for i in splits:
        model = tree.DecisionTreeClassifier(min_samples_split=i, random_state=42)
        avg_score = np.mean(cross_val_score(model, X, y, cv=3))
        train_accuracy.append(avg_score)

    return splits[np.argmax(train_accuracy)]

# call main function
if __name__ == "__main__":
    main()
