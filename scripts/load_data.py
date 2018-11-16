# package import for parsing arguments
import argparse
import pandas as pd

# variable for parsing
parser = argparse.ArgumentParser()

# adding argument for input file
parser.add_argument('input_file')
args = parser.parse_args()

def main():

    # read the data
    data = pd.read_csv(args.input_file)
    print(data.head(10))
        
# call main function
if __name__ == "__main__":
    main()