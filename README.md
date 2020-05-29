# Project-Model# Purwadhika Final Project - Predict Term Deposit

by: Hilman Fadhil Makarim

Dataset: Bank Marketing

Source : [kaggle](https://www.kaggle.com/rouseguy/bankbalanced)

![](https://github.com/hilmanmakarim/Project-Model/blob/master/gallery/bankcampaign.PNG)

PROJECT DESCRIPTION
---
This project to classifying the possibility of customer bank will make a term deposit or not.
The classification goal is to predict if the client will subscribe a term deposit (variable y).
The data is related with direct marketing campaigns of a Portuguese banking institution,  The marketing campaigns were based on phone calls. Often, more than one contact to the same client was required, in order to access if the product (bank term deposit) would be ('yes') or not ('no') subscribed. (source : [Bank Marketing](https://archive.ics.uci.edu/ml/datasets/Bank+Marketing)

Final decision for this classification model is Random Forest Classifier
APPS
---
HOME PAGE
![](https://github.com/hilmanmakarim/Project-Model/blob/master/gallery/Home.PNG)

Attribute Information:
Bank client data:

    Age (numeric)
    Job : type of job (categorical: 'admin.', 'blue-collar', 'entrepreneur', 'housemaid', 'management', 'retired', 'self-employed', 'services', 'student', 'technician', 'unemployed', 'unknown')
    Marital : marital status (categorical: 'divorced', 'married', 'single', 'unknown' ; note: 'divorced' means divorced or widowed)
    Education (categorical: 'basic.4y', 'basic.6y', 'basic.9y', 'high.school', 'illiterate', 'professional.course', 'university.degree', 'unknown')
    Default: has credit in default? (categorical: 'no', 'yes', 'unknown')
    Housing: has housing loan? (categorical: 'no', 'yes', 'unknown')
    Loan: has personal loan? (categorical: 'no', 'yes', 'unknown')


Related with the last contact of the current campaign:

    Contact: contact communication type (categorical: 'cellular','telephone')
    Month: last contact month of year (categorical: 'jan', 'feb', 'mar', ..., 'nov', 'dec')
    Day_of_week: last contact day of the week (categorical: 'mon','tue','wed','thu','fri')
    Duration: last contact duration, in seconds (numeric). Important note: this attribute highly affects the output target (e.g., if duration=0 then y='no'). Yet, the duration is not known before a call is performed. Also, after the end of the call y is obviously known. Thus, this input should only be included for benchmark purposes and should be discarded if the intention is to have a realistic predictive model.

Other attributes:

    Campaign: number of contacts performed during this campaign and for this client (numeric, includes last contact)
    Pdays: number of days that passed by after the client was last contacted from a previous campaign (numeric; 999 means client was not previously contacted)
    Previous: number of contacts performed before this campaign and for this client (numeric)
    Poutcome: outcome of the previous marketing campaign (categorical: 'failure','nonexistent','success')
    
Output variable (desired target):

    deposit - has the client subscribed a term deposit? (binary: 'yes', 'no')

PREDICTION RESULT
---
Customer will create new term deposit
![](https://github.com/hilmanmakarim/Project-Model/blob/master/gallery/resultyes.PNG)
Customer will not create a new term deposit
![](https://github.com/hilmanmakarim/Project-Model/blob/master/gallery/resultnot.PNG)
