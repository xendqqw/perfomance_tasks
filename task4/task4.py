file_path = input()

with open(file_path, 'r') as f:
    nums = [int(line.strip()) for line in f]

nums.sort()
median = nums[len(nums) // 2]
moves = 0

for num in nums:
    moves += abs(num - median)

print(moves)
