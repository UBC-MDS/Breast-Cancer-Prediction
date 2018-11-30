# Supervised Learning Model to Predict Breast Cancer
## DSCI 522 Workflows


### Question

- What are the strongest predictors of breast cancer?
- Type of question = predictive 

### Introduction 

The goal of this project is to discover the strongest predictors of breast cancer in the data source [Breast Cancer Coimbra Data Set](https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Coimbra). The dataset includes 64 records of breast cancer paitients and 52 records of healthy controls. There are 9 features in the dataset that contribute to predict breast cancer. Using these features, the project aims to identify the strongest predictors of breast cancer.

#### Motivation for analysis

Cancer is an open ended problem till date. It is one of biggest research areas of medical science. There are many types of  cancers which are rapidly getting common. It is estimated that 41,400 deaths (40,920 women and 480 men) from breast cancer will occur this year [2018](https://www.cancer.net/cancer-types/breast-cancer/statistics/2015). We were highly interested to use machine learning models to dive in this dataset and explore about breast cancer predictions.

### Data Exploration
  
The data used in the analysis is from the UCI machine learning repository [Breast Cancer Coimbra Data Set](https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Coimbra). The data comprises of nine predictors, and a binary dependent variable indicating the presence or absence of breast cancer. All nine predictors are quantitative variables with positive values.
  
Quantitative Attributes: 
  
**Age** (years) : Age of the individual.
  
**BMI** (kg/m2) : Body mass index of the individual.
  
**Glucose** (mg/dL) : Glucose level of the individual. 
  
**Insulin** (µU/mL) : Insulin level of the individual. Insulin is a hormone made by the pancreas that allows your body to use sugar (glucose) from carbohydrates in the food that you eat for energy or to store glucose for future use.
  
**HOMA** : Homeostasis model assessment used to detect insulin resistance and identify patients at high risk of breast cancer development.
  
**Leptin** (ng/mL) : Leptin, "the hormone of energy expenditure", is a hormone predominantly made by adipose cells that helps to regulate energy balance by inhibiting hunger. Leptin is opposed by the actions of the hormone ghrelin, the "hunger hormone". Both hormones act on receptors in the arcuate nucleus of the hypothalamus. 
  
**Adiponectin** (µg/mL) : Adiponectin (also referred to as GBP-28, apM1, AdipoQ and Acrp30) is a protein hormone which is involved in regulating glucose levels as well as fatty acid breakdown. In humans it is encoded by the ADIPOQ gene and it is produced in adipose tissue.
  
**Resistin** (ng/mL) : Resistin also known as adipose tissue-specific secretory factor (ADSF) or C/EBP-epsilon-regulated myeloid-specific secreted cysteine-rich protein (XCP1) is a cysteine-rich adipose-derived peptide hormone that in humans is encoded by the RETN gene.
  
**MCP-1** (pg/dL) : The chemokine (C-C motif) ligand 2 (CCL2) is also referred to as monocyte chemoattractant protein 1 (MCP1) and small inducible cytokine A2. CCL2 is a small cytokine that belongs to the CC chemokine family. 
  
**Labels**: 1 denotes Healthy controls and 2 denotes Patients.


### Plan of action

- Use supervised learning to build a predictive model.
- 80% of the data will be used to train the predictive model, and 20% will be used to test the predictive model. To avoid over-fitting in the model, use cross validation.
- Visualize distributions of training data features using histograms to identify better predictors from the data set.
- Use decision tree classification to build the predictive model.
- Visualise the test data predictions.

### Choosing decision tree classification

We choose decision tree classification for our analysis because it is parametric. In our attempt to build a model that ranks features based on their importance, decision tree classification takes all of the features and complete training data to pick the strongest predictors. Other supervised learning approaches that are non-parametric such as K-Nearest Neighbours would not be able to rank the features by importance, and thus, fail to answer our analysis question.

### Usage

1. Clone this repo, and using the command line, navigate to the root of this project.

2. Run the following commands:

``python scripts/read_clean.py data/breast_cancer.csv results/breast_cancer_new.csv``

``python scripts/eda.py results/breast_cancer_new.csv img/plot``

``python scripts/analysis.py results/breast_cancer_new.csv results/detailed.csv``

``python scripts/analysis.py results/breast_cancer_new.csv results/importance.csv``

``python scripts/plot.py results/importance.csv results/results.png``

``Rscript -e "rmarkdown::render('doc/report.Rmd')``

### Result Summary and Visualization

The [Final report](https://github.com/UBC-MDS/Breast-Cancer-Prediction/blob/master/doc/report.md) records visualization of the importance of features and accuracy of predicative model on test data set.

### Dependencies

Python and the following python packages:
- numpy (version 1.14.3)
- pandas (version 0.23.0)
- sklearn (version 0.19.1)
- matplotlib (version 3.0.0)
- seaborn (version 0.9.0)
- argparse (version 1.0.10)

### Relevant research links:

[Machine learning applications in cancer prognosis and prediction](https://www.sciencedirect.com/science/article/pii/S2001037014000464)

### Citation 

- [Wikipedia](https://en.wikipedia.org/wiki/Insulin) (for basic terms of medical attributes and their importance in the cancer research).

- Patrício, M., Pereira, J., Crisóstomo, J., Matafome, P., Gomes, M., Seiça, R., & Caramelo, F. (2018). [Using Resistin, glucose, age and BMI to predict the presence of breast cancer](https://bmccancer.biomedcentral.com/articles/10.1186/s12885-017-3877-1)

### Team

[Akansha Vashisth](https://github.com/akanshaVashisth)

[Talha Siddiqui](https://github.com/talhaadnan100)