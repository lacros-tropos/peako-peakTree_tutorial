# script for downloading data from the cloudnet data portal
# 
# Meanwhile there is a cloudnet api client available
# https://github.com/actris-cloudnet/cloudnet-api-client
# 

import requests
import datetime
import os
from datetime import timedelta, date
from pathlib import Path
import re

save_directory = Path('../data')
save_directory.mkdir(exist_ok=True)

uri = 'https://cloudnet.fmi.fi/api/raw-files' # for raw files like RPG binary files
#uri = 'https://cloudnet.fmi.fi/api/files' # e.g. for categorize files

filename_pattern = r".*LV0" # in the case of the rpg binary files LV0 and LV1 are returned by the request
filename_pattern = r".*_(07|08|09|12)\d{4}_.*LV0" # very limited set of data to improve download speed

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

start_date = datetime.datetime(2024, 1, 14)
end_date= datetime.datetime(2024, 1, 15)

for single_date in daterange(start_date, end_date):
    print(single_date)
    payload = {'date': f'{single_date.strftime("%Y-%m-%d")}', 'site':'hyytiala', 'instrument':'rpg-fmcw-94'}
    #payload = {'date': f'{single_date.strftime("%Y-%m-%d")}', 'site':'hyytiala', 'product':'classification'}
    #payload = {'date': f'{single_date.strftime("%Y-%m-%d")}', 'site':'leipzig-lim', 'product':'categorize'}
    #payload = {'date': f'{single_date.strftime("%Y-%m-%d")}', 'site':'leipzig-lim', 'product':'classification'}
    metadata = requests.get(uri,payload).json()

    for row in metadata:
        if not re.match(filename_pattern, row['filename']):
            continue
        print('downloading... ', row['filename'])
        res = requests.get(row['downloadUrl'])
        file_path = save_directory / row['filename']
        with open(file_path, 'wb') as f:
            f.write(res.content)
        print(f'saved {file_path}')
