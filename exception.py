from flask import Flask
from src.logger import logging
from src.exception import CustomException
import os, sys

app = Flask(__name__)

@app.route('/', methods= ['GET', 'POST'])
def index():
    try:
        raise Exception("We are testion our Exception file")
    except Exception as e:
        ml = CustomException(e, sys)
        logging.info(ml.error_message)
        
    logging.info("We are testing our logging file.")
    return "Successfull"

if __name__ == '__main__':
    app.run(debug= True)

