#### AWS Machine Learning Study Notes
*6/6/2023* <br/>
* Amazon S3
  - Bucket
  - Amazon S3 max object size is 5TB. 
  - no need to remember the S3 storage class
  - Glacier: no need to storage after xx days

#### AWS Machine Learning Bootcamp
* Supervised Learning
  - Binary Classification: true or false
  - MultiClassification: e.g. predict which month people would like to purchase
  - Regression

* Approaches of outliers
- Artificial - delete
- Natural - log (decrease the extremeness), replace in mean

##### General Steps for a machine learning project
* Data Preprocessing
  - Understand a business scenario and corresponding dataset by analyzing the data using descriptive statistics
  - Use visualization tools to support this analysis:
    - Scatter plots to spot correlations between features
    - Box and whisker plots and histograms to understand the distribution of the data
  - Use statistics tools to support previous analysis, such as a correlation matrix to quantify those relationships
  - Based on the analysis conclusions, prepare a processed dataset for the model by:
    - Dealing with outliers
    - Dealing with missing values (remove/impute)
    - Cleaning the data

* XGBoost
  - Hyperparameter: your settings
