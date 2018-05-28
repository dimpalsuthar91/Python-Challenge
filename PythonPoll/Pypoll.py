#import os and write csv path
import os
from collections import Counter

csvpath = os.path.join("election_data_2.csv") 

#Import csv
import csv
with open(csvpath, newline='') as csvfile:

    # CSV reader delimiter and varaiable
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader,None)

   #lists
    voterid = []
    county = []
    candidates = []
    
    #run for loop for every row
    for dog in csvreader:
        voterid.append(dog[0])
        county.append(dog[1])
        candidates.append(dog[2])
    
    #find a unique set of canditates, and the total vote. Counter is a neat command
    can_set = set(candidates)    
    tot_vote = len(voterid)
    cnt = Counter(candidates)

    #create a list with the unique names
    can_names = []
    
    for row in can_set:  
        can_names.append(row)

    print("Election Results")
    print("----------------------------------------")
    print(f"The total number of votes was {tot_vote}")
    print("----------------------------------------")

    dictionary_can = {}
    can_count = 0
    for row in can_names:
        candidate_name = str(can_names[can_count])
        votes = candidates.count(candidate_name)
        votes = int(votes)
        percentage = round(votes / tot_vote * 100, 2)
        dictionary_can.update({ candidate_name : votes})
        print(f"{candidate_name}: {percentage}%  ({votes} votes)" )
        can_count = can_count + 1

    import operator

    winner = max(dictionary_can, key=lambda key: dictionary_can[key])
    
    print("Winner: ", winner)