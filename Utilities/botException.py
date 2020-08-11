import logging
import datetime

logging.basicConfig(filename="../BotIn.log", level=logging.INFO)
class MissingWebDriver(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.message = args[0]
        logging.error(f"{self.message} at {datetime.datetime.now()}")
        

    def __str__(self):
        return (f"{self.message} \n--> Please define a webdriver ")

