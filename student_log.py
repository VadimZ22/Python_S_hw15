import logging

FORMAT = '{levelname:<8} - {asctime}. "{name}" функция "{funcName}()" {msg}'

logging.basicConfig(filename='st_log.log.', filemode='a',
                    encoding='utf-8', format=FORMAT, style='{', level=logging.INFO)
logger = logging.getLogger(__name__)

def log_info(msg: str):
    logger.info(msg)

def log_error(msg: str):
    logger.error(msg)
