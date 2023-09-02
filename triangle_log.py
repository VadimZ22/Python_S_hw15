import logging


logging.basicConfig(filename='tr_log.log.',
                    filemode='a',
                    encoding='utf-8',
                    format='{levelname:<8} - {asctime}. "{name}" функция "{funcName}()" {msg}',
                    style='{',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def log_info(msg: str):
    logger.info(msg)

def log_error(msg: str):
    logger.error(msg)
