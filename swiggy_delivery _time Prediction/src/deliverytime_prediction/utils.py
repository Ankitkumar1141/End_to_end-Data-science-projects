import os
import sys
from src.deliverytime_prediction.exception import CustomException
from src.deliverytime_prediction.logging import logging
import pandas as pd
from dotenv import load_dotenv
import pymysql

load_dotenv()
host = os.getenv("host")
user = os.getenv("user")
password = os.getenv("password")
db = os.getenv("db")

def read_data():
    logging.info("Reading data from database")
    try :
        mydb = pymysql.connect(
            host = host,
            user = user,
            password = password,
            db = db
        )
        logging.info("Connection established")
        data = pd.read_sql_query("select * from swiggy",mydb)
        print(data.head())

        return data
    except Exception as e:
        raise CustomException(e,sys)