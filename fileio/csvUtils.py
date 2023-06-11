"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv
from pathlib import Path

def load_file():
     csvpath=Path(r'./Resources/users_data.csv')
     return load_csv(csvpath)

def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = {}
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data[row[0]]=row[1]
    return data

#Append function created to insert the new user data in csv.
def append_csv(username,password):
    user_list=[]
    user_list.append(username)
    user_list.append(password)
    csvpath=Path(r'./Resources/users_data.csv')
    with open(csvpath,mode="a",newline='') as csvfile:         
        csvwriter=csv.writer(csvfile,delimiter=(','))
        csvwriter.writerow(user_list)
            