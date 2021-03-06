#importing file and module
import csv
import os

# for some reason, ask BCS said that windows didn't like the os.path.join, but this worked
#Importing and letting it know what to output
import_budget_data ="C:\\Users\\morga\\Repositories\\PythonProject\\PyBank\\Resources\\budget_data.csv"
output_budget_analysis ="C:\\Users\\morga\\Repositories\\PythonProject\\PyBank\\output\\budgetanalysis.txt"


#starter variables
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999]
total_months = 0
month_changing = []

#total_net_change = []
net_total = 0
net_change_tally = []

#reading in the header, placing it outside loop
with open(import_budget_data) as budget_data:
    read_csv = csv.reader(budget_data)
    header = next(read_csv)

    #row ticker
    initial_row = next(read_csv)
    total_months += 1
    net_total += int(initial_row[1])
    previous_net = int(initial_row[1])
    

    for rows in read_csv:
        
        #defining variables and calculating totals
        total_months += 1
        net_total += int(rows[1])

        total_net_change =  int(rows[1]) - previous_net
        previous_net = int(rows[1])
        net_change_tally += [total_net_change]
        month_changing += [rows[0]]

        #finding greatest increase
        if total_net_change > greatest_increase[1]:
            greatest_increase[0]
            greatest_increase[1] = total_net_change

        #finding greatest decrease
        if total_net_change < greatest_decrease[1]:
            greatest_decrease = rows[0]
            greatest_decrease[1] = total_net_change

    #Finding Average Change to complete loop
    net_average = sum(net_change_tally) / len(net_change_tally)


summary = (
    f"Financial Analysis\n"
    f"-------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net_change}\n"
    f"Average  Change: ${net_average:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

#Output in terminal
print(summary)

#Putting results in output folder as .txt
with open(output_budget_analysis, 'w') as txt_file:
    txt_file.write(summary)






