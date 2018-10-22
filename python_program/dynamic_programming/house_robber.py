# Problem: 
# You are a professional robber planning to rob houses along a street.
# Each houses has certain amount of money stashed, the only constraint stopping you
# from tobbing each of them is that adjacent houses have security system connected
# and it will automatically contact to the police if two adjacent houses were broken
# into on the same night.

# Given a list of non-negative integers representing the amount of money of each house,
# determine the maximum amount of money you can rob tonight without alerting the police.


# Recursive algo:

def house_rob_rec(n, nums):
	max_val = 0
	if n == 1:
		return nums[0]
	if n == 2:
		return max(nums[0], nums[1])
	max_val = max(max_val, house_rob_rec(n - 1, nums))
	for i in range(n - 2, 0, -1):
		max_val = max(max_val, house_rob_rec(i, nums) + nums[n - 1])
	return max_val


def house_rob_dp(n, nums):
	rob = [0] * n
	rob[0] = nums[0]
	rob[1] = max(nums[0], nums[1])
	for i in range(2, n):
		rob[i] = max(rob[i - 1], nums[i] + rob[i - 2])
	return rob[n - 1]