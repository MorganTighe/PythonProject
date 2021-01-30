#Let's import!
import csv
import os

#files in and out using full path because my computer isn't running os.path.join
#AskBCS helped me get these lines to run
import_election_data ="C:\\Users\\morga\\Repositories\\PythonProject\\PyPoll\\Resources\\election_data.csv"
output_budget_analysis ="C:\\Users\\morga\\Repositories\\PythonProject\\PyPoll\\output\\electionanalysis.txt"

#Counting Votes and defining variables
vote_count = 0



#CSV Reading...
with open(import_election_data) as election_data:
    read_csv = csv.reader(election_data)

    #Header Row
    header = next(read_csv)

    vote_count = vote_count = 1

    print(vote_count)








