N = int(input())
A = list(map(int, input().split()))

ranking = {}
sorted_A = sorted(A)


for i in range(N):
    if sorted_A[i] not in ranking:
        ranking[sorted_A[i]] = 1
    else:
        ranking[sorted_A[i]] += 1
        


for i in range(N):
    answer_ranking = 1
    for time, value in ranking.items():
        if A[i] == time:
            print(answer_ranking)
            break
        else:
            answer_ranking += value
