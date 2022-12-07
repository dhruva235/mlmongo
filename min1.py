from sensor.logger import logging
from sensor.exception import SensorException
import sys,os
def test_log_exp():
    logging.info("started")
    try:
        result = 3/0
        print(result)
        logging.info("stopping")
    except Exception as e:
        logging.debug("stopping due to error")
        raise SensorException(e,sys)  


if __name__ == "__main__":
    try:
        test_log_exp()
    except Exception as e:
        print(e)  


