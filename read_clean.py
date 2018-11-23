

import argparse
import pandas as pd

# input file
#input_file = dataR2.csv

# variable for parsing
parser = argparse.ArgumentParser()

# adding argument for input file
parser.add_argument('input_file')
args = parser.parse_args()

def main():

    # read the data
    data = pd.read_csv(args.input_file)
    print(data.head(10))

    # Wrangling data
    #Renaming the column MCP.1
    data.rename(columns={'MCP.1':'MCP1'},
                     inplace=True)

    assert len([x for x in data.Age if x < 0]) < 1 , "all values should be postive"
    assert len([x for x in data.BMI if x < 0]) < 1 , "all values should be postive"
    assert len([x for x in data.Glucose if x < 0]) < 1 , "all values should be postive"
    assert len([x for x in data.Insulin if x < 0]) < 1 , "all values should be postive"
    assert len([x for x in data.HOMA if x < 0]) < 1 , "all values should be postive"
    assert len([x for x in data.Leptin if x < 0]) < 1 , "all values should be postive"
    assert len([x for x in data.Adiponectin if x < 0]) < 1 , "all values should be postive"
    assert len([x for x in data.Resistin if x < 0]) < 1 , "all values should be postive"
    assert len([x for x in data.MCP1 if x < 0]) < 1 , "all values should be postive"


    # Summary of all the features
    data.describe()

# call main function
if __name__ == "__main__":
    main()
