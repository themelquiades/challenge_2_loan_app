# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data
along with writing new data to a new CSV file

"""
import csv
from pathlib import Path

def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data


"""Function that writes data into a new CSV file at the path provided.

    Args:
        csvpath (Path): The new csv file path.

    Returns:
        A new CSV file at the specified path containing a list of lists.

    """
def save_csv(csvpath, qualifying_loans):
    csvpath = Path(csvpath)
    with open(csvpath, 'w', newline='') as csvfile:
        csvwriter=csv.writer(csvfile)
        for row in qualifying_loans:
            csvwriter.writerow(row)