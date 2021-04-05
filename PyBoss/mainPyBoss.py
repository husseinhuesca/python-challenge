import os
import csv
import sys


udemy_csv = os.path.join("Resources","employee_data.csv")

# Lists to store data
EmployeeID = []
Name = []
DOB = []
SSN = []
State = []

# with open(udemy_csv, newline='', encoding='utf-8') as csvfile:
with open(udemy_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)    
    for row in csvreader:
        # Add columns to lists
        EmployeeID.append(row[0])
        Name.append(row[1])
        DOB.append(row[2])
        SSN.append(row[3])
        State.append(row[4])


#Name-----------------------------
NewName = []
Newname1 = []
FirstName= []
LastName= []

for row in Name:    
    NewName = row.split(" ",1)
    Newname1.append(NewName)
for row in Newname1:
    FirstName.append(row[0])
for row in Newname1:
    LastName.append(row[1]) 
    

#DOB-----------
NewDOB = []
NewDOB1 = []
DOB_Year= []
DOB_Month= []
DOB_Day = []
DOB_New2 = []

for row in DOB:    
    NewDOB = row.split("-",2)
    NewDOB1.append(NewDOB)
for row in NewDOB1:
    DOB_Year.append(row[0])
for row in NewDOB1:
    DOB_Month.append(row[1]) 
for row in NewDOB1:
    DOB_Day.append(row[2]) 

cont = 0
for row in NewDOB1:
    DOB_New2.append(str(DOB_Month[cont]) + "/"+str(DOB_Day[cont])+ "/" +str(DOB_Year[cont]))
    cont = cont + 1
  
#SSN----------

NewSSN = []
NewSSN1 = []
SSNLast= []

for row in SSN:    
    NewSSN = row.split("-",2)
    NewSSN1.append(NewSSN) 
for row in NewSSN1:
    SSNLast.append("***-**-" +str(row[2])) 


#Dic----------
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

NewState = []
NewStateAbb = []
for row in State:    
    NewState = us_state_abbrev.get(row)
    NewStateAbb.append(NewState) 


print("------------------------------------------------------------------------")

#Create a new CSV file
# Zip all  lists together into tuples
finalfile = zip(EmployeeID, FirstName, LastName, DOB_New2, SSNLast, NewStateAbb)

# save the output file path
output_file = os.path.join("Analysis","finalPyBoss.csv")

# open the output file, create a header row, and then write the zipped object to the csv
with open(output_file, "w", newline='') as datafile:
    writer = csv.writer(datafile)

    writer.writerow(["Emp ID","First Name","Last Name", "DOB", "SSN", "State"])

    writer.writerows(finalfile)


print("------------------------------------------------------------------------")

