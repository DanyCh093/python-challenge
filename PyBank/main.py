# Despendencies
import csv

# Files to Load
file_to_load = "budget_data.csv"
file_to_output = "output.csv"

Profit_Losses = "Investments"

# Variables to Track
total_months = 0
total_Investments = 0

prev_Investments = 0
Investments_change = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 999999999999999999]

Investments_changes = []

# Read Files
with open(file_to_load) as Investments_data:
    reader = csv.reader(Investments_data)

    # Loop through all the rows of data we collect
        
    headers = next(reader)
        print ('headers')

    for row in reader:
       # Calculate the totals
        total_months = total_months + 1
        total_Investments = total_Investments + int(row [1])
        # print(row)

        # Keep track of changes
        Investments_change = int(row[1]) - prev_Investments
        # print(Investments_change)

        # Reset the value of prev_Investments to the row I completed my analysis
        prev_Investments = int(row[1])
        # print(prev_Investments)

        # Determine the greatest increase
        if (Investments_change > greatest_increase[1]):
            greatest_increase[1] = Investments_change
            greatest_increase[0] = row[0]

        if (Investments_change < greatest_decrease[1]):
            greatest_decrease[1] = Investments_change
            greatest_decrease[0] = row[0]

        # Add to the Investments_changes list
        Investments_changes.append(int(row[1]))

    # Set the Investments average
    revenue_avg = sum(Investments_changes) / len(Investments_changes)
    
    # Show Output
    print()
    print()
    print()
    print("Financial Analysis")
    print("-------------------------")
    print("Total Months: " + str(total_months))
    print("Total Investments: " + "$" + str(total_Investments))
    print("Average Change: " + "$" + str(round(sum(Investments_changes) / len(Investments_changes),2)))
    print("Greatest Increase: " + str(greatest_increase[0]) + " ($" +  str(greatest_increase[1]) + ")") 
    print("Greatest Decrease: " + str(greatest_decrease[0]) + " ($" +  str(greatest_decrease[1]) + ")")
    


# Output Files
with open(file_to_output, "w") as txt_file:
    txt_file.write("Total Months: " + str(total_months))
    txt_file.write("\n")
    txt_file.write("Total Investments: " + "$" + str(total_Investments))
    txt_file.write("\n")
    txt_file.write("Average Change: " + "$" + str(round(sum(Investments_changes) / len(Investments_changes),2)))
    txt_file.write("\n")
    txt_file.write("Greatest Increase: " + str(greatest_increase[0]) + " ($" + str(greatest_increase[1]) + ")") 
    txt_file.write("\n")
    txt_file.write("Greatest Decrease: " + str(greatest_decrease[0]) + " ($" + str(greatest_decrease[1]) + ")")
 


