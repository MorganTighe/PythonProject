#importing file and module
import csv
import os

import_budget_data = os.path.join("Resources", "budget_data.csv")
output_budget_analysis = os.path.join("output", "budgetanalysis.txt")

#starter variables
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999]
total_months = 0
month_changing = []
total_months = 0
total_net_change = []
net_total = 0

#reading in the header, placing it outside loop
with open(import_budget_data) as budget_data:
    read_csv = csv.reader(budget_data)

    header = next(read_csv)

    #row ticker
    initial_row = next(read_csv)
    total_months += 1
    net_total += int(first_row[1])
    previous_net = int(first_row[1])

    for rows in read_csv:
        
        #defining variables and calculating totals
        start_net = int(row[1])
        net_total += int(row[1])
        total_months += 1
        total_net_change += 1
        month_changing += [row[0]]  

        #finding the change in net
        start_net = int(row[1])
        net_change = int(row[1]) - start_net
        total_net_change += [net_change]

        #finding greatest increase
        if net_change > greatest_increase[1]:
            greatest_increase[0]
            greatest_increase[1] = net_change

        #finding greatest decrease
        if net_change < greatest_decrease[1]:
            greatest_decrease = row[0]
            greatest_decrease[1] = net_change

summary = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net_change}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

# Print the output (to terminal)
print(summary)

# Export the results to text file
with open(output_budget_analysis, 'w') as txt_file:
    txt_file.write(summary)






