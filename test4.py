import re
from collections import Counter

r = open("English.txt").read()

x = Counter(re.split("\W+",r))

print(x.most_common(10))









