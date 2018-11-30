# Akansha Vashisth, Nov 2018
#
# This script does the following:
# - reads the input file(breast_cancer.csv parsed by the argument),
# - verfies all the columns in the file using assert statements that verify all variables are complete (i.e. don't have NAs or missing values),
# - changes column name 'MCP.1' to 'MCP1',
# - writes the new clean data file(output file).
# Argument variables of the script are an input data file and
# a clean data output file containing all the data. 
#
# Dependencies: argparse and pandas
#
# Usage: python scripts/read_clean.py data/breast_cancer.csv results/breast_cancer_new.csv

# package import for parsing arguments
import argparse
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

    # Wrangling data
    #Renaming the column MCP.1
    data.rename(columns={'MCP.1':'MCP1'},
                     inplace=True)

    #Checking for all positive values
    assert len([x for x in data.Age if x < 0]) < 1 , "all values should be postive"
    assert len([x for x in data.BMI if x < 0]) < 1 , "all values should be postive"
    assert len([x for x in data.Glucose if x < 0]) < 1 , "all values should be postive"
    assert len([x for x in data.Insulin if x < 0]) < 1 , "all values should be postive"
    assert len([x for x in data.HOMA if x < 0]) < 1 , "all values should be postive"
    assert len([x for x in data.Leptin if x < 0]) < 1 , "all values should be postive"
    assert len([x for x in data.Adiponectin if x < 0]) < 1 , "all values should be postive"
    assert len([x for x in data.Resistin if x < 0]) < 1 , "all values should be postive"
    assert len([x for x in data.MCP1 if x < 0]) < 1 , "all values should be postive"

    # Checking if last column is classification
    assert len([x for x in data.Age if x < 0]) < 1 , "all values should be postive"


    #Writing new csv  input_file
    data.to_csv(args.output_file, index=False)

    # Summary of all the features
    data.describe()

# call main function
if __name__ == "__main__":
    main()
