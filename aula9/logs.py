#!/usr/bin/env python3
import logging

logging.basicConfig(
    loggingfilename='app.log',
    level=logging.DEBUG,
    format='%(asctime)s [%(levelname)s] %(name)s' + '[%(funcName)s] [%(filename)s %(lineno)s %(message)s]',
    datefmt = '%d/%m/%Y %H:%M:%S'
)

logging.debbug('Batata')
