
import os, re
import pandas as pd
import numpy as np
from loguru import logger
import glob
import shutil

#change these for experiment
input_folder = 'raw_data/Experiment42/20220113_complexes/'
output_folder = 'imagejresults/complexes/'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

#can change based on proteins in experiment
hsp_colocalised = 'hsp27_coloc_traj'
hsp_noncolocal = 'hsp27_non-coloc_traj'
client_colocalised = 'Rhodanese_coloc_traj'
client_noncolocal ='Rhodanese_non-coloc_traj'


    #change these for the experiment you're using
folders = {
        #t=0
        '20220113_experiment42_t0/Trajectories/Coloc/Hsp/': ('hsp27/zero-hsp27-01/coloc/', hsp_colocalised),
        '20220113_experiment42_t0/Trajectories/non-coloc/Hsp/': ('hsp27/zero-hsp27-01/non-coloc/', hsp_noncolocal),
        '20220113_experiment42_t0/Trajectories/Coloc/Client/': ('Rhodanese/zero-Rhodanese-01/coloc/', client_colocalised),
        '20220113_experiment42_t0/Trajectories/non-coloc/Client/': ('Rhodanese/zero-Rhodanese-01/non-coloc/', client_noncolocal),



        # #t=20
        '20220113_experiment42_t20/Trajectories/Coloc/Hsp/': ('hsp27/20min-hsp27-01/coloc/', hsp_colocalised),
        '20220113_experiment42_t20/Trajectories/non-coloc/Hsp/': ('hsp27/20min-hsp27-01/non-coloc/', hsp_noncolocal),
        '20220113_experiment42_t20/Trajectories/Coloc/Client/': ('Rhodanese/20min-Rhodanese-01/coloc/', client_colocalised),
        '20220113_experiment42_t20/Trajectories/non-coloc/Client/': ('Rhodanese/20min-Rhodanese-01/non-coloc/', client_noncolocal),
        #'20211221_144207_380exp41_CLIC647_t20/Trajectories/': ('20min-CLIC-01/non-coloc/', client_noncolocal),

        # #t=40
        '20220113_experiment42_t40/Trajectories/Coloc/Hsp/': ('hsp27/40min-hsp27-01/coloc/', hsp_colocalised),
        '20220113_experiment42_t40/Trajectories/non-coloc/Hsp/': ('hsp27/40min-hsp27-01/non-coloc/', hsp_noncolocal),
        '20220113_experiment42_t40/Trajectories/Coloc/Client/': ('Rhodanese/40min-Rhodanese-01/coloc/', client_colocalised),
        '20220113_experiment42_t40/Trajectories/non-coloc/Client/': ('Rhodanese/40min-Rhodanese-01/non-coloc/', client_noncolocal),
        #'20211221_152000_426exp41_CLIC647_t40/Trajectories/': ('40min-CLIC-01/non-coloc/', client_noncolocal),


        # #t=60
        '20220113_experiment42_t60/Trajectories/Coloc/Hsp/': ('hsp27/60min-hsp27-01/coloc/', hsp_colocalised),
        '20220113_experiment42_t60/Trajectories/non-coloc/Hsp/': ('hsp27/60min-hsp27-01/non-coloc/', hsp_noncolocal),
        '20220113_experiment42_t60/Trajectories/Coloc/Client/': ('Rhodanese/60min-Rhodanese-01/coloc/', client_colocalised),
        '20220113_experiment42_t60/Trajectories/non-coloc/Client/': ('Rhodanese/60min-Rhodanese-01/non-coloc/', client_noncolocal),
        #'20211221_160040_386exp41_CLIC647_t60/Trajectories/': ('60min-CLIC-01/non-coloc/', client_noncolocal),

        # #t=4h
        '20220113_experiment42_t4h/Trajectories/Coloc/Hsp/': ('hsp27/4h-hsp27-01/coloc/', hsp_colocalised),
        '20220113_experiment42_t4h/Trajectories/non-coloc/Hsp/': ('hsp27/4h-hsp27-01/non-coloc/', hsp_noncolocal),
        '20220113_experiment42_t4h/Trajectories/Coloc/Client/': ('Rhodanese/4h-Rhodanese-01/coloc/', client_colocalised),
        '20220113_experiment42_t4h/Trajectories/non-coloc/Client/': ('Rhodanese/4h-Rhodanese-01/non-coloc/', client_noncolocal),
        #'20211221_163905_909exp41_CLIC647_t4h/Trajectories/': ('4h-CLIC-01/non-coloc/', client_noncolocal),


        # #t=7h

        '20220114_experiment42_7h/Trajectories/Coloc/Hsp/': ('hsp27/7h-hsp27-01/coloc/', hsp_colocalised),
        '20220114_experiment42_7h/Trajectories/non-coloc/Hsp/': ('hsp27/7h-hsp27-01/non-coloc/', hsp_noncolocal),
        '20220114_experiment42_7h/Trajectories/Coloc/Client/': ('Rhodanese/7h-Rhodanese-01/coloc/', client_colocalised),
        '20220114_experiment42_7h/Trajectories/non-coloc/Client/': ('Rhodanese/7h-Rhodanese-01/non-coloc/', client_noncolocal),
        #'20211221_172629_877exp41_CLIC647_t7h/Trajectories/': ('7h-CLIC-01/non-coloc/', client_noncolocal)



        }

for old_folder, (new_folder, filetype) in folders.items():
        old_files = [filename for filename in os.listdir(f'{input_folder}{old_folder}') if '.csv' in filename]
        if not os.path.exists(f'{output_folder}{new_folder}'):
            os.makedirs(f'{output_folder}{new_folder}')
        for x, filename in enumerate(old_files): 
            shutil.copyfile(f'{input_folder}{old_folder}{filename}', f'{output_folder}{new_folder}{filetype}{x}.csv')






