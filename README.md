# 🛡️🏦 BankShield: Safeguarding Customer Relationships 

BankShield is a comprehensive bank customer churn prediction project. By utilizing various machine learning algorithms, we aim to identify the best model to predict customer churn and safeguard valuable customer relationships.

## 🏁 Overview 
Customer churn is a critical issue in the banking sector. BankShield aims to predict which customers are likely to leave the bank, allowing for proactive measures to retain them. We have employed multiple machine learning algorithms to find the most effective model for churn prediction.

## 🤖 Algorithms Used 
We implemented and compared the following algorithms to determine the best performer:
1. **Logistic Regression**
2. **K-Neighbors Classifier**
3. **Random Forest Classifier**
4. **AdaBoost Classifier**

## 📊 Model Comparison 
Each algorithm's performance was evaluated based on accuracy, precision, recall, F1-score, and AUC-ROC curve. The comparison helped identify the most effective model for predicting customer churn.

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

## 🏆 Results 
The results of the different algorithms are compared in terms of their performance metrics. The algorithm with the highest accuracy and best overall metrics is chosen as the final model.

![image](https://github.com/mayurd8862/Bank-Customer-Churn-Prediction/assets/113239727/56b06d9c-45ee-46ab-a42a-a80c2ce7d2fe)

![image](https://github.com/mayurd8862/Bank-Customer-Churn-Prediction/assets/113239727/50fbd851-8f52-483c-9ac4-b747c23cdea5)


## 🤝 Contributing 
Contributions are welcome! Please fork the repository and create a pull request with your changes.

## 📜 License 
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
