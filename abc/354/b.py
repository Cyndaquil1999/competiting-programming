N = int(input())
user_data = []

for _ in range(N):
    name, rating = input().split()
    user_data.append((name, int(rating)))

user_data.sort(key=lambda x: (x[0], x[1]))

rating_total = sum(rate for name, rate in user_data)

print(user_data[rating_total % N][0])4
2 5 1 2
