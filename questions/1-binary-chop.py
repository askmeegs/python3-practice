# binary search
import time

"""
Problem:
Implement binary search - first iteratively, then recursively.
A is the array; x is the target element

Details -
- A is already sorted
- A contains unique values (no dups)
- Return the index (0-indexed) of x in A, or -1 if appears nowhere

My notes:
- Binary search is about narrowing the search limits, that's it.
"""


# method - define limits to the search zone
def binary_iter(A, x):
	print("\n\ninput=%s looking for %s, found at index..." % (A,x))

	# first and last are the limits of the search
	first = 0
	last  = len(A)-1
	while first<=last:
		mid = (first+last)//2
		if A[mid] == x:
			return mid
		else:
			# if we need to go left, take the first half of our Zone
			if x < A[mid]:
				last = mid-1
			# if we need to go right, take the second half of our Zone
			else:
				first = mid+1
	return -1



# method: trash anything not in the search zone
# FALLS SHORT: because recursion is Forgetful, only prints IF the int exists, not where
# would need - a recursive helper to keep track of relative index of "mid" in the initial A? 
def binary_rec(A, x):
	if len(A) == 0:  #base case - we've run out of options
		return False
	else: #recursive case
		mid = len(A)//2 #rounds down
		if A[mid] == x:
			return True
		else:
			if x < A[mid]: #go left
				return binary_rec(A[:mid], x)
			else: #go right
				return binary_rec(A[mid+1:], x)



print(binary_rec([1,3,4,5,7], 5))
print(binary_rec([1,3,4,5,7], 6))
print(binary_rec([0,1,3,4,5,8,9,13,15], 11))
print(binary_rec([0,1,3,4,5,8,9,13,15], 13))
print(binary_rec([1], 4))
print(binary_rec([], 42))
print(binary_rec([3,4,5,12], 12))
print(binary_rec([3,4,5,12], 3))
print(binary_rec([3,4,5,12], -10))
