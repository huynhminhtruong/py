class Book:
	def __init__(self, name, writer, year):
		self.name = name
		self.writer = writer
		self.year = year
		self.next = None

class Books:
	def __init__(self):
		self.head = None

	def add_book(self, book: Book):
		if (self.head == None):
			self.head = book
		else:
			current_node = self.head
			while (current_node.next != None):
				current_node = current_node.next
			current_node.next = book

	def get_books_max_year(self, year):
		current_node = self.head
		while (current_node != None):
			if (current_node.year == year):
				print(current_node.name)
			current_node = current_node.next

def execute_books():
	n = int(input())
	books = Books()
	years = [0] * 2022
	max_publish = 0
	max_year = -1
	for _ in range(0, n):
		name = input()
		writer = input()
		year = int(input())

		book = Book(name, writer, year)
		books.add_book(book)

		years[year] += 1
		if (years[year] > max_publish):
			max_publish = years[year]
			max_year = year
		elif years[year] == max_publish:
			max_year = year if max_year > year else max_year
	
	books.get_books_max_year(max_year)

if __name__ == '__main__':
	execute_books()