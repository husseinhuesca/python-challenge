import os
import csv
import sys

#Fumction to sum all profit/losses
def sumpandl(pandl):
    cont = 0.0
    for cont2 in pandl:
        cont = cont + float(cont2)
    return cont


udemy_csv = os.path.join("Resources","budget_data.csv")

# Lists to store data
monthyear = []
profitlosses = []

# with open(udemy_csv, newline='', encoding='utf-8') as csvfile:
with open(udemy_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)    
    for row in csvreader:
        # Add month&porfit and profitlosses
        monthyear.append(row[0])
        profitlosses.append(row[1])


print("Financial Analysis")
print("------------------------------------------------------------------------")

#Total periods
print("Total Month: " + str(len(monthyear)))       

#Sum Total periods
sumtotal = sumpandl(profitlosses)
print("Total: $" + str(sumtotal))

floatprofitlosses = []
for row in profitlosses:
    floatprofitlosses.append(float(row))


cont3= 1
cont = 0
difchanges = []
cont1 = 0 
while cont1 <= (len(floatprofitlosses)-2):
    x = floatprofitlosses[cont]
    y = floatprofitlosses[cont3]
    z = y - x
    difchanges.append(z)
    cont3 = cont3 + 1
    cont = cont + 1
    cont1 = cont1 + 1

#Average changes
cont = 0.0
for cont4 in difchanges:
    cont = cont + float(cont4)    
average = cont / len(difchanges)
print ("Average  Change: $" + str(round(average,2)))
    

#Max decrease and increase
max_increase = max(difchanges)
max_decrease = min(difchanges)

maxincrease_index = difchanges.index(max_increase)
dateincrease = monthyear[maxincrease_index + 1]
print("Greatest Increase in Profits: " + dateincrease + " ($" + str(max(difchanges)) + ")")

maxdecrease_index = difchanges.index(max_decrease)
datedecrease = monthyear[maxdecrease_index + 1]
print("Greatest Decrease in Profits: " + datedecrease + " ($" + str(min(difchanges)) + ")")

print("------------------------------------------------------------------------")

#Write new Txt file with the results
sys.stdout = open("Analysis\PyBank_Results.txt", "w")

print("Financial Analysis")
print("------------------------------------------------------------------------")
print("Total Month: " + str(len(monthyear)))    
print("Total: $" + str(sumtotal))
print ("Average  Change: $" + str(round(average,2)))
print("Greatest Increase in Profits: " + dateincrease + " ($" + str(max(difchanges)) + ")")
print("Greatest Decrease in Profits: " + datedecrease + " ($" + str(min(difchanges)) + ")")
print("------------------------------------------------------------------------")
   
sys.stdout.close()