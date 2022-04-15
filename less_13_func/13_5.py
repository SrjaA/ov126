def count_args(*args):
    return len(args)

print(count_args(3,4,8,23,65,34))

print(count_args(*[int(i) for i in input().split()]))