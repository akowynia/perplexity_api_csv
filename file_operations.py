import csv
import time
from get_perplexity import get_perplexity
import os

def read_csv_file(file_path, save_path, prompt):
    """
    Reads a CSV file, processes each row, and writes the results to a text file.

    Args:
        file_path (str): The path to the input CSV file.
        save_path (str): The path to the output text file.
        prompt (str): The prompt to be used for the get_perplexity function.
    """
    with open(file_path, mode='r', newline='') as file:
        csv_reader = csv.reader(file, delimiter=';')
        for row in csv_reader:
            print(row[1])
            time.sleep(10)  # Wait for 10 seconds between processing each row
            print("Waiting for 10 seconds")
            message = get_perplexity(row[1], prompt)

            # Format the output message
            form = "***\n **" + row[1] + "**" + '\n\n' + message + '\n ***'
            with open(save_path+".txt", 'a') as output_file:
                output_file.write(form + '\n')

def create_txt_file_if_not_exists(save_path):
    """
    Creates a text file if it does not already exist.

    Args:
        save_path (str): The path to the text file to be created.
    """
    try:
        # Remove the file extension if it exists
        save_path = os.path.splitext(save_path)[0]


        with open(save_path+".txt", 'x') as file:
            pass  # File created successfully
    except FileExistsError:
        pass  # File already exists, do nothing