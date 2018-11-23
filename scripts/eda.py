import argparse
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

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
    feature_cols = data.iloc[:,:9]
    for i in feature_cols:
        sns_data1 = sns.distplot(data1[i].dropna(),kde = False)
        sns_data2 = sns.distplot(data2[i].dropna(),kde = False)
        sns_data1.set_title(i)
        sns_data1.set_ylabel("Count")
        sns_data1.set_xlabel(i)
        plt.savefig('plot'+str(i)+'.png')
        plt.close()

# call main function
if __name__ == "__main__":
    main()
