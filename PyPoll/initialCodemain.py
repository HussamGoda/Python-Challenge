# Importing Modules os and csv
import os
import csv

# List to store entries in the .csv file
list_of_entries = []

#List to store candidates names without repeatation
candidates = []

#List to store total votes for each candidate in the List "candidates"
total_votes_for_each_candidate = []

# List to store vote % for each candidate in the List "candidates"
vote_percent_for_each_candidate = []

# Location of.csv file
csv_electiondata_file_location = os.path.join('Resources','election_data.csv')

# Open file (budget_data.csv) and reading entries in file
with open(csv_electiondata_file_location, encoding='UTF-8') as csvfile:
     entries_in_file = csv.reader(csvfile, delimiter=',')
     
     # header in file, and reporting in terminal
     header_in_file = next(entries_in_file)
     print(f"This is the header in the file: {header_in_file}")
     

     # Store entries in List: list_of_entries
     for entries in entries_in_file:
        print(entries) 
        list_of_entries.append(entries)
        
total_number_of_votes = len(list_of_entries)
print(total_number_of_votes)
x = int(total_number_of_votes)

#Finding total number of candidates and thier names. Store names in List: candidates
for i in range(0, x):
    if list_of_entries[i][2] not in  candidates:
       candidates.append (list_of_entries[i][2])
print(candidates)
total_number_of_candidates = len(candidates)
print(str(total_number_of_candidates))
y=int(total_number_of_candidates)


# Total votes for each candidate and List: candidates and store in List: Total_votes_for_each_candidate
for i in range(0, y):
    counter = 0
    for j in range(0, x):
        if list_of_entries[j][2] == candidates [i]:
           counter = counter + 1
    total_votes_for_each_candidate.append(counter)

print(str(Total_votes_for_each_candidate))

#calculate ratio of total vote for each candidate and store in List: vote_percent_for_each_candidate
for i in range(0, y):
    ratio_as_percent_for_each_candidate = round((100 *  (total_votes_for_each_candidate [i] / x)), 3)
    vote_percent_for_each_candidate.append(ratio_as_percent_for_each_candidate)

#print(str(vote_percent_for_each_candidate))

#who is the winner...locate position of maximum vote in List: vote_percent_for_each_candidate. This is the same location for the winner in Lits: candidates
maximum_vote_percent = 0
for i in range(0, y):
    if vote_percent_for_each_candidate[i] > maximum_vote_percent:
       maximum_vote_percent = vote_percent_for_each_candidate[i]
       winner_location_on_list = i

print(str(candidates[winner_location_on_list]))

#print to terminal
print("\nElection Results\n")
print("-------------------------\n")
print("Total Votes: " + str(total_number_of_votes))
print("\n-------------------------\n")
for i in range (0, y):
    print(str(candidates[i]) + ": " + str(vote_percent_for_each_candidate[i]) + "%  (" + str(total_votes_for_each_candidate[i]) + ")\n")
print("-------------------------\n")
print("Winner: " + str(candidates[winner_location_on_list]))
print("\n------------------------")

#Writing final analysis to a text file named Analysis.txt, placed in the Analysis folder
file = open('Analysis/Election_Results.txt', 'w')
file.write('Election Results\n\n')
file.write('--------------------------------\n\n')
file.write('Total Votes: ' + str(total_number_of_votes))
file.write('\n\n--------------------------------\n\n')
for i in range (0, y):
    file.write(str(candidates[i]) + ': ' + str(vote_percent_for_each_candidate[i]) + '%  (' + str(total_votes_for_each_candidate[i]) + ')\n\n')
file.write('---------------------------------\n\n')
file.write('Winner: ' + str(candidates[winner_location_on_list]))
file.write('\n\n------------------------------')
file.close()












    
