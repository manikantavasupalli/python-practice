def remove_adj_dups(s):
	cat=s[0]
	u = []
	i=0
	while i < len(s)-1:
		if s[i] != s[i+1]:
			u.append(s[i])
			if i == len(s)-2:
				u.append(s[i+1])
			i+=1
		else:
			i+=2
		
	print(''.join(u))

remove_adj_dups("geeksforgeeksmadoifasd  asdf   addd d     sd   sssss mani")