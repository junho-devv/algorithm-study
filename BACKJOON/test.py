import sys

input = sys.stdin.readline

list_n = [[30, 10], [20, 20], [30, 40], [10, 12], [10, 11]]
list_n.sort(key = lambda x: -x[0])
print(list_n)