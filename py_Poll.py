# The data we need to retrieve.
#   resources/election_results.csv
# 1. The total number of votes cast.
# 2. A commplete list of candidates who recieved votes.
# 3. The percentage of votes each candidate won.
# 4. The total number of votes each candidate won.
# 5. The winner of the election based on popular vote.

# Add our dependencies.
import csv
import os

# Assign a variable to load a file from the path.
file_to_load = os.path.join('resources', 'election_results.csv')

# Create a filename variable to a direct or indirect path to tthe file.
file_to_save = os.path.join('analysis', 'election_analysis.txt')

# Open the election results and read the file.
with open(file_to_load) as election_data:
    #Read the file object with the reader function
    file_reader = csv.reader(election_data)
    
    # Read and print the header row   
    headers = next(file_reader)
    print(headers)

# Using the with statement to open the file as a text file
with open(file_to_save, 'w') as txt_file:

    # Write three countties to the file.
    txt_file.write('Counties in the Election\n------------------------\nArapahoe\nDenver\nJefferson')

#Close the file
txt_file.close()

# Close the file.
election_data.close()