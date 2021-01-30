#Let's import!
import csv
import os

#files in and out using full path because my computer isn't running os.path.join
#AskBCS helped me get these lines to run
import_election_data ="C:\\Users\\morga\\Repositories\\PythonProject\\PyPoll\\Resources\\election_data.csv"
output_budget_analysis ="C:\\Users\\morga\\Repositories\\PythonProject\\PyPoll\\output\\electionanalysis.txt"

#Counting Votes and defining variables
vote_count = 0
candidatevotes = {}
candidatelist = []
candidatewin = ""
winningballots = 0


#CSV Reading...
with open(import_election_data) as election_data:
    read_csv = csv.reader(election_data)

    #Vote Count Ticker
    vote_count = vote_count + 1

    #Header Row
    header = next(read_csv)
    
    #Looping through the rows
    for rows in read_csv:
         
        vote_count = vote_count + 1

        #defining the candidate names
        candidatenames = rows[2]
         
        #In need of another loop - this will find candidates names
        if candidatenames not in candidatelist:
            candidatelist.append(candidatenames)

            #Let's count some votes per candidate
            candidatevotes[candidatenames] = 0
        
        candidatevotes[candidatenames] = candidatevotes[candidatenames] + 1

        #Testing... It works!
        #print(candidatenames)
        #print(candidatevotes)

#Need to print a .txt - here we go
with open(output_budget_analysis, 'w') as txt_file:

    #Printing Results
    electionresults = (
        f"\n\nElectionResults\n"
        f"--------------------\n"
        f"Total Votes: {vote_count}\n"
        f"--------------------\n"
    )
    print(electionresults)

    #Hopefully adding this to the .txt
    #txt_file.write(electionresults)

    for runner in candidatevotes:
        votes = candidatevotes.get(runner)
        percentage = float(votes) / float(vote_count) * 100
        #Test Line
        #print(percentage)

        #Have to find winner, which means new variables at the top
        if (votes > winningballots):
            winningballots = votes
            candidatewin = runner

        #Print the lines
        totals = f"{runner}: {percentage}% ({votes})\n"
        print(totals, end="")

        #place on csv
        txt_file.write(totals)

    #So who won? Printing result!
    who_won = (
        f"Winner: {candidatewin}\n"
    )
    print(who_won)

    #saving it to CSV (with any luck)
    txt_file.write(who_won)
    







            
        











