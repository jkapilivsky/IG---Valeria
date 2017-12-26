import sys, logging

def error_handling():
    return '{}, {}, line: {}'.format(sys.exc_info()[0],
                                     sys.exc_info()[1],
                                     sys.exc_info()[2].tb_lineno)

try:
    a+bb
except Exception as err:
    logging.error(error_handling())