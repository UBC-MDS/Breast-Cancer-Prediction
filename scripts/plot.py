# package import for parsing arguments
import argparse
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# variable for parsing
parser = argparse.ArgumentParser()

# adding argument for input file
parser.add_argument('input_file')
parser.add_argument('output_file')
args = parser.parse_args()

def main():
    # read the data
    df = pd.read_csv(args.input_file)

    # produce a figure of feature importance
    output = sns.barplot(df['Features'], df['Importance'], palette='Blues_d')
    output.set_xticklabels(output.get_xticklabels(), rotation=45)
    fig = output.get_figure()
    fig.savefig(args.output_file)

# call main function
if __name__ == "__main__":
    main()
