def get_first_dig(number):
	return int(number/(10**(len(str(number))-1)))

def check_order(a1, a2):
	m = min(a1, a2) # get the min number to traverse the elements
	flag = True
	for i in range(1,len(str(m))):
		if int(str(a1)[i]) >= int(str(a2)[i]):
			continue
		else:
			flag = False
			break
	return flag

def sort_with_digit1(a):
	n = len(a)
	for i in range(0,n):
		for j in range(0,n-i-1):
			if get_first_dig(a[j]) < get_first_dig(a[j+1]):
				a[j], a[j+1] = a[j+1], a[j]
			elif get_first_dig(a[j]) == get_first_dig(a[j+1]):
				is_order = check_order(a[j], a[j+1])
				if not is_order:
					a[j], a[j+1] = a[j+1], a[j]

	print(a)
	
	

inp_array = [12,423,12,44,45,222,444,3,1,5,55,66,443,49]
sort_with_digit1(inp_array)