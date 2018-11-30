import argparse
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

"""This script visualizes the distributions of training data features using histograms to identify better predictors from our data set"""

# variable for parsing
parser = argparse.ArgumentParser()

# adding argument for input file
parser.add_argument('input_file')
parser.add_argument('output_file')
args = parser.parse_args()

def main():

    # read the data
    data = pd.read_csv(args.input_file)

    # split the data
    data1 = data[data.Classification==1]
    data2 = data[data.Classification==2]

    # Visualize the features
    feature_cols = data.columns.values[:-1]
    number = range
    for idx,item in enumerate(feature_cols):
        sns_data1 = sns.distplot(data1[item].dropna(),kde = False, label="Healthy controls")
        sns_data2 = sns.distplot(data2[item].dropna(),kde = False, label="Patient")
        sns_data1.set_title(item)
        sns_data1.set_ylabel("Count")
        sns_data1.set_xlabel(item)
        plt.legend()
        plt.savefig(args.output_file+str(idx+1)+'.png')
        plt.close()

# call main function
if __name__ == "__main__":
    main()
