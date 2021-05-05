# The data we need to retrieve
# 1. The total number of votes case
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

import csv
import os

#Assign a variable to load a file from a path
file_to_load = os.path.join("election_results.csv")

#Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file
with open(file_to_load) as election_data:

     # Read the file object with the reader function.
     file_reader = csv.reader(election_data)
     
# Print each row in the CSV file
     headers = next(file_reader)
     print(headers)
# Using the with statement open the file as a text file.
#with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    #txt_file.write("Arapahoe, ")
    #txt_file.write("Denver, ")
    #txt_file.write("Jefferson")
    #txt_file.write("Counties in the Election\n---------------\nArapahoe\nDenver\nJefferson")
# Close the file
#txt_file.close()