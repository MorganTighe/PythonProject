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


#CSV Reading...
with open(import_election_data) as election_data:
    read_csv = csv.reader(election_data)

    #Vote Count Ticker
    vote_count = vote_count + 1

    #Header Row
    header = next(read_csv)
    
    #Looping through the rows
    for rows in read_csv:

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
    

            
        











