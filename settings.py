# -*- coding: utf-8 -*-

import logging
import os
import sys
from logging.config import dictConfig

logging_config = dict(
    version=1,
    formatters={
        'f': {'format':
              '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'}
        },
    handlers={
        'h': {'class': 'logging.StreamHandler',
              'formatter': 'f',
              'level': logging.DEBUG}
        },
    root={
        'handlers': ['h'],
        'level': logging.DEBUG,
        },
)


#网络代理
PROXIES = 'http:100.98.76.31:10240'

PRO_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(PRO_DIR)
if sys.platform == 'win32':
    CHROME_DRIVER = os.path.join(PRO_DIR, './opt/chromedriver.exe')
else:
    CHROME_DRIVER = os.path.join(PRO_DIR, './opt/chromedriver')