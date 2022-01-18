# Math6002: Deterministic OR Methods
# Coursework 1
# Name: Emma Tarmey
# ID: 2940 4045


class graph:
    
    def __init__(self, graph_data = None):
        if (graph_data is None):
           graph_data = {}
        self.graph_data = graph_data
    
    def arcs(self):
        return self.find_all_arcs()
    
    # Find the distinct list of edges
    def find_all_arcs(self):
        arcs = []
    
        for arc in self.graph_data:
           for next_arc in self.graph_data[arc]:
              if {next_arc, arc} not in arcs:
                 arcs.append({arc, next_arc})
        
        return (arcs)


def find_ones(shires, data):
    ones    = []
    current = 0
    
    for shire in shires:
        current = data[shire]
        if ((current >= 50000) and (current <= 100000)):
            
            # shire 10 may not become a 1-shire constituency
            if (shire == "10"):
                pass
            else:
                ones.append(shire)
    return (ones)


def find_twos(pairs, data):
    twos    = []
    current = 0
    shire_1 = ""
    shire_2 = ""
    
    for pair in pairs:
        shire_1 = list(pair)[0]
        shire_2 = list(pair)[1]
        current = data[shire_1] + data[shire_2]
        
        if ((current >= 30000) and (current <= 100000)):
            # remove duplicates
            if (pair in twos):
                pass
            else:
                twos.append(pair)
    
    return (twos)


def find_all_threes(pairs, data):
    all_threes = []
    current    = {}
    
    for pair_1 in pairs:
        for pair_2 in pairs:
            current = pair_1.union(pair_2)
            
            # only accept a new constituency if we have 2 arcs between 3 shires
            # pairs of the same are rejected as union will have 2 elements
            # non-adjacent pairs also rejected as union will have 4 elements
            if (len(current) == 3):
                all_threes.append(current)
    
    return (all_threes)


def find_threes(pairs, data):
    all_threes = find_all_threes(pairs, data)
    
    threes  = []
    current = 0
    shire_1 = ""
    shire_2 = ""
    shire_3 = ""
    
    for three in all_threes:
        shire_1 = list(three)[0]
        shire_2 = list(three)[1]
        shire_3 = list(three)[2]
        current = data[shire_1] + data[shire_2] + data[shire_3]
        
        if ((current >= 30000) and (current <= 100000)):
            
            # remove duplicates
            if (three in threes):
                pass
            else:
                threes.append(three)
    
    return (threes)


def find_all_fours(pairs, data):
    all_fours = []
    current   = {}
    triples   = find_all_threes(pairs, data)
    
    for pair in pairs:
        for triple in triples:
            current = pair.union(triple)
            
            # only accept a new constituency if we have 3 arcs between 4 shires
            # pairs of the same are rejected as union will have 3 elements
            # non-adjacent pairs also rejected as union will have 5 elements
            if (len(current) == 4):
                all_fours.append(current)
    
    return (all_fours)


def find_fours(pairs, data):
    all_fours = find_all_fours(pairs, data)
    
    fours   = []
    current = 0
    shire_1 = ""
    shire_2 = ""
    shire_3 = ""
    shire_4 = ""
    
    for four in all_fours:
        shire_1 = list(four)[0]
        shire_2 = list(four)[1]
        shire_3 = list(four)[2]
        shire_4 = list(four)[3]
        current = data[shire_1] + data[shire_2] + data[shire_3] + data[shire_4]
        
        if ((current >= 30000) and (current <= 100000)):
            
            # remove duplicates
            if (four in fours):
                pass
            else:
                fours.append(four)
    
    return (fours)

def find_fives(pairs, data):
    all_fives = []
    current   = {}
    quads     = find_all_fours(pairs, data)
    
    for pair in pairs:
        for quad in quads:
            current = pair.union(quad)
            
            # only accept a new constituency if we have 4 arcs between 5 shires
            # pairs of the same are rejected as union will have 4 elements
            # non-adjacent pairs also rejected as union will have 6 elements
            if (len(current) == 5):
                all_fives.append(current)
    
    fives   = []
    current = 0
    shire_1 = ""
    shire_2 = ""
    shire_3 = ""
    shire_4 = ""
    shire_5 = ""
    
    for five in all_fives:
        shire_1 = list(five)[0]
        shire_2 = list(five)[1]
        shire_3 = list(five)[2]
        shire_4 = list(five)[3]
        shire_5 = list(five)[4]
        current = data[shire_1] + data[shire_2] + data[shire_3] + \
        data[shire_4] + data[shire_5]
        
        if ((current >= 30000) and (current <= 100000)):
            
            # remove duplicates
            if (five in fives):
                pass
            else:
                fives.append(five)
    
    return (fives)


# Create the dictionary with graph elements
graph_data = { 
   "1"  : ["2","5"],
   "2"  : ["1", "3", "5"],
   "3"  : ["2", "4", "5"],
   "4"  : ["3", "5", "10"],
   "5"  : ["1", "2", "3", "4", "6", "10"],
   "6"  : ["5", "7", "8"],
   "7"  : ["6", "8", "9"],
   "8"  : ["6", "7", "9", "10", "11"],
   "9"  : ["7", "8", "11", "12"],
   "10" : ["4", "5", "8", "11", "13"],
   "11" : ["8", "9", "10", "12", "13"],
   "12" : ["9", "11", "14"],
   "13" : ["10", "11", "14"],
   "14" : ["12", "13"]
}

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

g = graph(graph_data)

shires = graph_data.keys()
arcs  = g.find_all_arcs()

print("Number of shires = ", len(shires))
for shire in shires:
    print(shire)
print("\n")

print("Number of possible adjacency connections = ", len(arcs))
for arc in arcs:
    print(sorted( [int(i) for i in arc] ))
print("\n")

# Find every valid 1-shire constituency
ones = find_ones(shires, electorate_data)
print("Number of valid 1-shire constituencies = ", len(ones))
for one in ones:
    print(one)
print("\n")

# Find every valid 2-shire constituency
twos = find_twos(arcs, electorate_data)
print("Number of valid 2-shire constituencies = ", len(twos))
for two in twos:
    print(sorted( [int(i) for i in two] ))
print("\n")

# Find every valid 3-shire constituency
threes = find_threes(arcs, electorate_data)
print("Number of valid 3-shire constituencies = ", len(threes))
for three in threes:
    print(sorted( [int(i) for i in three] ))
print("\n")

# Find every valid 4-shire constituency
fours  = find_fours(arcs, electorate_data)
print("Number of valid 4-shire constituencies = ", len(fours))
for four in fours:
    print(sorted( [int(i) for i in four] ))
print("\n")

# Find every valid 5-shire constituency
fives  = find_fives(arcs, electorate_data)
print("Number of valid 5-shire constituencies = ", len(fives))
for five in fives:
    print(sorted( [int(i) for i in five] ))
print("\n")


valid_constituencies = ones + twos + threes + fours + fives
print("Total number of valid constituencies = ", len(valid_constituencies))
for i in range(0, len(valid_constituencies)):
    con = valid_constituencies[i]
    
    if (i < 3):
        print("Constituency ", i+1, ": \t", [int(con)])
    else:
        print("Constituency ", i+1, ": \t", sorted( [int(i) for i in con] ))
print("\n")
