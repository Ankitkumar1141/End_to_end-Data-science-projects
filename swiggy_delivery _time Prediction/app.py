from src.deliverytime_prediction.logging import logging
from src.deliverytime_prediction.exception import CustomException
import sys


if __name__ == "__main__":
    logging.info("Execution has started sucessfully")
    try:
        a = 1/0
    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)