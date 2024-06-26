# Online Payment Fraud Detection

- Author - Priyanka Anumandla
- Semester - Spring'24
- Prepared for UMBC Data Science Master Degree Capstone by Dr Chaojie (Jay) Wang
- GitHub - https://github.com/priyanka903
- LinkedIn - https://www.linkedin.com/in/priyanka-anumandla
- PowerPoint Presentation: https://1drv.ms/p/c/3e38ad4e76a9edce/EbG8vvBEWaxKhlXqMsJPqwAB38s0jblNxCb8qKv-jNa0nw?e=KwzMwP 
- YouTube Video: https://www.youtube.com/watch?v=kyuX8t-dgg0


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