def toString(List):
    return ''.join(List)

# Function to print permutations of string
# This function takes three parameters:
# 1. String
# 2. Starting index of the string
# 3. Ending index of the string.


def permute(a, l, r):
	if l == r:
		# print("l==r")
		print(toString(a))
	else:
		for i in range(l, r+1):
			print('i=',i,'l=',l,'r=',r)
			a[l], a[i] = a[i], a[l]
			# print("a1"+str(a))
			permute(a, l+1, r)
			# print('2i=',i,'2l=',l,'2r=',r)
			a[l], a[i] = a[i], a[l]  # backtrack
			# print("a2"+str(a))





# Driver program to test the above function
string = "ABCD"
n = len(string)
a = list(string)
permute(a, 0, n-1)
