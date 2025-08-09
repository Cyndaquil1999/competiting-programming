S = input()

word_range = [True] * 123
for i in range(len(S)):
    word_range[ord(S[i])] = False
    
    
    
for i in range(97, 123):
    if word_range[i]:
        print(chr(i))
        break