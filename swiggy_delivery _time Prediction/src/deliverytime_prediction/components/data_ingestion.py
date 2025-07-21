import os
import sys
from src.deliverytime_prediction.exception import CustomException
from src.deliverytime_prediction.logging import logging
from src.deliverytime_prediction.utils import read_data
import pandas as pd
from sklearn.model_selection import train_test_split

from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path:str = os.path.join("artifacts","train.csv")
    test_data_path:str = os.path.join("artifacts","test.csv")
    raw_data_path:str = os.path.join("artifacts","raw.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        try:
            data = read_data()
            logging.info("Reading Data from database")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            data.to_csv(self.ingestion_config.raw_data_path,index = False,header=True)
            train_set,test_set = train_test_split(data,test_size=0.2,random_state=42)
            data.to_csv(self.ingestion_config.train_data_path,index = False,header=True)
            data.to_csv(self.ingestion_config.test_data_path,index = False,header=True)

            logging.info("Ingestion is completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )


        except Exception as e:
            raise CustomException(e,sys)