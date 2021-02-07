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
    monthlychangeprofits =0
    #Add a bolean  to correct for the missing numbers when finding the difference for the change in profit
    First = True 
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
        profit.append(int(row[1]))
        #Monthy change
        
        totalprofit = totalprofit + int(row[1])

        #Calculate the average change in profits from month to month. Then calulate the average change in profits
        finalprofit = int(row[1])
        if not First == True:
            monthlychangeprofits = (profit[-1] - profit[-2])
            monthlychange.append(monthlychangeprofits)
        else:
            First = False
        

        #Average change in profits
    averagechangeprofits = sum(monthlychange)/len(monthlychange)

        #Find the change in profits minimum and maximum
    greatestincreaseprofits = max(monthlychange)
    greatestdecreaseprofits = min(monthlychange)

    increasedate = date[monthlychange.index(greatestincreaseprofits)]
    decreasedate = date[monthlychange.index(greatestdecreaseprofits)]
        
        
    print("PyBank Homework")
    print("Financial Analysis")
    print("Total Months: " + str(count))
    print("Total Profits: " + "$" + str(totalprofit))
    print("Average Change: " + "$" + str(int(averagechangeprofits)))
    print("Greatest Increase in Profits: " + str(increasedate) + " ($" + str(greatestincreaseprofits) + ")")
    print("Greatest Decrease in Profits: " + str(decreasedate) + " ($" + str(greatestdecreaseprofits)+ ")")
 

with open('PyBank.txt', 'w') as text:
    
    text.write("PyBank Homework"+ "\n")
    text.write("Financial Analysis"+ "\n")
    text.write("Total Months: " + str(count) + "\n")
    text.write("Total Profits: " + "$" + str(totalprofit) +"\n")
    text.write("Average Change: " + '$' + str(int(averagechangeprofits)) + "\n")
    text.write("Greatest Increase in Profits: " + str(increasedate) + " ($" + str(greatestincreaseprofits) + ")\n")
    text.write("Greatest Decrease in Profits: " + str(decreasedate) + " ($" + str(greatestdecreaseprofits) + ")\n")
    
    

    