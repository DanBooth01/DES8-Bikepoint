import requests
import time
import json
import logging
import os

logger = logging.getLogger(__name__)

def extract_json(url, data_dir, timestamp, max_retry, delay):
    """Extracts JSON from specified URL

    Args:
        url (_type_): The url you want to download
        data_dir (_type_): Where to save the data
        timestamp (_type_): The filename will be this
        max_retry (_type_): The number of time to retry the API
        delay (_type_): _description_
    """
    ## Keep trying until the max number of attempts is reached

    os.makedirs(data_dir, exist_ok=True)
    filename = f"{data_dir}/{timestamp}.json"

    attempt = 0

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
