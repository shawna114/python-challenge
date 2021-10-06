#Imports modules allowing reading/writing files and counting items
import os
import csv

#Creates empty lists that items can be added to
months = []
total_months = []
total_amount = []
month_change = []
columns = []

#Opens file and identifies that intention is to read only
with open ('C:\\Users\\shawn\\python-challenge\\PyBank\\Resources\\budget_data.csv', 'r') as csvfile:
   
#CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

#Reads the header row first
    csv_header = next(csvreader)

#Stores header row in columns list
    columns = csv_header

#Appends values to appropriate lists for future calculations
    for row in csvreader:
        total_months.append(row[0])
        total_amount.append(int(row[1]))
        months.append(row[0])

#Creates sum function for [Profit/Losses] column and for sum month_change list to average total change
def sum(total_amount):
    total = 0
    for x in total_amount:
        total += x
    return total

#Iterates through rows to identify month change amount; appends value to month_change list.
for i in range(len(total_amount)-1):
   month_change.append(total_amount[i+1]-total_amount[i])

#Calculates average change by referencing the sum of the month_changed list and dividing by count of total_months list - 1
average_change = sum(month_change)/(len(total_months)-1)

#Calculates the max change/uses index to find the corresponding month in the month list
max_increase = max(month_change)
max_month_increase = months[month_change.index(max(month_change)) + 1]

#1. Calculates the min change/uses index to find the corresponding month in the month list
max_decrease = min(month_change)
max_month_decrease = months[month_change.index(min(month_change)) + 1]

#Prints values to terminal/adjusts formats, accounting for negative $ amounts
print('Financial Analysis')
print('----------------------------')
print(f'Total: $' + str('{:,}'.format(sum(total_amount))))
print(f'Total Months: ' + str(len(total_months)))
print(f'Average Change: ' + str('${:,.2f}').format(average_change).replace('$-','-$'))
print(f'Greatest Increase in Profits: ' + str(max_month_increase) + ' ' + str('(${:,})'.format(max_increase).replace('$-','-$')))
print(f'Greatest Decrease in Profits: ' + str(max_month_decrease) + ' ' + str('(${:,})'.format(max_decrease).replace('$-','-$')))

#Specifies path for output file
output_path = os.path.join("C:\\Users\\shawn\\python-challenge\\PyBank", "Analysis", "Financial_Analysis.txt")

#Opens the file using 'write' mode. Specifies the variable to hold the contents
with open(output_path, 'w') as txtfile:

#Initializes txt.writer
    txtwriter = txtfile

#Writes results to .txt file in specified formats (uses '\n' to go to next line)
    txtwriter.write('Financial Analysis \n')
    txtwriter.write('----------------------------\n')
    txtwriter.write(f'Total: $' + str('{:,}\n'.format(sum(total_amount))))
    txtwriter.write(f'Total Months: ' + str(len(total_months)))
    txtwriter.write(f'\nAverage Change: ' + str('${:,.2f}\n').format(average_change).replace('$-','-$'))
    txtwriter.write(f'Greatest Increase in Profits: ' + str(max_month_increase) + ' ' + str('(${:,})\n'.format(max_increase).replace('$-','-$')))
    txtwriter.write(f'Greatest Decrease in Profits: ' + str(max_month_decrease) + ' ' + str('(${:,})\n'.format(max_decrease).replace('$-','-$')))


