in_equation = input().split('-')

nums = []
for i in in_equation:
    result = 0
    nums_2 = i.split('+')
    for num in nums_2:
        result += int(num)

    nums.append(result)

answer = nums[0] - sum(nums[1:])
print(answer)
