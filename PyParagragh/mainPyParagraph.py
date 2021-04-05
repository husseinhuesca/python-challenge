import os
import csv
import sys
import re




udemy_txt = os.path.join("Resources","raw_data_paragraph_3.txt")

# with open:
with open(udemy_txt) as txtfile:
    txtreader = txtfile.read()
    
#Original Text   
print("----------------------------")

print(txtreader)

print("----------------------------")

words = txtreader.split()

#Word Count
print("Approximate Word Count: " + str(len(words)))

#Sentence Split
sentence =  re.split("(?<=[.!?]) +",txtreader)

print("Approximate Sentence Count: " + str(len(sentence)))


#Average Letter Count
characters = []
for row in words:
    characters1 = len(row)
    characters.append(characters1)


cont = 0.0
for cont1 in characters:
    cont = cont + float(cont1)    
average = cont / len(characters)

print("Average Letter Count: "+ str(round(average,1)))

charactersSentences = []
for row in sentence:
    characterssentence1 = row.split()
    charactersSentences.append(characterssentence1)

#Average Sentence Count
charactersSentences2 = []
for row in charactersSentences:
    characterssentence3 = len(row)
    charactersSentences2.append(characterssentence3)

cont = 0.0
for cont1 in charactersSentences2:
    cont = cont + float(cont1)    
average1 = cont / len(charactersSentences2)

print("Average Sentence Lenght: " + str(round(average1,1)))

print("----------------------------")


#Write new Txt file with the results
sys.stdout = open("Analysis\PyParagraph_Results.txt", "w")

print("----------------------------")
print(txtreader)
print("----------------------------")

print("Approximate Word Count: " + str(len(words)))
print("Approximate Sentence Count: " + str(len(sentence)))
print("Average Letter Count: "+ str(round(average,1)))
print("Average Sentence Lenght: " + str(round(average1,1)))

print("----------------------------")
sys.stdout.close()