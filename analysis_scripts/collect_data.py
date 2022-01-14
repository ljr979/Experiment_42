
import os, re
import pandas as pd
import numpy as np
from loguru import logger
import glob
import shutil

#change these for experiment
input_folder = 'experimental_data/Experiment_41/211221_CLIC_control/'
output_folder = 'imagejresults/controls/CLIC/'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

#can change based on proteins in experiment
hsp_colocalised = 'hsp27_coloc_traj'
hsp_noncolocal = 'hsp27_control_traj'
client_colocalised = 'CLIC_coloc_traj'
client_noncolocal ='CLIC_control_traj'


    #change these for the experiment you're using
folders = {
        #t=0
        # '20211207_130401_226exp41_CLIChsp27_t0/Trajectories/Coloc/Hsp/': ('hsp27/zero-hsp27-01/coloc/', hsp_colocalised),
        # '20211207_130401_226exp41_CLIChsp27_t0/Trajectories/non-coloc/Hsp/': ('hsp27/zero-hsp27-01/non-coloc/', hsp_noncolocal),
        # '20211207_130401_226exp41_CLIChsp27_t0/Trajectories/Coloc/Client/': ('CLIC/zero-CLIC-01/coloc/', client_colocalised),
        # '20211207_130401_226exp41_CLIChsp27_t0/Trajectories/non-coloc/Client/': ('CLIC/zero-CLIC-01/non-coloc/', client_noncolocal),
        '20211221_135310_444exp41_CLIC647_t0/Trajectories/': ('zero-CLIC-01/non-coloc/', client_noncolocal),


        # #t=20
        # '20211207_140137_119exp41_CLIChsp27_t20/Trajectories/Coloc/Hsp/': ('hsp27/20min-hsp27-01/coloc/', hsp_colocalised),
        # '20211207_140137_119exp41_CLIChsp27_t20/Trajectories/non-coloc/Hsp/': ('hsp27/20min-hsp27-01/non-coloc/', hsp_noncolocal),
        # '20211207_140137_119exp41_CLIChsp27_t20/Trajectories/Coloc/Client/': ('CLIC/20min-CLIC-01/coloc/', client_colocalised),
        # '20211207_140137_119exp41_CLIChsp27_t20/Trajectories/non-coloc/Client/': ('CLIC/20min-CLIC-01/non-coloc/', client_noncolocal),
        '20211221_144207_380exp41_CLIC647_t20/Trajectories/': ('20min-CLIC-01/non-coloc/', client_noncolocal),

        # #t=40
        # '20211207_151017_583exp41_CLIChsp27_t40/Trajectories/Coloc/Hsp/': ('hsp27/40min-hsp27-01/coloc/', hsp_colocalised),
        # '20211207_151017_583exp41_CLIChsp27_t40/Trajectories/non-coloc/Hsp/': ('hsp27/40min-hsp27-01/non-coloc/', hsp_noncolocal),
        # '20211207_151017_583exp41_CLIChsp27_t40/Trajectories/Coloc/Client/': ('CLIC/40min-CLIC-01/coloc/', client_colocalised),
        # '20211207_151017_583exp41_CLIChsp27_t40/Trajectories/non-coloc/Client/': ('CLIC/40min-CLIC-01/non-coloc/', client_noncolocal),
        '20211221_152000_426exp41_CLIC647_t40/Trajectories/': ('40min-CLIC-01/non-coloc/', client_noncolocal),


        # #t=60
        # '20211207_160623_835exp41_CLIChsp27_t60/Trajectories/Coloc/Hsp/': ('hsp27/60min-hsp27-01/coloc/', hsp_colocalised),
        # '20211207_160623_835exp41_CLIChsp27_t60/Trajectories/non-coloc/Hsp/': ('hsp27/60min-hsp27-01/non-coloc/', hsp_noncolocal),
        # '20211207_160623_835exp41_CLIChsp27_t60/Trajectories/Coloc/Client/': ('CLIC/60min-CLIC-01/coloc/', client_colocalised),
        # '20211207_160623_835exp41_CLIChsp27_t60/Trajectories/non-coloc/Client/': ('CLIC/60min-CLIC-01/non-coloc/', client_noncolocal),
        '20211221_160040_386exp41_CLIC647_t60/Trajectories/': ('60min-CLIC-01/non-coloc/', client_noncolocal),

        # #t=4h
        # '20211207_170404_112exp41_CLIChsp27_t4h/Trajectories/Coloc/Hsp/': ('hsp27/4h-hsp27-01/coloc/', hsp_colocalised),
        # '20211207_170404_112exp41_CLIChsp27_t4h/Trajectories/non-coloc/Hsp/': ('hsp27/4h-hsp27-01/non-coloc/', hsp_noncolocal),
        # '20211207_170404_112exp41_CLIChsp27_t4h/Trajectories/Coloc/Client/': ('CLIC/4h-CLIC-01/coloc/', client_colocalised),
        # '20211207_170404_112exp41_CLIChsp27_t4h/Trajectories/non-coloc/Client/': ('CLIC/4h-CLIC-01/non-coloc/', client_noncolocal),
        '20211221_163905_909exp41_CLIC647_t4h/Trajectories/': ('4h-CLIC-01/non-coloc/', client_noncolocal),


        # #t=7h

        # '20211207_175834_260exp41_CLIChsp27_t7h/Trajectories/Coloc/Hsp/': ('hsp27/7h-hsp27-01/coloc/', hsp_colocalised),
        # '20211207_175834_260exp41_CLIChsp27_t7h/Trajectories/non-coloc/Hsp/': ('hsp27/7h-hsp27-01/non-coloc/', hsp_noncolocal),
        # '20211207_175834_260exp41_CLIChsp27_t7h/Trajectories/Coloc/Client/': ('CLIC/7h-CLIC-01/coloc/', client_colocalised),
        # '20211207_175834_260exp41_CLIChsp27_t7h/Trajectories/non-coloc/Client/': ('CLIC/7h-CLIC-01/non-coloc/', client_noncolocal),
        '20211221_172629_877exp41_CLIC647_t7h/Trajectories/': ('7h-CLIC-01/non-coloc/', client_noncolocal)



        }

for old_folder, (new_folder, filetype) in folders.items():
        old_files = [filename for filename in os.listdir(f'{input_folder}{old_folder}') if '.csv' in filename]
        if not os.path.exists(f'{output_folder}{new_folder}'):
            os.makedirs(f'{output_folder}{new_folder}')
        for x, filename in enumerate(old_files): 
            shutil.copyfile(f'{input_folder}{old_folder}{filename}', f'{output_folder}{new_folder}{filetype}{x}.csv')






