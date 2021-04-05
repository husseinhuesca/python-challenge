import os
import csv
import sys

udemy_csv = os.path.join("Resources","election_data.csv")


# with open(udemy_csv, newline='', encoding='utf-8') as csvfile:
with open(udemy_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)    
    dictcandidate = {row[0]:row[2] for row in csvreader}

#Identify Candidates
uniquevalues = []
for val in dictcandidate.values():
    if val in uniquevalues:
      continue
    else:
        uniquevalues.append(val)


#Results---------
print("Election Results")
print("----------------------------------------")
print("Total Votes: " + str(len(dictcandidate)))
print("----------------------------------------")

votes = []
contx = 0
for cont in uniquevalues:
    for cont1 in dictcandidate.values():
        if cont1 == cont:
            contx = contx + 1 
    votes.append(contx)
    contx = 0
    

#Votes Results
cont = 0
for conta in uniquevalues:
    print(str(uniquevalues[cont]) + ": " + str(round(((votes[cont]/len(dictcandidate))*100),3)) + "% (" + str(votes[cont]) + ")")
    cont = cont + 1


#Candidate Winner
max_winner = max(votes)
maxwinner_index = votes.index(max_winner)
candidatewinner = uniquevalues[maxwinner_index]
print("----------------------------------------")
print("Winner: " + candidatewinner)
print("----------------------------------------")

#New File TXT with Results
sys.stdout = open("Analysis\PyPoll_Results.txt", "w")

print("Election Results")
print("----------------------------------------")
print("Total Votes: " + str(len(dictcandidate)))
print("----------------------------------------")
cont = 0
for conta in uniquevalues:
    print(str(uniquevalues[cont]) + ": " + str(round(((votes[cont]/len(dictcandidate))*100),3)) + "% (" + str(votes[cont]) + ")")
    cont = cont + 1
print("----------------------------------------")
print("Winner: " + candidatewinner)
print("----------------------------------------")
   
sys.stdout.close()