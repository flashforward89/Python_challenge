# In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.
import os
import csv

# Path for csv file

PyPollcsv = os.path.join("Resources","election_data.csv")

# Lists to store data

count = 0
candidatelist = []
unique_candidate = []
vote_count = []
vote_percent = []

# Open the CSV using the set path PyPollcsv

with open(PyPollcsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    
    for row in csvreader:
        # Count the total number of votes
        count = count + 1
        # Add the candidate names to candidatelist
        candidatelist.append(row[2])
        
    for x in set(candidatelist):
        unique_candidate.append(x)
        # y is the total number of votes per candidate
        y = candidatelist.count(x)
        vote_count.append(y)
        # z is the percent of total votes per candidate
        z = round ((y/count)*100)
        vote_percent.append(z)
        
    winning_vote_count = max(vote_count)
    winner = unique_candidate[vote_count.index(winning_vote_count)]
    
print("Election Results")   
print("Total Votes :" + str(count))    
for i in range(len(unique_candidate)):
            print(unique_candidate[i] + ": " + str(vote_percent[i]) +"% (" + str(vote_count[i])+ ")")
print("The winner is: " + winner)

# Print to a text file: election_results.txt

with open('election_results.txt', 'w') as text:
    text.write("Election Results\n")
    text.write("Total Vote: " + str(count) + "\n")
    for i in range(len(set(unique_candidate))):
        text.write(unique_candidate[i] + ": " + str(vote_percent[i]) +"% (" + str(vote_count[i]) + ")\n")
    text.write("The winner is: " + winner + "\n")
        
