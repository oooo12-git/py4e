fhand = open("zenofpython.txt")
zen = fhand.read()
# print(zen)
di = dict()
words = zen.split()
for word in words:
    di[word] = di.get(word,0)+1

largest = -1
theword = None
for k,v in di.items():
    if v > largest :
        largest = v
        theword = k
print('Done -->',theword,largest)