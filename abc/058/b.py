O = input()
E = input()
ans = ""

N = min(len(O), len(E))
for i in range(N):
    ans += O[i] + E[i]

if abs(len(O) - len(E)) == 1:
    ans += O[-1]

print(ans)    