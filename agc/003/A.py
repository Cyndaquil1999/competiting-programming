S = input()
angle = {"N": 0, "W": 0, "S": 0, "E": 0}

for s in S:
    angle[s] += 1

if angle["N"] != 0 and angle["S"] != 0 and angle["E"] == 0 and angle["W"] == 0:
    print("Yes")
elif angle["N"] == 0 and angle["S"] == 0 and angle["E"] != 0 and angle["W"] != 0:
    print("Yes")  
elif (angle["N"] == 0 or angle["S"] == 0) or (angle["E"] == 0 or angle["W"] == 0):
    print("No")
else:
    print("Yes")
