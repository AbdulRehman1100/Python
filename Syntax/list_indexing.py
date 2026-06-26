
tstlist = ["Kiyani Street", 'Mangla Road','Dina', 'Jhelum', 49400]
print(tstlist, type(tstlist), len(tstlist))

for i in range(len(tstlist)):
    print(i, tstlist[i])

for i in tstlist:
    print(i)

i = 0
while(i < len(tstlist)):
    print(tstlist[i])
    i = i + 1