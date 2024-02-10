from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
from src.mlproject.components.data_ingestion import DataIngestion
from src.mlproject.components.model_tranier import *

from src.mlproject.components.data_transformation import *
import sys


if __name__=="__main__":
    logging.info("The execution has started")


    try:
        data_ingestion=DataIngestion()
        train_data_path,test_data_path=data_ingestion.initiate_data_ingestion()

        data_transformation_config=DataTransformationConfig()
        data_transformation=DataTransformation()
        train_arr,test_arr,_=data_transformation.initiate_data_transormation(train_data_path,test_data_path)

        model_trainer=ModelTrainer()
        print(model_trainer.initiate_model_trainer(train_arr,test_arr))


    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)
    # except Exception as e:
    #     logging.info("Custom exception")
    #     raise CustomException(e,sys)
    
    print("THIS IS DRY RUNNING OF DIFFERENT CLASSES")
