# AzureML predicting pattern related to death by heart failure 

## Project Overview

In this project, we will an public data source related to health care sector, the data is avaliable to download in CSV.
The CSV file will be uploaded to Azure ML Workspace's datasets, and afterwards there are 2 models that needs to be trained.

- HyperDriver
- Automated ML

Afterwards it will be possible to compare the two models and their performance.
From there the AutoML will be deployed and tested.


![image](https://github.com/user-attachments/assets/5c1414c2-a92b-4261-a940-52080e180d82)



## Project Set Up and Installation

Heart disease is the leading cause of death around the world, responsible for about 17.9 million deaths each year, or roughly 31% of all global deaths.
Heart failure, often resulting from heart disease, is a key focus of this dataset, which includes 12 features to help predict the risk of death from heart failure.
Many heart-related conditions can be avoided by reducing risk factors like smoking, poor diet, lack of exercise, obesity, and alcohol abuse through broad public health efforts.

## Dataset

The data is publicaly availabe at "https://www.kaggle.com/datasets/andrewmvd/heart-failure-clinical-data" and have not been updated since 2020.

### Task

In the provided data 13 datapoints (columns) which can help identify pattern related to heart failure.

1. Age - The patients age
2. Anaemia - Decrease of red blood cells or hemoglobin
3. creatinine_phosphokinase - Level of the CPK enzyme in the blood
4. diabetes - If the patient has diabetes or not.
5. ejection_fraction - Percentage of blood leaving the heart at each contraction (percentage
6. high_blood_pressure - If the patient has hypertension (boolean)
7. platelets - Platelets in the blood
8. serum_sodium - Level of serum sodium in the blood
9. serum_creatine - Level of serum creatine in the blood
10. sex - the gender of the patient
11. smoking - If the patient was smoking or not
12. time - follow-up period in days
13. DEATH_EVENT - if the patient died during the follow-up

Point 13, DEATH_EVENT will the column to analyzed. 

### Access

The data has manually downloaded from "https://www.kaggle.com/datasets/andrewmvd/heart-failure-clinical-data" and uploaded to AzureML datasets, as well as Github.

## Automated ML

Primary_metric = Classification
Since the DEATH_EVENT is a True/False (1/0), classification should be suffeicient as the primary_metric

Timeout_minutes = 20
To save on compute resources and adhere to the workspace timelimit, 20 minutes was set a the timeout.

Max_current_iteration = 5
Given the small data size, 5 iteration should be enough.

Enable_early_stopping = True
Early stopping initiated with the goal of saving time.

featurization = 'auto'
Simple the default setting making sure data huardrails and featurazation steps are performed automatically.

![image](https://github.com/user-attachments/assets/37f348de-d15c-449b-9a53-e6a75c43c825)

### Results

The outcome of the AutoML approach resulted in the best model being VotingEnsemble model with an accuracy of 0.879.
The result was achived by comgining 6 ensemble details, all with the same weight at 0.1666:

SparseNormalizer, XGBoosterClarrifier

MaxAbsScaler, LightGBM

MaxAbsScaler, LightGBM

RobustScaler,RandomForest

StandardScalerWrapper,XGBoosterClarrifier

StandardScalerWrapper,XGBoosterClarrifier

![image](https://github.com/user-attachments/assets/48f749bc-8ade-44a8-a0e4-b6769c2b8e6f)


In terms of optimization, an obvious first step is to incease the timeout or change the early termination policy.
As shown on the image below displaying the best model, is stopped due to the early termination policy.
However, it will come with the cost of more ressouces, in terms of time and money.


### The best model

![image](https://github.com/user-attachments/assets/00010243-2908-4a20-847e-4af0dc782ce4)
![image](https://github.com/user-attachments/assets/a5c77c1f-a895-4d50-832c-51ca9eed77a5)
![image](https://github.com/user-attachments/assets/372c2844-fb20-4a12-b71c-9747ba63de04)


### Metric


![image](https://github.com/user-attachments/assets/089205c6-bbdb-49f0-b8fc-496b6508908d)



### Ensemble details


![image](https://github.com/user-attachments/assets/d31e9ac8-0bd1-4555-804d-9d434dc09125)


### Environment details

![image](https://github.com/user-attachments/assets/6e3cdfef-cee9-4ba2-9afe-76cad267bbdc)


### Run details

![image](https://github.com/user-attachments/assets/2a82be82-ab2c-4d78-bf13-26a8b3581d7c)


### Registrating the best model


![image](https://github.com/user-attachments/assets/eddf1382-8b77-4bc2-b60a-58585a4b9216)



## Hyperparameter Tuning

For the Hyperparameter tuning a logisticRegression algorith was used along side 2 defined paramters.

1. Inverse regularization strength: Which was set to either 0.1, 0.5, 1, or 5, with 1 being the default setting.

2. Maximum number of iterations: Which was set to either 50, 100, or 500, with the default being 100.

Both parameters supporting the classification task for the logistic regression, utilizing them to make predictions.
As well as having the main benefit of handling hyperparameters without overwhelming/overclocking the compute ressoruces.


The RandomParameterSampling method was selected for parameter sampling. This approach is beneficial because it produces results that closely reflect what might be expected if the entire population were tested.

Additionally, the Banditpolicy was implemented with the goal of saving compute ressources etc. as it manages resources very efficiently by terminating jobs that do not perform well compared to the best job, using a defined slack factor.


![image](https://github.com/user-attachments/assets/6c5f224f-7f98-4cc1-8894-422833a44e81)



### Results

The model achieved an accuracy of 0.92 using the HyperDrive run. 
To enhance the performance, more parameters could be added to the tuning process. Trying a different parameter sampling method might also give a better results. Additionally, adjusting the early termination policy could help ensure that promising runs are not stopped too soon. Simple just giving it more time to run could help identify better model, however it comes with the expense of ressources.

### Run details
![image](https://github.com/user-attachments/assets/87a20e8e-e867-4384-affa-bfe62fc4ab6b)

### Overview of the different models:

![image](https://github.com/user-attachments/assets/ddc1e9dd-e7ec-4874-9310-00be4903536a)

### The best model:

![image](https://github.com/user-attachments/assets/f7cebfde-83ce-4963-a9b9-903d29436d43)

![image](https://github.com/user-attachments/assets/00e4c405-82c3-406d-84f1-0563395ecb39)

### Metric:

![image](https://github.com/user-attachments/assets/2df2797a-f6a9-4683-9453-7789ebeb491a)

### Registrating the best model

![image](https://github.com/user-attachments/assets/164dac38-9964-4f01-98d0-8ca90dfcc33a)

![image](https://github.com/user-attachments/assets/79489ad4-f12c-44e8-ad77-5fc121e10572)


## Model Deployment

The best AutoML was deloyed (VotingEnsemble) - The model was succesfully deployed and the endpoint being active.

### Notebook deployment
![image](https://github.com/user-attachments/assets/fa0d9b21-e4f5-4bb5-ac24-29758e18a75d)


### Notebook interacting with the deployed endpoint:
![image](https://github.com/user-attachments/assets/ca3a1605-94d2-49ac-ac07-5954bc002bab)

### GUI of endpoint:
![image](https://github.com/user-attachments/assets/3e870537-34eb-45f2-acd0-dd42539b1e18)

### Deployment state in the notebook
![image](https://github.com/user-attachments/assets/10c9100b-8c8c-4ad3-b4da-d2bd5ea8defe)


### Deployment state in GUI
![image](https://github.com/user-attachments/assets/c806f0ae-caa6-43b1-b587-f89196139f34)

### Sample input to the endpoint

![image](https://github.com/user-attachments/assets/fd79a0a4-cb45-4e2e-b691-1280678c7f9f)

### verifying the output 
![image](https://github.com/user-attachments/assets/ce1ade02-7934-47d8-bb84-0fc51e2523f4)


## Screen Recording

https://www.youtube.com/watch?v=QwSc4_eGmzI&ab_channel=JacobJensen

## Future Work

Some improvements for future consideration

Training optimization: Due to the time limit  of the workspace and limited attempts, several timeouts was added to the experiment - Without timeout AutoMl could have developed more models and potentailly have created a even better performance model.

Improved data: The dataset currently withstands of 13 columns and 300 rows, thereby giving the Azure limited data to analyze on, so the data could be improved by either adding more. Additionally, if a SME believe the 13 columns are missing a vital data point, more column could also be relevant. Furthermore, the data is from 2020, 5 years old, new relevant data etc. could have been discovered. 

Having the right permission in AzureML - As the provided AzureML workspace did not have the right permission, I have to manually add "Azure Container Instance Contributor" to the my own workspace - The process would be more efficient to have the correct permissions from the start and saving time researching.
