#Your task is to create a Python script that analyzes the records to calculate each of the following:

#Importing os and csv
import os
import csv

# Path to collect data from the Resources folder
budgetcsv = os.path.join('Resources', 'budget_data.csv')

#The total number of months included in the dataset

#opening the CSV file
with open(budgetcsv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header=next(csvreader)

#Defining lists and variables
    count =0
    profit = []
    totalprofit = 0
    monthlychange = []
    date = []
    initialprofit = 0
    totalchangeinprofits=0  

    # #The net total amount of "Profit/Losses" over the entire period

    # #Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes

    # #The greatest increase in profits (date and amount) over the entire period

    # #The greatest decrease in losses (date and amount) over the entire period

        # Conducting the 
    for row in csvreader:    
        # Use count to count the number months in this dataset
        count = count + 1 
        date.append(row[0])

        # Calucalting total profits
        profit.append(row[1])
        totalprofit = totalprofit + int(row[1])

        #Calculate the average change in profits from month to month. Then calulate the average change in profits
        finalprofit = int(row[1])
        monthlychangeprofits = finalprofit - initialprofit

        #Creating a list for monthly changes
        monthlychange.append(monthlychangeprofits)

        totalchangeinprofits = totalchangeinprofits + monthlychangeprofits
        initialprofit = finalprofit

        #Average change in profits
        averagechangeprofits = (totalchangeinprofits/count)
        
        #Find the change in profits minimum and maximum
        greatestincreaseprofits = max(monthlychange)
        greatestdecreaseprofits = min(monthlychange)

        increasedate = date[monthlychange.index(greatestincreaseprofits)]
        decreasedate = date[monthlychange.index(greatestdecreaseprofits)]
        
        
    print("PyBank")
    

    

with open('PyBank.txt', 'w') as text:
    
    text.write("PyBank"+ "\n")
    

    