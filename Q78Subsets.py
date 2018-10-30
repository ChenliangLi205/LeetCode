import time

T1 = [1, 2, 3, 4, 5, 6, 7]


def powerSet(nums):
	if len(nums) == 0:
		return []

	if len(nums) == 1:
		return [[], nums]

	subSets = [[]]

	def start_from(i):
		power_set = [[nums[i]]]
		if i == len(nums)-1:
			return power_set
		new_sets = start_from(i+1)
		for s in new_sets:
			power_set.append(power_set[0]+s)
		power_set.extend(new_sets)
		return power_set

	return subSets+start_from(0)

if __name__ == '__main__':
	time1 = time.time()
	print(powerSet(T1))
	print(time.time()-time1)
