W = input()
words = dict()

for w in W:
    if w not in words:
        words[w] = 1
    else:
        words[w] += 1
        
for key, val in words.items():
    if val % 2 != 0:
        exit(print("No"))
    
print("Yes")