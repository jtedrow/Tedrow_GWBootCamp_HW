import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

with open (csvpath, "r") as file:
    election_data = csv.reader(file, delimiter=',')
    election_header = next(election_data)
    
    #Obtain list of all votes, store total number of votes and unique canidates
    canidates = []
    
    for row in election_data:
        canidates.append(row[2])
    
    total_votes = len(canidates)
    canidates_unique = list(set(canidates))
    
    #Count the votes using a for loop
    khan_votes = 0
    li_votes = 0
    otooley_votes = 0
    correy_votes = 0
    
    for vote in canidates:
        if vote == "Khan":
            khan_votes += 1
        elif vote == "Correy":
            correy_votes += 1
        elif vote == "Li":
            li_votes += 1
        elif vote == "O'Tooley":
            otooley_votes += 1
    
    #determine percentages
    khan_percent = khan_votes / total_votes * 100
    li_percent = li_votes / total_votes * 100
    otooley_percent = otooley_votes / total_votes * 100
    correy_percent = correy_votes / total_votes * 100
    
    #determine maximum number of votes
    max_vote = max(khan_votes, li_votes, otooley_votes, correy_votes)
    
    #determine winner with a for loop
    winner = []
    
    if max_vote == khan_votes:
        winner = "Khan"
    elif max_vote == li_votes:
        winner = "Li"
    elif max_vote == otooley_votes:
        winner = "O'Tooley"
    elif max_vote == correy_votes:
        winner = "Correy"
        
    
print(f"""
      Election Results
      ---------------------
      Total Votes: {total_votes:,}
      ---------------------
      Khan: {khan_percent:.1f}% ({khan_votes:,})
      Correy: {correy_percent:.1f}% ({correy_votes:,}) 
      Li: {li_percent:.1f}% ({li_votes:,}) 
      O'Tooley: {otooley_percent:.1f}% ({otooley_votes:,}) 
      ---------------------
      The winner is {winner} with {max_vote:,} votes!
      ---------------------""")

# Open the file using "write" mode. Specify the variable to hold the contents
with open("pypoll_analysis.txt", 'w') as txtfile:
    
    txtfile.write(f"""
Election Results
---------------------
Total Votes: {total_votes:,}
---------------------
Khan: {khan_percent:.1f}% ({khan_votes:,})
Correy: {correy_percent:.1f}% ({correy_votes:,}) 
Li: {li_percent:.1f}% ({li_votes:,}) 
O'Tooley: {otooley_percent:.1f}% ({otooley_votes:,}) 
---------------------
The winner is {winner} with {max_vote:,} votes!
---------------------""")
