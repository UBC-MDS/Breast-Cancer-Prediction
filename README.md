# Supervised Learning Model to Predict Breast Cancer
## DSCI 522 Workflows
Data Source: [Breast Cancer Coimbra Data Set]()

### Question

- Using quantitative health attributes from Breast Cancer Coimbra data set, predict whether individuals have breast cancer or not?
- Type of question = predictive 

### Data Import

- `load_data.py` Python script loads a CSV file.
- To load the data, use `load_data.py` script and parse `breast-cancer-coimbra-data-set.csv` file as an argument.
- Run script in console as `python scripts/load_data.py data/breast-cancer-coimbra-data-set.csv`.

### Plan

- Use supervised learning to build a predictive model
- 80% of the data will be used the train the predictive model, and 20% will be used to test the predictive model. This is to avoid over-fitting on our model
- Visualize distributions of training data features using histograms to identify better predictors from our data set
- Use classification with a decision tree to build the predictive model
- Include a visualization of the decision tree
- Visualise the test data predictions

### Result Summary and Visualization
	
- Visualize accuracy of predicative model on test data set
- Raw output of test data predictions

## Dependencies
Python and Python Packages:
- numpy
- pandas
- sklearn
- matplotlib
- seaborn
- argparse
