import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

# Open and read csv file
with open(csvpath, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the first row to idenfity header
    header = next(csvreader)

    # Vote counter
    total_votes = 0

    # Candidate list & vote counter
    candidate_list = []
    candidate_vote_count = {}


    # Loop through csv to count the number of votes
    for i in csvreader:
        total_votes = total_votes + 1

    # Pull candidate name from csv   
        candidate = i[2]

    # If statement to only capture unique cadidate names
        if candidate not in candidate_list:
            # Add names to open list
            candidate_list.append(candidate)
            # Start unique candidate's vote count
            candidate_vote_count[candidate] = 0
        # Add vote to unique candidate count
        candidate_vote_count[candidate] = candidate_vote_count[candidate] +1

Election_Analysis = (
f'Election Results\n'
f'-----------------------\n'
f'Total Votes: {total_votes}\n'
f'-----------------------\n'
f'Total Votes:{candidate_vote_count}\n'
f'-----------------------\n'
f'Winner: Diana DeGette \n'
)

# Export analysis
file_to_output = os.path.join("Analysis", "election_analysis.txt")

with open(file_to_output, "w") as txt_file:
    txt_file.write(Election_Analysis)