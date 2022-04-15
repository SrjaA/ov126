nums = [int(i) for i in input().split()]
plus = len(list(filter(lambda i: i > 0, nums)))
minus = len(list(filter(lambda i: i < 0, nums)))
n = len(list(filter(lambda i: i == 0, nums)))
print(plus, minus, n)