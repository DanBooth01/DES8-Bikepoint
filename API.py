## import packages
import requests
import os
import json
from datetime import datetime
import time

## API Endpoint we want to extract data from
url = 'https://api.tfl.gov.uk/BikePoint/'

## Create a folder
data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)

## Create a timestamp
timestamp = datetime.now().strftime("%Y-%m-%d %H-%M-&S")
filename = f"{data_dir}/{timestamp}.json"

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

        ##Open the output file and write the API data to it as a JSON
        with open(filename, 'w') as file:
            json.dump(data, file)

        print(f"File {filename} was successfully saved")
        break

    elif status < 200 or status >=500:
                #Wait before retying to avoid repeatadly hitting the API
        time.sleep(delay)
        attempt += 1
        print(f"Status code: {status}, retrying attempt number {attempt}")


    else:
        print(f"Error. Status code {status}. Fix it")
        break