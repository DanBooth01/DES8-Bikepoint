## import packages
import requests
import os
import json
from datetime import datetime

## API Endpoint we want to extract data from
url = 'https://api.tfl.gov.uk/BikePoint/'

## Create a folder
data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)

## Create a timestamp
timestamp = datetime.now().strftime("%Y-%m-%d %H-%M-&S")
filename = f"{data_dir}/{timestamp}.json"

## Send GET request to API
response = requests.get(url)
## Get Response
status =  response.status_code



## Convert the JSON response
data = response.json()

##Open the output file and write the API data to it as a JSON

with open(filename, 'w') as file:
    json.dump(data, file)
