# AzureML predicting pattern related to death by heart failure 

Heart disease is the leading cause of death around the world, responsible for about 17.9 million deaths each year, or roughly 31% of all global deaths.
Heart failure, often resulting from heart disease, is a key focus of this dataset, which includes 12 features to help predict the risk of death from heart failure.
Many heart-related conditions can be avoided by reducing risk factors like smoking, poor diet, lack of exercise, obesity, and alcohol abuse through broad public health efforts.


## Project Set Up and Installation

## Dataset

The data is publicaly availabe at "https://www.kaggle.com/datasets/andrewmvd/heart-failure-clinical-data" and have not been updated since 2020.

### Task

In the provided data 13 datapoints (columns) which can help identify pattern related to heart failure.

1. Age - The patients age
2. Anaemia - Decrease of red blood cells or hemoglobin
3. creatinine_phosphokinase - Level of the CPK enzyme in the blood
4. diabetes - If the patient has diabetes or not.
6. ejection_fraction - Percentage of blood leaving the heart at each contraction (percentage
7. high_blood_pressure - If the patient has hypertension (boolean)
8. platelets - Platelets in the blood
9. serum_sodium - Level of serum sodium in the blood
10. sex - the gender of the patient
11. smoking - If the patient was smoking or not
12. time - follow-up period in days
13. DEATH_EVENT - if the patient died during the follow-up

Point 13, DEATH_EVENT will the column to analyzed. 

### Access

The data has manually downloaded from "https://www.kaggle.com/datasets/andrewmvd/heart-failure-clinical-data" and uploaded to AzureML datasets, as well as Github.

## Automated ML
*TODO*: Give an overview of the `automl` settings and configuration you used for this experiment

Primary_metric = Classification
Since the DEATH_EVENT is a yes/no (1/0), classification should be suffeicient as the primary_metric

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


Metric
![image](https://github.com/user-attachments/assets/089205c6-bbdb-49f0-b8fc-496b6508908d)



![image](https://github.com/user-attachments/assets/f84f58ff-bb96-4697-a502-6e577d3ce9a9)


Esemble details

![image](https://github.com/user-attachments/assets/d31e9ac8-0bd1-4555-804d-9d434dc09125)



Registrating the best model

![image](https://github.com/user-attachments/assets/6fe4ed25-d6d9-4c4e-9816-135a2de2abe6)


Environment details

![image](https://github.com/user-attachments/assets/6e3cdfef-cee9-4ba2-9afe-76cad267bbdc)


### Results
*TODO*: What are the results you got with your automated ML model? What were the parameters of the model? How could you have improved it?

*TODO* Remeber to provide screenshots of the `RunDetails` widget as well as a screenshot of the best model trained with it's parameters.

Rundetails:
![image](https://github.com/user-attachments/assets/2a82be82-ab2c-4d78-bf13-26a8b3581d7c)

Overview of the different models:

![image](https://github.com/user-attachments/assets/5dabb05b-b8e0-4941-8d89-59969678ec9a)

### The best model:
![image](https://github.com/user-attachments/assets/d93e1c7f-8f2c-42b0-b131-b1c24d2cbdf6)



## Hyperparameter Tuning
*TODO*: What kind of model did you choose for this experiment and why? Give an overview of the types of parameters and their ranges used for the hyperparameter search

For the Hyperparameter tuning a logisticRegression algorith was used along side 2 defined paramters.

1. Inverse regularization strength: Which was set to either 0.1, 0.5, 1, or 5, with 1 being the default setting.

2. Maximum number of iterations: Which was set to either 50, 100, or 500, with the default being 100.

Both parameters supporting the classification task for the logistic regression, utilizing them to make predictions.
As well as having the main benefit of handling hyperparameters without overwhelming/overclocking the compute ressoruces.


The RandomParameterSampling method was selected for parameter sampling. This approach is beneficial because it produces results that closely reflect what might be expected if the entire population were tested.

Additionally, the Banditpolicy was implemented with the goal of saving compute ressources etc. as it manages resources very efficiently by terminating jobs that do not perform well compared to the best job, using a defined slack factor.


![image](https://github.com/user-attachments/assets/6c5f224f-7f98-4cc1-8894-422833a44e81)



### Results

The model achieved an accuracy of 0.88 using the HyperDrive run. 
To enhance the performance, more parameters could be added to the tuning process. Trying a different parameter sampling method might also yield better results. Additionally, adjusting the early termination policy could help ensure that promising runs are not stopped too soon. Simple just giving it more time to run could help identify better model, however it comes with the expense of ressources.

Rundetails
![image](https://github.com/user-attachments/assets/87a20e8e-e867-4384-affa-bfe62fc4ab6b)

Overview of the different models:
![image](https://github.com/user-attachments/assets/ddc1e9dd-e7ec-4874-9310-00be4903536a)

The best model:

![image](https://github.com/user-attachments/assets/f7cebfde-83ce-4963-a9b9-903d29436d43)

![image](https://github.com/user-attachments/assets/00e4c405-82c3-406d-84f1-0563395ecb39)

Metric:
![image](https://github.com/user-attachments/assets/2df2797a-f6a9-4683-9453-7789ebeb491a)


## Model Deployment
*TODO*: Give an overview of the deployed model and instructions on how to query the endpoint with a sample input.

Pipeline endpoint:
![image](https://github.com/user-attachments/assets/e029f1bb-97fe-4bc5-94ea-c7bc129a94b1)

![image](https://github.com/user-attachments/assets/c9be172f-d8f2-4aab-aca1-e77fafc074ca)

![image](https://github.com/user-attachments/assets/2b6265a9-4154-4b10-adf7-6bf2b156072f)

Registrating the best model:
![image](https://github.com/user-attachments/assets/f4c4e0a6-d3ea-473d-a618-8724777ebfc5)

![image](https://github.com/user-attachments/assets/d51df0b7-e91a-49a9-9849-ba928a6e0e58)


## Screen Recording
*TODO* Provide a link to a screen recording of the project in action.

https://www.youtube.com/watch?v=QwSc4_eGmzI&ab_channel=JacobJensen

## Standout Suggestions
*TODO (Optional):* This is where you can provide information about any standout suggestions that you have attempted.
