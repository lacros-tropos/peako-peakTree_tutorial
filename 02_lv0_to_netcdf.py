# script for converting binary rpg radar files to netcdf using rpgpy

import glob
import os
from pathlib import Path
from rpgpy import rpg2nc

#files = glob.glob('/path/to/LV0/files/*.LV0', recursive=True)
files = list(Path('../data/').glob('*.LV0'))
files.sort()
print(files)

for fin in files:
    fout = fin.with_suffix(fin.suffix + '.nc')
    if not os.path.isfile(fout):
        print(f'processing file {fin}...')
        try:
            rpg2nc(fin, fout)
            print(f'wrote file {fout}')
        except:
            print(f'problem with file {fin}')
    else:
        print(f'file already exists: {fout}')
