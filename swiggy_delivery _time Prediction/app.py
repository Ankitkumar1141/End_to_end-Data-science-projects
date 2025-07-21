from src.deliverytime_prediction.logging import logging
from src.deliverytime_prediction.exception import CustomException
from src.deliverytime_prediction.components.data_ingestion import DataIngestion
from src.deliverytime_prediction.components.data_ingestion import DataIngestionConfig
import sys


if __name__ == "__main__":
    logging.info("Execution has started sucessfully")
    try:
        data_ingestion = DataIngestion()
        data_ingestion.initiate_data_ingestion()
    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)