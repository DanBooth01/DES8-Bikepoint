## import packages
import requests
import os
import json
from datetime import datetime
import time
import logging

## API Endpoint we want to extract data from
url = 'https://api.tfl.gov.uk/BikePoint/'

## Create a folder
data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)

## Create a timestamp
timestamp = datetime.now().strftime("%Y-%m-%d %H-%M-&S")
filename = f"{data_dir}/{timestamp}.json"

## Create folder
log_dir = 'log'
os.makedirs(log_dir, exist_ok=True)
log_filename = f"{data_dir}/{timestamp}.json"

## Configure logging so messages are written to the log files

logging.basicConfig(
    filename = log_filename,
    format = "%(asctime)s - %(levelname)s - %(message)s",
    level = logging.INFO
)

## Create the logger and confirm that it has been successfully set up

logger = logging.getLogger()
logger.info("Logger successfuly initialised")

## Set up a rety setting in case API fails

max_retry = 5
attempt = 0
delay = 10


## Keep trying until the max number of attempts is reached

while attempt < max_retry:

    ## Send GET request to API
    response = requests.get(url)
    ## Get Response
    status =  response.status_code

    ## Write an if statement based on status code

    if 200 <= status <300:
        ## Convert the JSON response
        data = response.json()

        ## Check API returns data before trying to save it

        if len(data)>0:

            try:
                ##Open the output file and write the API data to it as a JSON
                with open(filename, 'w') as file:
                    json.dump(data, file)

                print(f"File {filename} was successfully saved")

                ##Add logger info
                logger.info(f"File {filename} was successfully saved")

            except Exception as e:
                print(f"An error has occured: {e}")
                logger.error(f"An error has occured: {e}")

            break

        # API request succeeded but no data returned
        else: 
            print("No data returned")
            logger.warning("No data returned")
            break

    elif status < 200 or status >=500:
                #Wait before retying to avoid repeatadly hitting the API
        time.sleep(delay)
        attempt += 1
        print(f"Status code: {status}, retrying attempt number {attempt}")
        logger.info(f"Status code: {status}, retrying attempt number {attempt}")


    else:
        print(f"Error. Status code {status}. Fix it")
        logger.critical(f"Error. Status code {status}. Fix it")
        break
