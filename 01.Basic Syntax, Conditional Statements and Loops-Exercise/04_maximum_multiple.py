divisor = int(input())
bound = int(input())

max_N = 0

for i in range(1, bound + 1):
    if i % divisor == 0:
        if i > max_N:
            max_N = i
print(max_N)

