# Talha A. Siddiqui, Nov 2018
#
# This script visualizes the results of fetures importance based on the
# decision tree classifier in analysis.py. Argument variables of
# the script are a features importance data file, and a result png.
#
# Dependencies: argparse, pandas, numpy, matplotlib, seaborn
#
# Usage: python plot.py importance_file results.png

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
    fig = output.get_figure()
    fig.savefig(args.output_file)

# call main function
if __name__ == "__main__":
    main()
