import itertools;


# Returns subsets of size 'n' from a list 's'
def findsubsets(s, n):
    l= list(itertools.combinations(s, n));
    return l;

# Calculates support, counts freq of itemsets in tlists
def getCandidateSet (itemsets,transactions,minSupport,n): 
    #freq of each item set in tlists
    support ={};
    for itemset in itemsets:
        for tlist in transactions.values():
            if ( set(itemset).issubset(set(tlist))):
                if itemset in support : 
                    support[itemset] +=1.0/n;
                else:
                    support[itemset] = 1.0/n;
    print("Before pruning  - {}".format(support) )
    for [iset,isupport] in list(support.items()):
        if isupport < minSupport:
            print("Removing {} [support - {},  less than min support]".format(iset,isupport))
            support.pop(iset);
    return support; 
# returns set of valid t-items
def get_transactionitems (transactions,support):
    if  not support :
        dic = dict(); 
        for l in transactions.values():
            for i in l:
                if i in dic:
                    dic[i] +=1;
                else:
                    dic[i]=1;
        return set(list(dic.keys()));
    else:
        nl = [];
        for i in support.keys():
            for k in i:
                nl.append(k);
        return set(nl);

#get support of a tuple
def getSupport(itemSet,support):
    supportIndex=len(itemSet);
    if itemSet in support[supportIndex]: 
        return support[supportIndex][itemSet];
    else:
        return -1;

#Generates rules from freqItemSet
def generateRulesAndConf(freqItemSet,support):
    confidence= {};
    rules = []
    print("Frequent item set - " + str(freqItemSet));
    subsets = powerset(freqItemSet);
    subsets.pop(0);
    subsets.pop(-1);
    print(subsets);
    for i in range(0,int(len(subsets)/2)):
        rules.append((subsets[i] ,subsets[len(subsets)-1-i]));
        rules.append((subsets[len(subsets)-1-i], subsets[i]));
    print("Generating rules");
    for rule in rules:
        conf = float(getSupport(tuple(set(rule[0]+rule[1])),support) / getSupport(rule[1],support));
        print("{}\t-> {} \tconf = {}".format(rule[0],rule[1],conf));
        confidence[rule] = conf;
    return confidence

# returns powerset of a set
def powerset(iterable):
   # "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return list(itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(len(s)+1)));

def filterRules (rules,tc):
    rules = {k: v for k,v in rules.items() if v>tc};
    for rule in rules:
        rhs , lhs = rule;
        cnf = rules[rule];
        print("{} \t-> {}\tconf = {} ".format(rhs,lhs,cnf));
    return rules;


