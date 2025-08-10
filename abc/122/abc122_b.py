S = input()
words = ["A", "T", "C", "G"]

answer = 0
tmp_size = 0

for s in S:
    if s in words:
        tmp_size += 1

    else:
        answer = max(answer, tmp_size)
        tmp_size = 0

answer = max(answer, tmp_size)
print(answer)
