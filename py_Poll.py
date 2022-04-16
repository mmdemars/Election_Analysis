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

# Initialize the total vote counter.
total_votes = 0

# Candidate options
candidate_options = []
# Declare the empty dictionary
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ''
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    #Read the file object with the reader function
    file_reader = csv.reader(election_data)
    
    # Read the header row.   
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes +=1
        # Print the candidate name from each row
        candidate_name = row[2]
        # If the candidate does not match any existaing candidate...
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list
            candidate_options.append(candidate_name)
            # Begin tracking the candidates vote count
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1
       
    
# Determine the pecentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list
for candidate_name in candidate_votes:
    # 2. Retrieve vote count of a candidate
    votes = candidate_votes[candidate_name]
    # 3. Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
     # ASK DURING OFFICE HOURS WHY THIS IS ONLY WORKING WITH THE PLAY BUTTON THIS IS STUPID
    
    # print(f'{candidate_name}: received {vote_percentage:.2f}% of the vote.')
    # print('CODE TEST')
     #Determine winning vote count and candidates
    # 1. Determine if the votes are greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # 2 If true then set winning_count = votes and winning_percentage = vote_percentage
        winning_count = votes
        winning_percentage = vote_percentage
        # 3 Set the winning_candidate equal to the candidates name.
        winning_candidate = candidate_name
        # TO DO:  Print the candidate name and percentage of votes to the terminal
    print(f'{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n')
winning_candidate_summary = (f'-*-*---------------------*-*-\n' f'Winner: {winning_candidate}\n' f'Winning Vote Count: {winning_count:,}\n' f'Winning Percentage: {winning_percentage:.1f}%\n' f'-*-*---------------------*-*-\n')
print(winning_candidate_summary)

# print('serial killer run run run away')
# Print the candidate vote dictionary
# print(candidate_votes)

# Print the candidate list
# print(candidate_options)

# Print the total votes.
# print(total_votes)


# Using the with statement to open the file as a text file
with open(file_to_save, 'w') as txt_file:

    # Write three countties to the file.
    txt_file.write('Counties in the Election\n------------------------\nArapahoe\nDenver\nJefferson')

#Close the file
txt_file.close()

# Close the file.
election_data.close()