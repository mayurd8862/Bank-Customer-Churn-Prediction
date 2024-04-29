from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
from src.mlproject.components.data_ingestion import DataIngestion
from src.mlproject.components.model_tranier import *

from src.mlproject.components.data_transformation import *
import sys

from src.mlproject.pipelines.prediction_pipeline import CustomData, PredictPipeline

import pandas as pd
from src.mlproject.exception import CustomException
from src.mlproject.utils import load_object


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

        data = CustomData(619,'France','Female',51,2,0,1,1,1013478)
        pred_df = data.get_data_as_data_frame()

        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)
        # results = float(results)
        if results[0]==1:
            print("YES") 
        else:
            print("NO")


    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)
    # except Exception as e:
    #     logging.info("Custom exception")
    #     raise CustomException(e,sys)
    
    print("THIS IS DRY RUNNING OF DIFFERENT CLASSES")


