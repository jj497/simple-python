import logging
import time

logging.basicConfig(level=logging.NOTSET)

logging.info('Main.py was called')
for i in range(10):
    time.sleep(2)
    logging.debug('Test Debug')
    print('Test print')
logging.info('Main.py logging complete')