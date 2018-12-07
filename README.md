# Breast Cancer Prediction

#### Date : 2018-11-30

#### Authors

| Name | Github |
| ---- | -------|
| Akansha Vashisth |[akanshaVashisth](https://github.com/akanshaVashisth)|
| Talha Siddiqui| [talhaadnan100](https://github.com/talhaadnan100)|


#### Question

- What are the strongest predictors of breast cancer?
- Type of question = predictive 

#### Introduction 

The goal of this project is to discover the strongest predictors of breast cancer in the data source [Breast Cancer Coimbra Data Set](https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Coimbra). The dataset includes 64 records of breast cancer patients and 52 records of healthy controls. There are 9 features in the dataset that contribute to predict breast cancer. Using these features, the project aims to identify the strongest predictors of breast cancer.

##### Motivation for analysis

Cancer is an open ended problem till date. It is one of biggest research areas of medical science. There are many types of  cancers which are rapidly getting common. It is estimated that 41,400 deaths (40,920 women and 480 men) from breast cancer will occur this year [2018](https://www.cancer.net/cancer-types/breast-cancer/statistics/2015). We were highly interested to use machine learning models to dive in this dataset and explore about breast cancer predictions.

#### Data Exploration
  
The data used in the analysis is from the UCI machine learning repository [Breast Cancer Coimbra Data Set](https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Coimbra). The data comprises of nine predictors, and a binary dependent variable indicating the presence or absence of breast cancer. All nine predictors are quantitative variables with positive values.
  
Quantitative attributes and their description: 
  
*Age* (years) : Age of the individual.
  
*BMI* (kg/m2) : Body mass index of the individual.
  
*Glucose* (mg/dL) : Glucose level of the individual. 
  
*Insulin* (µU/mL) : Insulin level of the individual. Insulin is a hormone made by the pancreas that allows your body to use sugar (glucose) from carbohydrates in the food that you eat for energy or to store glucose for future use.
  
*HOMA* : Homeostasis model assessment used to detect insulin resistance and identify patients at high risk of breast cancer development.
  
*Leptin* (ng/mL) : Leptin, "the hormone of energy expenditure", is a hormone predominantly made by adipose cells that helps to regulate energy balance by inhibiting hunger. Leptin is opposed by the actions of the hormone ghrelin, the "hunger hormone". Both hormones act on receptors in the arcuate nucleus of the hypothalamus. 
  
*Adiponectin* (µg/mL) : Adiponectin (also referred to as GBP-28, apM1, AdipoQ and Acrp30) is a protein hormone which is involved in regulating glucose levels as well as fatty acid breakdown. In humans it is encoded by the ADIPOQ gene and it is produced in adipose tissue.
  
*Resistin* (ng/mL) : Resistin also known as adipose tissue-specific secretory factor (ADSF) or C/EBP-epsilon-regulated myeloid-specific secreted cysteine-rich protein (XCP1) is a cysteine-rich adipose-derived peptide hormone that in humans is encoded by the RETN gene.
  
*MCP-1* (pg/dL) : The chemokine (C-C motif) ligand 2 (CCL2) is also referred to as monocyte chemoattractant protein 1 (MCP1) and small inducible cytokine A2. CCL2 is a small cytokine that belongs to the CC chemokine family. 
  
*Labels*: 1 denotes Healthy controls and 2 denotes Patients.


#### Plan of action

- Use supervised learning to build a predictive model.
- 80% of the data will be used to train the predictive model, and 20% will be used to test the predictive model. To avoid over-fitting in the model, use cross validation.
- Visualize distributions of training data features using histograms to identify better predictors from the data set.
- Use decision tree classification to build the predictive model.
- Visualise the test data predictions.

#### Choosing decision tree classification

We choose decision tree classification for our analysis because it is parametric. In our attempt to build a model that ranks features based on their importance, decision tree classification takes all of the features and complete training data to pick the strongest predictors. Other supervised learning approaches that are non-parametric such as K-Nearest Neighbours would not be able to rank the features by importance, and thus, fail to answer our analysis question.

#### Usage

Steps without Docker:

1. Clone this repo, and using the command line, navigate to the root of this project.

    I Without Make:
    
      1. Run the following commands:

      ```python scripts/read_clean.py data/breast_cancer.csv results/breast_cancer_new.csv```

      ```python scripts/eda.py results/breast_cancer_new.csv img/plot```

      ```python scripts/analysis.py results/breast_cancer_new.csv results/detailed.csv```

      ```python scripts/analysis.py results/breast_cancer_new.csv results/importance.csv```

      ```python scripts/plot.py results/importance.csv results/results.png```

      ```Rscript -e "rmarkdown::render('doc/report.Rmd')```

    II With Make:
    
      1. Makefile runs all the above commands using the following command:
        
      ```make all```
        
      2. To erase all analysis output files created by the following command:
        
      ```make clean```

#### Dependencies Diagram

![](https://github.com/UBC-MDS/Breast-Cancer-Prediction/blob/master/Makefile.png)


#### Using docker image

Follow the steps to use docker image:

1. Use launchpad/Finder/Start menu/etc to find and launch Docker.

2. Open command line (terminal/GitBash) and run the following command:
```docker pull talhaadnan100/breast-cancer-prediction```

    To verify that it successfully pulled use command: ```docker images```

3. Now, to launch a container from the image run the following command:
```docker run --rm it -e PASSWORD=test -v <PATH-ON-YOUR-COMPUTER>:/home/breast-cancer-prediction talhaadnan100/breast-cancer-prediction /bin/bash```

    If it worked, then your command line prompt should look something like this:

    ```root@18907dd9d819:/#```

4. Now you can navigate in the directory ``/home/Breast-Cancer-Prediction`` by using the following commands to explore the container:
 ```cd``` , ```ls```, ```pwd```

5. To run the whole analysis from top to bottom, run command: ```make all```.

6. You can use ``exit`` command to exit from the the container and go back to your regular prompt/terminal.

#### Result Summary and Visualization

The [Final report](https://github.com/UBC-MDS/Breast-Cancer-Prediction/blob/master/doc/report.md) records visualization for the importance of all the features and accuracy of predictive model on test data set.

| Result files| Link to file|
| ---- | -------|
| File after cleaning the data| [breast_cancer_new.csv](https://github.com/UBC-MDS/Breast-Cancer-Prediction/blob/master/results/breast_cancer_new.csv)|
| File that includes all the predictions| [detailed.csv](https://github.com/UBC-MDS/Breast-Cancer-Prediction/blob/master/results/detailed.csv)|
| File for importance of features| [importance.csv](https://github.com/UBC-MDS/Breast-Cancer-Prediction/blob/master/results/importance.csv)|
| Plot for the result | [results.png](https://github.com/UBC-MDS/Breast-Cancer-Prediction/blob/master/results/results.png) |

#### Dependencies

Python 3.7 and the following python packages:
- numpy (version 1.14.3)
- pandas (version 0.23.0)
- sklearn (version 0.19.1)
- matplotlib (version 3.0.0)
- seaborn (version 0.9.0)
- argparse (version 1.0.10)

#### Relevant research links:

[Machine learning applications in cancer prognosis and prediction](https://www.sciencedirect.com/science/article/pii/S2001037014000464)

#### Citation 

- [Wikipedia](https://en.wikipedia.org/wiki/Insulin) (for basic terms of medical attributes and their importance in the cancer research).

- Patrício, M., Pereira, J., Crisóstomo, J., Matafome, P., Gomes, M., Seiça, R., & Caramelo, F. (2018). [Using Resistin, glucose, age and BMI to predict the presence of breast cancer](https://bmccancer.biomedcentral.com/articles/10.1186/s12885-017-3877-1).