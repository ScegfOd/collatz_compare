def collatz(*args):
	output = {0: 'a', 1: 'b'} # expandable/configurable output :D
	nums = list(map(int, args))
	while 1 not in nums:
		nums = [ (3*n)+1 if n%2 else n//2 for n in nums ]
	return output[nums.index(1)]

# testing
print("following two lines should match:\na b b")
print(collatz(10,15), collatz(13, 16), collatz(53782, 72534))
