from datetime import datetime as dt
import logging

def info_logger(info):
    time = dt.now().strftime('%D_%H:%M')
    with open ('phonebook_log.csv', 'a', encoding="utf-8") as file:
        file.write('{};phonebook;{}\n'
                    .format(time, info))

logging.basicConfig(
    level=logging.INFO,
    filename='phonebook_log.csv',
    format='[%(asctime)s] [%(levelname)s] [%(module)s] [%(funcName)s: %(lineno)d] => %(message)s',
    datefmt='%d.%m.%Y %H:%M:%S ',
)