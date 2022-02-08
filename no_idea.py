n, m = list(map(int, input().split()))

major_array = list(map(int, input().split()))

A = set(map(int, input().split()))
B = set(map(int, input().split()))

happiness = 0

for i in major_array:
    if i in A:
        happiness += 1
    if i in B:
        happiness -= 1

print(happiness)
