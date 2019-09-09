# In this challenge, you are tasked with helping a small, rural town modernize its vote-counting process. (Up until now, Uncle Cleetus had been trustfully tallying them one-by-one, but unfortunately, his concentration isn't what it used to be.)

# You will be give a set of poll data called election_data.csv. The dataset is composed of three columns: Voter ID, County, and Candidate. Your task is to create a Python script that analyzes the votes and calculates each of the following:

# The total number of votes cast

# A complete list of candidates who received votes

# The percentage of votes each candidate won

# The total number of votes each candidate won

# The winner of the election based on popular vote.



import os
import csv

# Locate the "election_data.csv" and declare it's file path
electioncsv = os.path.join("U3PyPollBES","election_data.csv")
# print(budgetcsv)

total_votes = []
candidate_name = []
unique = []
vote_count = []

with open(electioncsv, newline="") as csvfile:
    election_data = csv.reader(csvfile, delimiter=",")
    header = next(csvfile)


    for row in election_data:
        total_votes.append(row[0])
        candidate_name.append(row[2])

    for x in candidate_name:
        if x not in unique:
            unique.append(x)

# A complete list of candidates who received votes
print(unique)

# The total number of votes cast
votes = (len(total_votes))
khan_count = candidate_name.count("Khan")
correy_count = candidate_name.count("Correy")
li_count = candidate_name.count("Li")
tooley_count = candidate_name.count("O'Tooley")

# The percentage of votes each candidate won
khan_percent = round(khan_count/votes*100, 3)
li_percent = round(li_count/votes*100, 3)
correy_percent = round(correy_count/votes*100, 3)
tooley_percent = round(tooley_count/votes*100, 3)

# The winner of the election based on popular vote.
winner = max(khan_count, li_count, correy_count, tooley_count)
if winner == khan_count:
    winner_name = "Khan"
elif winner == li_count:
    winner_name = "Li"
elif winner == correy_count:
    winner_name = "Correy"
elif winner == tooley_count:
    winner_name = "O'Tooley"

election_results = (
f"Election Results\n"
f"-------------------------------\n"
# The total number of votes each candidate won
f"Total Votes: {votes}\n"
"-------------------------------\n"
f"Khan: {khan_percent}%, {khan_count} Votes\n"
f"Correy: {correy_percent}%, {correy_count} Votes\n"
f"Li: {li_percent}%, {li_count} Votes\n"
f"O'Tooley: {tooley_percent}%, {tooley_count} Votes\n"
f"-------------------------------\n"
f"Winner: {winner_name}\n"
f"-------------------------------\n"
)
print(election_results)

data_output = os.path.join("U3PyPollBES","election_results.txt")

# export to txt file
with open(data_output, "w") as textfile:
   textfile.write(election_results)
