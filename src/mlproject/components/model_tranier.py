import os
import sys
from dataclasses import dataclass
from urllib.parse import urlparse
# import mlflow
# import mlflow.sklearn
import numpy as np


from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
# from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

from src.mlproject.exception import CustomException
from src.mlproject.logger import logging
from src.mlproject.utils import save_object

@dataclass
class ModelTrainerConfig:
    trained_model_file_path=os.path.join("artifacts","model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config=ModelTrainerConfig()

    def evaluate_model(self,actual, pred):
        accuracy = accuracy_score(actual, pred)
        precision = precision_score(actual, pred)
        recall = recall_score(actual, pred)
        f1 = f1_score(actual, pred)
        return accuracy, precision, recall, f1

    def initiate_model_trainer(self,train_array,test_array):
        try:
            logging.info("Split training and test input data")
            X_train,y_train,X_test,y_test=(
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )

            models = {
                "Logistic Regression": LogisticRegression(),
                "K-Neighbors Classifier": KNeighborsClassifier(),
                # "Decision Tree Classifier": DecisionTreeClassifier(),
                "Random Forest Classifier": RandomForestClassifier(),
                "AdaBoost Classifier": AdaBoostClassifier()
            }


            accuracy_dict = {}  # Dictionary to store model accuracies

# Train and evaluate each model
            for model_name, model in models.items():
                model.fit(X_train, y_train)  # Train model
    
    # Make predictions
                y_train_pred = model.predict(X_train)
                y_test_pred = model.predict(X_test)
    
    # Evaluate model
                train_accuracy = accuracy_score(y_train, y_train_pred)
                test_accuracy = accuracy_score(y_test, y_test_pred)
    
                accuracy_dict[model_name] = test_accuracy  # Store test accuracy in dictionary

            best_model_name = max(accuracy_dict, key=accuracy_dict.get)
            best_model_accuracy = accuracy_dict[best_model_name]
            print("Best performing model:", best_model_name)
            print("Accuracy of best performing model:", best_model_accuracy)

            best_model = models[best_model_name]

            if best_model_accuracy<0.6:
                raise CustomException("No best model found")
            logging.info(f"Best found model on both training and testing dataset")

            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )



        except Exception as e:
            raise CustomException(e,sys)
        
