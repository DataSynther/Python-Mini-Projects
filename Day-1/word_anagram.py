## Creating Function for Grouping anagrams
from collections import defaultdict

def group_anagrams(a):
    try:
        dfdict = defaultdict(list)
        for i in a:
            sorted_i = " ".join(sorted(i))
            dfdict[sorted_i].append(i)
        return dfdict.values()
    
    except Exception as e:
        print (e)


words = ["tea", "eat", "bat", "ate", "arc", "car"]
print(group_anagrams(words))