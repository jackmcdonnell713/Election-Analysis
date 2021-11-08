# Data we need to Retrieve 
import csv
import os

#assign a variable to load file from a path
file_to_load = os.path.join("Resources", "election_results.csv")


#assign a variable to save file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

#open and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    headers = next(file_reader)
    print(headers)




# Total number of votes cast
# A complete list of candidates who received votes
# Total number of votes each candidate received
# Percentage of votes each candidate won
# The winner of the election based on popular vote