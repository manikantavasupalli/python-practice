'''
An incrementally sorted array would be the input and its has to be rearrached such that
highest number comes at 0th index and minimum number comes at 1st index.
2nd max comes at 2nd index and 2nd min comes at 3rd index
'''
import math

def rearrange_alt(array_a):
	n = len(array_a) # array size
	temp = [0]*n
	c=1
	for i in range(math.ceil(n / 2)):
		temp[c] = array_a[i]
		c = c+2
		if c == n:
			c-=1
	c=0
	for j in range(n-1,i, -1):
		temp[c] = array_a[j]
		c=c+2
	print(temp)
	

a = [1,2,3,4,5]
rearrange_alt(a)