import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

# Open and read csv file
with open(csvpath, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

# Create my variables/lists I want to use to display the analysis
    total_months = 0
    profit_loss = 0
    change_list = []
    max_increase = 0
    max_decrease = 0

    # Read the header row
    header = next(csvreader)

    # Extract first row to avoid error with int calculations
    first_i = next(csvreader)
    prev_change = int(first_i[1])

    # Loop through the csv rows and calculate measures
    for i in csvreader:

    # Calculate total Months and total Profit/Loss
        total_months += 1
        profit_loss += int(i[1])

        # Calculate monthly changes of Profit/Loss and put it in my change_list[]
        change = int(i[1]) - prev_change
        previous = int(i[1])
        change_list += [change]
        
        # Add largest increase in profits to max_increase value
        if change > max_increase:
            max_increase = change

        # Add smallestest increase in profits to max_decrease value
        if change < max_decrease:
            max_decrease = change

# Calculate the average of the Change
average_change = sum(change_list) / len(change_list)

analysis = (
    f'Financial Analysis\n'
    f'-----------------------------\n'
    f'Total Months: {total_months}\n'
    f'Total: ${profit_loss}\n'
    f'Average Change: ${average_change}\n'
    f'Greatest Increase in Profits: ${max_increase}\n'
    f'Greatest Decrease in Profits: (${max_decrease})\n')

# Export analysis
file_to_output = os.path.join("Analysis", "budget_analysis.txt")

with open(file_to_output, "w") as txt_file:
    txt_file.write(analysis)