# Math6002: Deterministic OR Methods
# Coursework 1
# Name: Emma Tarmey
# ID: 2940 4045

valid_constituencies = [{'2'}, {'4'}, {'12'}, {'2', '1'}, {'1', '5'},
                        {'2', '3'}, {'2', '5'}, {'4', '3'}, {'3', '5'},
                        {'4', '5'}, {'6', '5'}, {'10', '5'}, {'6', '7'},
                        {'6', '8'}, {'8', '7'}, {'7', '9'}, {'8', '9'},
                        {'8', '10'}, {'8', '11'}, {'9', '11'}, {'12', '9'},
                        {'10', '11'}, {'10', '13'}, {'12', '11'},
                        {'13', '11'}, {'14', '12'}, {'14', '13'},
                        {'2', '1', '5'}, {'2', '1', '3'}, {'1', '3', '5'},
                        {'6', '1', '5'}, {'2', '3', '5'}, {'6', '3', '5'},
                        {'10', '3', '5'}, {'6', '7', '5'}, {'6', '5', '8'},
                        {'10', '5', '11'}, {'6', '7', '8'}, {'6', '11', '8'},
                        {'8', '7', '9'}, {'8', '7', '11'}, {'7', '9', '11'},
                        {'8', '9', '11'}, {'8', '10', '11'}, {'8', '12', '11'},
                        {'8', '13', '11'}, {'13', '9', '11'},
                        {'14', '13', '11'}, {'6', '5', '11', '8'}]

electorate_data = {
   "1"  : 30000,
   "2"  : 50000,
   "3"  : 20000,
   "4"  : 70000,
   "5"  : 20000,
   "6"  : 40000,
   "7"  : 30000,
   "8"  : 30000,
   "9"  : 40000,
   "10" : 60000,
   "11" : 10000,
   "12" : 60000,
   "13" : 40000,
   "14" : 40000
}

votes_data = {
   "1"  : 17500,
   "2"  : 15000,
   "3"  : 14200,
   "4"  : 42000,
   "5"  : 18000,
   "6"  : 9000,
   "7"  : 12000,
   "8"  : 10000,
   "9"  : 26000,
   "10" : 34000,
   "11" : 2500,
   "12" : 27000,
   "13" : 29000,
   "14" : 15000
}


def determine_wins(constituencies, votes, totals):
    results = []
    total_votes  = 0
    total_voters = 0
    
    for i in range(0, len(constituencies)):
        con = constituencies[i]
        total_votes  = 0
        total_voters = 0
        
        print("Constituency ", i+1, ": ", con)
        
        for shire in con:
            total_votes  += votes_data[shire]
            total_voters += electorate_data[shire]
        
        print("Votes for Joris = ", total_votes)
        print("Total Voters = ", total_voters)
        
        if ((total_votes / total_voters) >= 0.5):
            results.append(1)
            print("Joris wins")
        else:
            results.append(0)
            print("Joris loses")
        
        print("")
    
    return results

results = determine_wins(valid_constituencies, votes_data, electorate_data)

print("Number of constituencies = ", len(valid_constituencies))
print("Number of constituencies where Joris wins = ", len([result for result \
    in results if (result == 1)]), "\n")

for i in range(0, len(results)):
    print("Constituency ", i+1, ": ", results[i])
    
    if ((i+1) % 5 == 0):
        print()
