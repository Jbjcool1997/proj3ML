![image](https://github.com/user-attachments/assets/486965b1-df34-44ae-9e2d-1ef2609908a4)*NOTE:* This file is a template that you can use to create the README for your project. The *TODO* comments below will highlight the information you should be sure to include.

# AzureML predicting pattern related to death by heart failure 

Heart disease is the leading cause of death around the world, responsible for about 17.9 million deaths each year, or roughly 31% of all global deaths.
Heart failure, often resulting from heart disease, is a key focus of this dataset, which includes 12 features to help predict the risk of death from heart failure.
Many heart-related conditions can be avoided by reducing risk factors like smoking, poor diet, lack of exercise, obesity, and alcohol abuse through broad public health efforts.

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

## Project Set Up and Installation

## Dataset

The data has manually downloaded from "https://www.kaggle.com/datasets/andrewmvd/heart-failure-clinical-data" and uploaded to AzureML datasets.

### Task
*TODO*: Explain the task you are going to be solving with this dataset and the features you will be using for it.

### Access
*TODO*: Explain how you are accessing the data in your workspace.

## Automated ML
*TODO*: Give an overview of the `automl` settings and configuration you used for this experiment

### Results
*TODO*: What are the results you got with your automated ML model? What were the parameters of the model? How could you have improved it?

*TODO* Remeber to provide screenshots of the `RunDetails` widget as well as a screenshot of the best model trained with it's parameters.

Rundetails:
![image](https://github.com/user-attachments/assets/2a82be82-ab2c-4d78-bf13-26a8b3581d7c)

Overview of the different models:

![image](https://github.com/user-attachments/assets/5dabb05b-b8e0-4941-8d89-59969678ec9a)

The best model:
![image](https://github.com/user-attachments/assets/d93e1c7f-8f2c-42b0-b131-b1c24d2cbdf6)



## Hyperparameter Tuning
*TODO*: What kind of model did you choose for this experiment and why? Give an overview of the types of parameters and their ranges used for the hyperparameter search


### Results
*TODO*: What are the results you got with your model? What were the parameters of the model? How could you have improved it?

*TODO* Remeber to provide screenshots of the `RunDetails` widget as well as a screenshot of the best model trained with it's parameters.

Rundetails
![image](https://github.com/user-attachments/assets/87a20e8e-e867-4384-affa-bfe62fc4ab6b)

Overview of the different models:
![image](https://github.com/user-attachments/assets/ddc1e9dd-e7ec-4874-9310-00be4903536a)

The best model:
![image](https://github.com/user-attachments/assets/00e4c405-82c3-406d-84f1-0563395ecb39)

![image](https://github.com/user-attachments/assets/f7cebfde-83ce-4963-a9b9-903d29436d43)


## Model Deployment
*TODO*: Give an overview of the deployed model and instructions on how to query the endpoint with a sample input.

Pipeline endpoint:
![image](https://github.com/user-attachments/assets/e029f1bb-97fe-4bc5-94ea-c7bc129a94b1)

![image](https://github.com/user-attachments/assets/c9be172f-d8f2-4aab-aca1-e77fafc074ca)



## Screen Recording
*TODO* Provide a link to a screen recording of the project in action.

https://www.youtube.com/watch?v=QwSc4_eGmzI&ab_channel=JacobJensen

## Standout Suggestions
*TODO (Optional):* This is where you can provide information about any standout suggestions that you have attempted.
