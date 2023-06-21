# Importing Modules os and csv
import os
import csv

# Create two lists to store all entries in the csv file and chnage in profit and loss
list_of_entries = []
change_profit_loss = []

# Locating file
csv_budgetdata_file_location = os.path.join('Resources','budget_data.csv')

# Open file (budget_data.csv) and reading entries in file
with open(csv_budgetdata_file_location, encoding='UTF-8') as csvfile:
    entries_in_file = csv.reader(csvfile, delimiter=',')

    #finding header and printing to terminal
    header_in_file = next(entries_in_file)
    print(f"This is the header in the file: {header_in_file}")
    #storing entries in List: list_of_entries
    for entries in entries_in_file:
        print(entries)
        list_of_entries.append(entries)

#total Number of Months        
total_months = len(list_of_entries)

y = int(total_months)
net_total_amount = int(list_of_entries[0][1])
total_change_over_period = 0
greatest_increase_in_profit = 0
greatsest_decrease_in_profit = 0

#Calculate Total, Average Change, Greatest Increase, Greatest Decrease
for y in range(1, y):
    net_total_amount = net_total_amount + int(list_of_entries[y][1])
    change = int(list_of_entries[y][1]) - int(list_of_entries[y-1][1])
    change_profit_loss.append(change)
    total_change_over_period = total_change_over_period + change
    if change > greatest_increase_in_profit:
        greatest_increase_in_profit = change
        location_for_date_profit = y
    if change < greatsest_decrease_in_profit:
        greatsest_decrease_in_profit = change
        location_for_date_loss = y
    # the command below is commented as it is not part of Challenge final requiremnts
    print(str(change_profit_loss[y-1]))

number_changes_over_period = y
average_change_over_period = round (total_change_over_period / y, 2)
date_for_greatest_increase =str(list_of_entries[location_for_date_profit][0])
date_for_greatest_decrease =str(list_of_entries[location_for_date_loss][0])


#writing final analysis to the terminal
print("Financial Analysis\n")
print("---------------------------------\n")
print("Total Months: " + str(total_months) + "\n")
print("Total: $" + str(net_total_amount) +" \n")
#print("Total Change Over Whole Period: $" + str(total_change_over_period))
print("Average Change: $" + str(average_change_over_period) + " \n") 
#print(str(greatest_increase_in_profit))
#print(str(date_for_greatest_increase))
print("Greatest Increase in Profits: " + str(date_for_greatest_increase) + "  ($" + str(greatest_increase_in_profit) +")\n")
#print(str(greatsest_decrease_in_profit))
#print(str(date_for_greatest_decrease))
print("Greatest Decrease in Profits: " + str(date_for_greatest_decrease) + "  ($" + str(greatsest_decrease_in_profit) +")\n")

#Writing final analysis to a text file named Analysis.txt, placed in the Analysis folder
file = open('Analysis/Analysis.txt', 'w')
file.write('Financial Analysis\n\n')
file.write('--------------------------------------------\n\n')
file.write('Total Months: ' + str(total_months))
file.write('\n\nTotal: $' + str(net_total_amount))
file.write('\n\nAverage Change: $' +str(average_change_over_period))
file.write('\n\nGreatest Increase in Profits: ' + str(date_for_greatest_increase) + '  ($' + str(greatest_increase_in_profit)+ ')')
file.write('\n\nGreatest Decrease in Profits: ' + str(date_for_greatest_decrease) + '  ($'+ str(greatsest_decrease_in_profit) +')')
file.close()





    



