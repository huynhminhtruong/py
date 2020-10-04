if __name__ == '__main__':
	a = [1, 2, 3, 4, 5]
	mid = int(len(a) / 2)
	x, y = a[0:mid], a[mid:len(a)]
	print(x, y, a[0:0])