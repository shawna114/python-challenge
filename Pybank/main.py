#In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.
#You will be give a set of poll data called election_data.csv. The dataset is composed of three columns: Voter ID, County, and Candidate. Your task is to create a Python script that analyzes the votes and calculates each of the following:
    #The total number of votes cast
    #Acomplete list of candidates who received votes
    #The percentage of votes each candidate won
    #The total number of votes each candidate won
    #The winner of the election based on popular vote.

#Imports modules allowing reading/writing files
import os
import csv

#Opens file and identifies that intention is to read only
with open ('C:\\Users\\shawn\\python-challenge\\Pybank\\Resources\\budget_data.csv', 'r') as csvfile:
   
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    print(csvreader)
    
    #Reads the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    
    print("CSV Header: "+str(csv_header))
    
    #Reads each row of data after the header
    for row in csvreader:
            print(row)