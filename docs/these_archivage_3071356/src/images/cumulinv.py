import sys
sum = 0
l = []

for line in sys.stdin:
    t = line.split()
    k = int(t[0])
    v = float(t[1])
    sum = sum + v
    l.append([k, v])

total = sum

for [k, v] in l:
    print ("%d %lf" % (k, sum/total))
    sum = sum - v
