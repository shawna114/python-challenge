#Imports modules allowing reading/writing files and counting items
import os
import csv
import numpy

#Creates empty lists that votes can be added to during loop
total_votes = []
khan_votes = []
correy_votes = []
li_votes = []
otooley_votes = []

#Creates list to store column names
columns = []

#Opens file and identifies that intention is to read only
with open ('C:\\Users\\shawn\\python-challenge\\PyPoll\\Resources\\election_data.csv', 'r') as csvfile:
   
#CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

#Reads the header row first
    csv_header = next(csvreader)

#Stores header row in columns list
    columns = csv_header
    
#Loops through rows in candidate column with 'if' statement to get total count of votes for each candidate
    for row in csvreader:
        if row[2]== 'Khan':
            khan_votes.append(row)  
        elif row[2] == 'Correy':
            correy_votes.append(row)
        elif row[2] == 'Li':
            li_votes.append(row)
        elif row[2] == "O'Tooley":
            otooley_votes.append(row)

#Counts votes for each candidate and sums individual candidate votes to calculate total votes
khan_votes = (len(khan_votes))
correy_votes = (len(correy_votes))
li_votes = (len(li_votes))
otooley_votes = (len(otooley_votes))
total_votes = (khan_votes + correy_votes + li_votes + otooley_votes)

#Calculates each candidate's percent of votes based on total votes.
khan_pct = (khan_votes/total_votes) 
correy_pct = (correy_votes/total_votes) 
li_pct = (li_votes/total_votes) 
otooley_pct = (otooley_votes/total_votes)
total_pct = (total_votes)/(total_votes)

#Prints election results in pre-defined format.
print("Election Results")
print("--------------------------")
print(f"Total Votes:  " + '{:,}'.format(total_votes))
print("--------------------------")
print(f"Khan:     " + '{:.2%}'.format(khan_pct) + ' ({:,})'.format(khan_votes))
print(f"Correy:   " + '{:.2%}'.format(correy_pct) + ' ({:,})'.format(correy_votes))
print(f"Li:       " + '{:.2%}'.format(li_pct) + ' ({:,})'.format(li_votes))
print(f"O'Tooley: " +   ' {:.2%}'.format(otooley_pct) + '  ({:,})'.format(otooley_votes))
print("--------------------------")

#Identifies/prints winner's name based on times each name appears in candidate column.
fdist=dict(zip(*numpy.unique(str(row[2]),return_counts=True)))
print("Winner: " + (list(fdist)[-1]))
print("--------------------------")

#Specifies path for file
output_path = os.path.join("C:\\Users\\shawn\\python-challenge\\PyPoll", "Analysis", "Election_Results.txt")

#Opens the file using "write" mode. Specifies the variable to hold the contents
with open(output_path, 'w') as txtfile:

#Initializes txt.writer
    txtwriter = txtfile

#Writes results to .txt file (uses '\n' to go to next line)
    txtwriter.write('Election Results   \n')
    txtwriter.write('--------------------------\n')
    txtwriter.write(f"Total Votes:  " + '{:,} \n'.format(total_votes))
    txtwriter.write('--------------------------\n')
    txtwriter.write(f"Khan:     " + '{:.2%}'.format(khan_pct) + ' ({:,})\n'.format(khan_votes))
    txtwriter.write(f"Correy:   " + '{:.2%}'.format(correy_pct) + ' ({:,})\n'.format(correy_votes))
    txtwriter.write(f"Li:       " + '{:.2%}'.format(li_pct) + ' ({:,})\n'.format(li_votes))
    txtwriter.write(f"O'Tooley: " +   ' {:.2%}'.format(otooley_pct) + '  ({:,})\n'.format(otooley_votes))
    txtwriter.write('--------------------------\n')
    txtwriter.write('Winner: ' + (list(fdist)[-1])) 
    txtwriter.write('\n')
    txtwriter.write('--------------------------')
