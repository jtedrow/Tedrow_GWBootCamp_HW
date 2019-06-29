import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')


with open (csvpath, 'r') as csvfile:
    budget_data = csv.reader(csvfile, delimiter=',')
    budget_header = next(budget_data)

    date_list = []
    profit_list = []
    
    for row in budget_data:
        date_list.append(row[0])
        profit_list.append(int(row[1]))
    
    total_months = len(date_list)
    total_profit = sum(profit_list)
    average = round(total_profit / total_months)
    max_increase = max(profit_list)
    max_increase_index = profit_list.index(max_increase)
    max_increase_month = date_list[max_increase_index]
    max_decrease = min(profit_list)
    max_decrease_index = profit_list.index(max_decrease)
    max_decrease_month = date_list[max_decrease_index]

print(f"""
Financial Analysis
---------------------------------------
Total Months: {total_months}
Total: ${total_profit:,}
Average Change: ${average:,}
Greatest Increase in Profits: {max_increase_month} (${max_increase:,})
Greatest Decrease in Profits: {max_decrease_month} (${max_decrease:,})""")


# Open the file using "write" mode. Specify the variable to hold the contents
with open("pybank_analysis.txt", 'w') as txtfile:
    
    txtfile.write(f"""
Financial Analysis
---------------------------------------
Total Months: {total_months}
Total: ${total_profit:,}
Average Change: ${average:,}
Greatest Increase in Profits: {max_increase_month} (${max_increase:,})
Greatest Decrease in Profits: {max_decrease_month} (${max_decrease:,})""")