import os
import csv

def split_csv(input_file, output_folder, rows_per_file=250):
    """
    Splits a given CSV file into smaller CSV files with a specified number of rows.
    
    :param input_file: Path to the large CSV file to split.
    :param output_folder: Folder where the smaller CSV files will be saved.
    :param rows_per_file: Number of rows in each smaller CSV file.
    """
    with open(input_file, 'r', newline='', encoding='utf-8') as infile:
        csv_reader = csv.reader(infile)
        headers = next(csv_reader)  # Read the header row

        # Initialize variables
        file_count = 1
        rows = []

        for row in csv_reader:
            rows.append(row)
            # If the rows reached the threshold, write them to a new file
            if len(rows) >= rows_per_file:
                output_file = os.path.join(output_folder, f"{os.path.splitext(os.path.basename(input_file))[0]}_part{file_count}.csv")
                with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
                    csv_writer = csv.writer(outfile)
                    csv_writer.writerow(headers)  # Write header to each smaller CSV
                    csv_writer.writerows(rows)    # Write the rows
                rows = []  # Reset rows for next chunk
                file_count += 1

        # Write remaining rows (if any)
        if rows:
            output_file = os.path.join(output_folder, f"{os.path.splitext(os.path.basename(input_file))[0]}_part{file_count}.csv")
            with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
                csv_writer = csv.writer(outfile)
                csv_writer.writerow(headers)
                csv_writer.writerows(rows)

def process_folder(input_folder, output_folder, rows_per_file=250):
    """
    Processes all CSV files in the input folder and splits them into smaller CSV files.
    
    :param input_folder: Folder containing the large CSV files.
    :param output_folder: Folder where the smaller CSV files will be saved.
    :param rows_per_file: Number of rows per smaller CSV file.
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate through each file in the folder
    for filename in os.listdir(input_folder):
        file_path = os.path.join(input_folder, filename)
        
        if os.path.isfile(file_path) and filename.endswith('.csv'):
            print(f"Processing file: {filename}")
            split_csv(file_path, output_folder, rows_per_file)

if __name__ == "__main__":
    input_folder = 'F:/Study/sem 6/Mini Project/TWRSC_2/Two-Wheeler-Road-Surface-Classifier-main/04 Preprocessed Data/FInal Data/Bitumin'  # Replace with your folder containing large CSV files
    output_folder = 'bitumin_processed'  # Replace with your desired output folder
    
    process_folder(input_folder, output_folder)
