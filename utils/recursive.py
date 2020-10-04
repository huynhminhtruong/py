def sort_lexicographical():
	pass
 
if __name__ == '__main__':
	s = input()
	a = list()
	for i in range(0, len(s)):
		if s[i] == 'F':
			a.append(i)
	print(a)