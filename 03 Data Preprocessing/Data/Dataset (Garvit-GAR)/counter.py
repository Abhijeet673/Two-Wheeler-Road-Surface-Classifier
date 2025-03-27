# This script is for counting the dataset

import os
import csv

def count_rows_in_csv_files(folder_path):
    # List all files in the folder
    files = os.listdir(folder_path)
    
    # Filter out only CSV files
    csv_files = [file for file in files if file.endswith('.csv')]
    
    # Dictionary to store the row count for each file
    row_counts = {}
    
    # Iterate over each CSV file
    for csv_file in csv_files:
        file_path = os.path.join(folder_path, csv_file)
        with open(file_path, mode='r', newline='') as file:
            reader = csv.reader(file)
            row_count = sum(1 for row in reader) - 1  # Subtract 1 for header row
            row_counts[csv_file] = row_count
    
    return row_counts

def get_count(folder_path, print_each_csv_count=False, save_to_file=False):
    """
    This function counts the number of rows in all CSV files in a given folder."
    """
    # Check if the folder exists
    if not os.path.exists(folder_path):
        print(f"Folder '{folder_path}' does not exist.")
        return
    # Check if the folder is empty
    if not os.listdir(folder_path):
        print(f"Folder '{folder_path}' is empty.")
        return
    # Get the row counts
    row_counts = count_rows_in_csv_files(folder_path)
    total_data = sum(row_counts.values())
    # Print the row counts
    for csv_file, row_count in row_counts.items():
        if print_each_csv_count:
            print(f'{csv_file}: {row_count} rows')
    print(f'Total data of {folder_path}: {total_data} rows\n')
    # Save the row counts to a file
    if save_to_file:
        output_file = os.path.join(folder_path, 'row_counts.txt')
        with open(output_file, 'w') as file:
            for csv_file, row_count in row_counts.items():
                file.write(f'{csv_file}: {row_count} rows\n')
            file.write(f'Total data of {folder_path}: {total_data} rows\n')
        print(f'Row counts saved to {output_file}')




# Specify the folder path
Concrete = 'Concrete'
MultiSB = 'MultiSB'
SingleSB = 'SingleSB'


# call get_count function for each folder
print('\nCounting the dataset...\n\n')
get_count(Concrete)
get_count(MultiSB)
get_count(SingleSB)
