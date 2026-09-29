from modules.log_initialise import setup_logging
from datetime import datetime
from modules.run_extract import extract_json

timestamp = datetime.now().strftime("%Y-%m-%d %H-%M-%S")

logger = setup_logging('log', timestamp)
logger.info('Logger successfully initialised')


## API Endpoint we want to extract data from
url = 'https://api.tfl.gov.uk/BikePoint/'
## Create a folder
data_dir = 'data'
## Set up a rety setting in case API fails
max_retry = 5
delay = 10

extract_json(url, data_dir, timestamp, max_retry, delay)