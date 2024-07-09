# 🛡️🏦 BankShield: Safeguarding Customer Relationships 

BankShield is a comprehensive bank customer churn prediction project. By utilizing various machine learning algorithms, we aim to identify the best model to predict customer churn and safeguard valuable customer relationships.

## 🏁 Overview 
Customer churn is a critical issue in the banking sector. BankShield aims to predict which customers are likely to leave the bank, allowing for proactive measures to retain them. We have employed multiple machine learning algorithms to find the most effective model for churn prediction.

## ⚙️ Installation 
To run this project locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/mayurd8862/Bank-Customer-Churn-Prediction.git
    ```
2. Navigate to the project directory:
    ```bash
    cd Bank-Customer-Churn-Prediction
    ```
3. Create a virtual environment and activate it:
    ```bash
    python -m venv env
    env\Scripts\activate
    ```
4. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```
5. Train and save best model:
    ```bash
    python test.py
    ```
5. Run User Interface web app:
    ```bash
    python app.py
    ```

## 🔬 Methodology
---
### 5.1. Problem Statement

The problem is to develop a machine learning model that predicts bank customer churn based on various customer attributes and transaction history.

### 5.2. Data

The dataset consists of more than 10,000 data points stored as rows with 14 features in columns. The features include process parameters such as:

- CustomerId: Unique identifier for each customer.
- Surname: Customer's last name.
- CreditScore: Customer's credit score.
- Geography: Country of the customer.
- Gender: Gender of the customer.
- Age: Age of the customer.
- Tenure: Number of years the customer has been with the bank.
- Balance: Account balance of the customer.
- NumOfProducts: Number of bank product facilities customer is using.
- HasCrCard: Whether the customer has a credit card (1: Yes, 0: No).
- IsActiveMember: Whether the customer is an active member (1: Yes, 0: No).
- EstimatedSalary: Estimated salary of the customer.
- Exited: Whether the customer has churned (1: Yes, 0: No).


### 5.3. Algorithms Used 
We implemented and compared the following algorithms to determine the best performer:
1. **Logistic Regression**
2. **K-Neighbors Classifier**
3. **Random Forest Classifier**
4. **AdaBoost Classifier**

### 5.4. Model Comparison 
Each algorithm's performance was evaluated based on accuracy, precision, recall, F1-score, and AUC-ROC curve. The comparison helped identify the most effective model for predicting customer churn.

## 🛠️ Pipeline 
![pipeline](https://github.com/mayurd8862/Bank-Customer-Churn-Prediction/assets/113239727/a13cef81-8a2d-42a0-820b-4aaf11e1f13e)

The MLOps (Machine Learning Operations) pipeline is designed to create an end-to-end workflow for developing and deploying a web application that performs data preprocessing, model training, model evaluation, and prediction. The pipeline leverages Docker containers for encapsulating code, artifacts, and the frontend of the application. The application is deployed on a AWS to provide a cloud hosting solution.

## 🏆 Results 
The results of the different algorithms are compared in terms of their performance metrics. The algorithm with the highest accuracy and best overall metrics is chosen as the final model.

![image](https://github.com/mayurd8862/Bank-Customer-Churn-Prediction/assets/113239727/56b06d9c-45ee-46ab-a42a-a80c2ce7d2fe)

![image](https://github.com/mayurd8862/Bank-Customer-Churn-Prediction/assets/113239727/50fbd851-8f52-483c-9ac4-b747c23cdea5)


## 🤝 Contributing 
Contributions are welcome! Please fork the repository and create a pull request with your changes.

## 📜 License 
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
