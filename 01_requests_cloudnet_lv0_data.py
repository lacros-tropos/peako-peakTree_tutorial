# script for downloading data from the cloudnet data portal

import requests
import datetime
import os
from datetime import timedelta, date

save_directory = '/path/to/LV0/data'

uri = 'https://cloudnet.fmi.fi/api/raw-files' # for raw files like RPG binary files
#uri = 'https://cloudnet.fmi.fi/api/files' # e.g. for categorize files

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

start_date = datetime.datetime(2025, 1, 1)
end_date= datetime.datetime(2025, 1, 2)

for single_date in daterange(start_date, end_date):
    print(single_date)
    payload = {'date': f'{single_date.strftime("%Y-%m-%d")}', 'site':'hyytiala', 'instrument':'rpg-fmcw-94'}
    #payload = {'date': f'{single_date.strftime("%Y-%m-%d")}', 'site':'hyytiala', 'product':'classification'}
    #payload = {'date': f'{single_date.strftime("%Y-%m-%d")}', 'site':'leipzig-lim', 'product':'categorize'}
    #payload = {'date': f'{single_date.strftime("%Y-%m-%d")}', 'site':'leipzig-lim', 'product':'classification'}
    metadata = requests.get(uri,payload).json()

    for row in metadata:
        res = requests.get(row['downloadUrl'])
        file_path = os.path.join(save_directory, row['filename'])
        with open(file_path, 'wb') as f:
            f.write(res.content)
        print(f'saved {file_path}')
