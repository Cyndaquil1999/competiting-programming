X = int(input())
numbers = [1]

for i in range(2,33):
    for j in range(2,10):
        if i ** j < 1010:
            numbers.append(i ** j)

numbers = sorted(numbers)

if X == 1000:
    exit(print(1000))

for i in range(len(numbers)-1):
    if numbers[i] <= X and numbers[i+1] > X:
        print(numbers[i])