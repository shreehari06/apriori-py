# Apriori Algo in Python

# util functions - 
from aprioriUtils import *;
# Variables and User Input
# I/0 
# minSupport = float(input("Enter min support - "));
# threshold_confidence = float(input("Enter threshold confidence - "));
# n = int(input("Enter number of transactions - "));

# NO I/O
minSupport = 0.5;
threshold_confidence = 0.7;
n=4;
transactions = dict();
iteration=0;
support = {};
transactions =  {1: [1, 3, 4], 2: [2, 3, 5], 3: [1, 2, 3, 5], 4: [2, 5]};

# I/O
# for i in range(1,n+1):
#     int_list = [];
#     str_input = input("Enter transaction " + str(i) + " - ");
#     str_list = str_input.split(" ");
#     for j in str_list:
#         int_list.append(int(j));
#     transactions[i]= int_list;

# Printing the input vars

print(''' 
Minimum support - {} 
Threshold Confidence - {}
Transactions - {}'''.format(minSupport,threshold_confidence,transactions));

# Helper Functions


 
# Returns list of items above min support

#Iterations :
itr = 0;
itemsets = [[]];
support = [[]];
while True:
    itr = itr +1;
    print( "\nITR - " + str(itr));
    print("Transaction items - " + str(get_transactionitems(transactions, support[itr-1]))); 
    itemsets.append(findsubsets (get_transactionitems(transactions,support[itr-1]),itr));
    print("itemsets - " + str(itemsets[itr]));
    support.append(calcSupport (itemsets[itr],transactions,minSupport,n));
    print("support - "+ str(support[itr]));
    if len(support[-1].keys()) == 1 :
        print("Iterations complete")
        break;

# Generating rules


freqItemSet =tuple(list(support[-1].keys())[0]);
cnfRules = generateRulesAndConf(freqItemSet,support);
print("Filtering rules -")
filterRules(cnfRules,threshold_confidence);
