from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
import sys


if __name__=="__main__":
    logging.info("The execution has started")


    try:
        a = 1/0

    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)
    # except Exception as e:
    #     logging.info("Custom exception")
    #     raise CustomException(e,sys)
    
    print("Hello mayur, Code is still working afeter getting custom exception")

#     try:
#         # #data_ingestion_config=DataIngestionConfig()
#         data_ingestion=DataIngestion()
#         train_data_path,test_data_path=data_ingestion.initiate_data_ingestion()

#         # data_transformation_config=DataTransformationConfig()
#         data_transformation=DataTransformation()
#         train_arr,test_arr,_=data_transformation.initiate_data_transormation(train_data_path,test_data_path)

#         # ## Model Training

#         model_trainer=ModelTrainer()
#         print(model_trainer.initiate_model_trainer(train_arr,test_arr))
#         # a = 1/00
        
#     except Exception as e:
#         logging.info("Custom Exception")
#         raise CustomException(e,sys)