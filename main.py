import csv
import requests
import configparser
import json
import time
import os
from file_operations import read_csv_file, create_txt_file_if_not_exists
from config import create_config
config_file = 'config.ini'

if not os.path.exists(config_file):
    create_config(config_file)
            
txt_file_path = input('Enter the path to the txt file to save: ')
create_txt_file_if_not_exists(txt_file_path)
prompt = input('Enter the prompt: ')
file_path = input('Enter the path to the csv file with questions: ')
read_csv_file(file_path,txt_file_path,prompt)
# Prompt the user to enter the path to the txt file where the results will be saved

