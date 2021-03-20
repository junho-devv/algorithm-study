def sequential_search(num, tar, arr):

    for x in range(num):
        if arr[x] == tar:
            return x+1


input_data = input().split()
n = int(input_data[0])
target = input_data[1]

aList = input().split()

print(sequential_search(n, target, aList))
