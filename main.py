import logging
import time

logging.info('Main.py was called')
for i in range(50):
    time.sleep(2)
    logging.debug('Test Debug')
    print('Test print')
logging.info('Main.py logging complete')