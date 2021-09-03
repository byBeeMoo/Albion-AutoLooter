values = [[-1820, 436], [-1743, 441], [-1671, 445], [-1587, 445], [-1499, 448], [-1826, 526], [-1739, 527], [-1662, 527],
          [-1583, 526], [-1503, 528], [-1826, 605], [-1744, 606], [-1667, 606], [-1584, 607], [-1510, 607]]

resx = []
resy = []

avglistx = []
avglisty = []

for value in values:
    resx.append(value[0])
    resy.append(value[1])


for i in range(0, len(resx)):
    if i+1 < len(resx):
        res = resx[i]-resx[i+1]
        if res < 0:
            avglistx.append(res)
            
for i in range(0, len(resy)):
    if i+1 < len(resy):
        res = resy[i]-resy[i+1]
        if res > -10:
            avglisty.append(res)
            
for i in range (0, len(avglistx)):
    res += avglistx[i]

print("average X: " + str(res/len(avglistx)))

for i in range (0, len(avglisty)):
    res += avglisty[i]
    
print("average Y: " + str(res/len(avglisty)))
            
            
print(avglistx)
print(avglisty)

print(resx)
print(resy)