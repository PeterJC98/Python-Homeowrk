# -*- coding: utf-8 -*-
"""Instructor Demo: CSV Reader.

This script will use the Pathlib library to set the file path,
use the csv library to read in the file, iterate over each
row of the file to capture employee salaries, calculate min,
max, avg metrics of employee salaries, and write the metrics
to a csv file.
"""

# Import the pathlib and csv library
from pathlib import Path
import csv

# Set the file path
csvpath = Path('../Resources/accounting.csv')

# Initialize variable to hold salaries
salaries = []

# Initialize line_num variable
line_num = 0

# Open the input path as a file object
with open(csvpath, 'r') as csvfile:

    # Print the datatype of the file object
    print(type(csvfile))

    # Pass in the csv file to the csv.reader() function
    # (with ',' as the delmiter/separator) and return the csvreader object
    #remember csv = comma separated values
    csvreader = csv.reader(csvfile, delimiter=',')
    # Print the datatype of the csvreader
    print(type(csvreader))

    # Go to the next row from the start of the file
    # (which is often the first row/header) and iterate line_num by 1
    header = next(csvreader)
    line_num += 1
    # Print the header
    print(f"{header} <---- HEADER")

    # Read each row of data after the header
    for row in csvreader:
        # Print the row
        print(row)
        #remember row returns a list 
        # Set salary variable equal to the value in the 4th column of each row
        salary = int(row[3])
        # Append the row salary value to the list of salaries
        salaries.append(salary)

max_salary = max(salaries)
min_salary = min(salaries)
avg_salary = sum(salaries)/len(salaries)
        
# Print the metrics
print(f'Max salary = {max_salary}, Min salary = {min_salary}, Average salary = {avg_salary:.2f}')

#write a csv file based on some data

# Set the output header
header = ["Max_Salary", "Min_Salary", "Avg_Salary"]
# Create a list of metrics
metrics = [max_salary, min_salary, avg_salary]

# Set the output file path
output_path = Path('output.csv')

# Open the output path as a file object
with open(output_path, 'w') as csvfile:
    # Set the file object as a csvwriter object
    csvwriter = csv.writer(csvfile, delimiter=',')
    # Write the header to the output file
    csvwriter.writerow(header)
    # Write the list of metrics to the output file
    csvwriter.writerow(metrics)