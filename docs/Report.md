# Online Payment Fraud Detection

- Author - Priyanka Anumandla
- Semester - Spring'24
- Prepared for UMBC Data Science Master Degree Capstone by Dr Chaojie (Jay) Wang
- GitHub - https://github.com/priyanka903
- LinkedIn - https://www.linkedin.com/in/priyanka-anumandla
- PowerPoint Presentation: https://1drv.ms/p/c/3e38ad4e76a9edce/EbG8vvBEWaxKhlXqMsJPqwAB38s0jblNxCb8qKv-jNa0nw?e=KwzMwP 
- YouTube Video: 


## Background
### Problem Statement
Dataset revolves around online payment transactions, particularly focusing on identifying fraudulent activities. Each row in dataset corresponds to a transaction and contains information such as the transaction type, amount, involved parties (customer initiating the transaction and recipient), balances before and after the transaction, and a label indicating whether the transaction is fraudulent or not.

### Potential Real-world applications
Online payment fraud is a significant issue affecting businesses and individuals alike. By leveraging machine learning models on datasets like the one you've collected, organizations can develop robust systems to automatically detect and prevent fraudulent transactions. This matters for several reasons:
- Financial Impact: Fraudulent transactions can lead to significant financial losses for both businesses and customers. Identifying and preventing such transactions is crucial for protecting financial assets.
- Security: Enhancing the security of online transactions is essential to maintain the trust of users in online payment systems. Identifying fraudulent activities contributes to a more secure online environment.
- Operational Efficiency: Automated fraud detection systems can improve operational efficiency by reducing the manual effort required to investigate and handle fraudulent transactions.

### Research Questions
- Discover the hidden patterns in the fraudulent transactions that can be utilized for better detection.
- What all attributes play significant role in fraudulent transactions?
- Does amount/type of transaction attibute have the imporantance in fraud transaction.
- Identify which machine learning algorithms or models are most effective in identifying fraudulent transactions.

## Data 
- **Source:** https://www.kaggle.com/datasets/jainilcoder/online-payment-fraud-detection/data
- **Size:** - 186 MB
- **Shape:** 
  - Rows - 6362620
  - Columns - 11
- **Each row describes** - Transaction details.
- **Data Dictionary**

| Column          | Data Type | Definition                                            | Potential Values                                      |
|-----------------|-----------|-------------------------------------------------------|--------------------------------------------------------|
| Step            | Integer   | The step in the transaction process                    | Continuous numerical values                           |
| Type            | String    | The type of transaction (e.g., PAYMENT, TRANSFER)      | PAYMENT, TRANSFER, CASH_OUT, etc.                       |
| Amount          | Float     | The transaction amount                                 | Continuous numerical values                           |
| NameOrig        | String    | The name of the origin account                         | Alphanumeric account identifiers                      |
| OldBalanceOrg   | Float     | The original balance in the origin account             | Continuous numerical values                           |
| NewBalanceOrig   | Float     | The new balance in the origin account after the transaction | Continuous numerical values                   |
| NameDest        | String    | The name of the destination account                    | Alphanumeric account identifiers                      |
| OldBalanceDest   | Float     | The original balance in the destination account        | Continuous numerical values                           |
| NewBalanceDest   | Float     | The new balance in the destination account after the transaction | Continuous numerical values                   |
| IsFraud         | Integer   | Indicates whether the transaction is fraudulent (1 for true, 0 for false) | 0, 1                                               |
| IsFlaggedFraud  | Integer   | Indicates whether the transaction is flagged as fraudulent according to business rules | 0, 1                                       |

- **Target Variable(s)** - isFraud is Target Variable
- The remaining columns are predictors

## Model Training
1. Models for Predictive Analytics:
Models used are Logistic regression, Decision trees, Random forest and XGboost. I have applied grid search on the best model to recieve idea results.

2. Training Procedure:
I have performed the Train vs test split for 70/30 to ensure the model learns effectively and generalizes well to new data.

3. Python Packages:
I have primarily used python packages in project. They are Numpy, Pandas, missingno, matplotlib, plotly, seaborn and scikit-learn

4. Development Environments:
The development environments are
- Local machine: Jupyter Notebook 
- Online platforms: Google Colab, GitHub

5.Performance Measures of the models
I have evaluated performance of the model using Accuracy, Classification Report and ROC curve.

## Web App Development:
Developed a web application using Streamlit for users to interact with Transaction details
- **Streamliapp:** (https://txnfraudidentification.streamlit.app/)

## Conclusion:

- The project involved analyzing a dataset of online payment transactions to identify patterns associated with fraud. By utilizing machine learning techniques, models were developed to predict whether a transaction is fraudulent based on factors like transaction type, amount, and account balances before and after transactions.
- Limitation: The dataset may not cover all possible scenarios of fraud, which can limit the model's ability to generalize to new, unseen types of fraud.
- Lessons learned are challenges of Imbalanced Data: Addressing the challenge of imbalanced classes in fraud detection taught the critical importance of using the right metrics for evaluating model performance.
- Future Research Direction:  Developing models that can learn from streaming data in real-time would be a significant step forward, allowing for dynamic adaptation to emerging fraud patterns.










































