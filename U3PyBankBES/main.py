# Unit 3 | Assignment - Py Me Up, Charlie
# In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. 
# You will give a set of financial data called budget_data.csv. 
# The dataset is composed of two columns: Date and Profit/Losses. 
# (Thankfully, your company has rather lax standards for accounting so the records are simple.)

# Your task is to create a Python script that analyzes the records to calculate each of the following:
# # # The total number of months included in the dataset
# # # The net total amount of "Profit/Losses" over the entire period
# # # The average of the changes in "Profit/Losses" over the entire period
# # # The greatest increase in profits (date and amount) over the entire period
# # # The greatest decrease in losses (date and amount) over the entire period

import os
import csv

# Locate the "budget_data.csv" and declare it's file path
budgetcsv = os.path.join("U3PyBankBES","budget_data.csv")
# print(budgetcsv)

with open(budgetcsv, newline="") as csvfile:
    budget_data = csv.reader(csvfile, delimiter=",")
    header = next(csvfile)
    total_profit = []
    total_months = []
    average_change = []
    avg = []

    for header in budget_data:
        #add all values to a defined list
        total_months.append(header[0])
        avg.append(header[0])
        total_profit.append(header[1])
        total_profit = list(map(int, total_profit))
        ltp = (len(total_profit))
        if ltp > 1:
            diff = total_profit[ltp-1]-total_profit[ltp-2]
            average_change.append(diff)
    avg.pop(0)
    zipped = list(zip(avg, average_change))

# The total number of months included in the dataset
    for x in zipped:
        if x[1] == max(average_change):
            max_month = (x[0])
    for i in zipped:
        if i[1] ==min(average_change):
            min_month = (i[0])

# The greatest increase in profits (date and amount) over the entire period
#find the max of average_change
greatest_increase = max(average_change)

# The greatest decrease in losses (date and amount) over the entire period
#find the min of average_change
greatest_decrease = min(average_change)


# The total number of months included in the dataset
months = len(total_months)
# The net total amount of "Profit/Losses" over the entire period
profits = sum(total_profit)
# The average of the changes in "Profit/Losses" over the entire period
average_change = round(sum(average_change)/len(average_change),2)

financial_analysis = (
f"Financial Analysis\n"
f"------------------------\n"
f"Total Months: {months}\n"
f"Total: ${profits}\n"
f"Average Change: ${average_change}\n"
f"Greatest Increase in Profits: {max_month} - ${greatest_increase}\n"
f"Greatest Decrease in Profits: {min_month} - ${greatest_decrease}\n"
)

print(financial_analysis)

data_output = os.path.join("U3PyBankBES","financial_analysis.txt")

# export to txt file
with open(data_output, "w") as textfile:
   textfile.write(financial_analysis)