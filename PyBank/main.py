import csv
import os


raw_data = open('budget_data.csv')
csv_reader = csv.reader(raw_data, delimiter=',')

file_heders = next(csv_reader)
print(F"Hearder: {file_heders} ")
count_months = 0
total = 0
previousvalue = 867884
total_changes = 0
G_increase = 0
G_decrease = 0

for row in csv_reader:
    
    count_months += 1
    total = total + int(row[1])
    change = int(row[1])-previousvalue
    total_changes += change
    previousvalue = int(row[1])
    if change > G_increase:
        G_increase = change
        m_increase = row[0]
    if change <G_decrease:
        G_decrease = change
        m_decrease = row[0]    

average = total_changes/ (count_months - 1)
average = str(round(average, 2))
print(F" Total Months: {count_months}, \n Total: {total}, \n Average: {average},\n Greatest Increase in Profits: {m_increase} {G_increase},\n Greatest Decrease in Profits: {m_decrease} {G_decrease}")
with open("out.txt", "w") as f:
    f.write(F" Total Months: {count_months}, \n Total: {total}, \n Average: {average},\n Greatest Increase in Profits: {m_increase} {G_increase},\n Greatest Decrease in Profits: {m_decrease} {G_decrease}")