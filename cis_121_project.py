'''
Anwar Moubakir
Luke Ross
Youssef Abdelaziz
10/31/2023

CIS 121 Project -- Digital Book Library
'''

#Book class with defining attributes
class Book:
	def __init__(self, name, author, date_published, genre):
		self.name = name
		self.author = author
		self.date_published = date_published
		self.genre = genre

	#Book 'getters'
	def get_name(self):
		return self.name
		
	def get_author(self):
		return self.author
		
	def get_date(self):
		return self.date_published
		
	def get_genre(self):
		return self.genre
		
#List of functions
def add_book(book):
	''' This function adds books of a given library '''
	library = open("book_library.txt", 'a')
	newbook_name = book.get_name()
	newbook_author = book.get_author()
	newbook_date = book.get_date()
	newbook_genre = book.get_genre()
	library.write(f'{newbook_name}\t{newbook_author}\t{newbook_date}\t{newbook_genre}\n')
	library.close()

def sort_books(method):
	''' This function sorts books of a given library file with a given method. Methods: alphabet, author, date, genre '''
	if method == 'alphabet':
		library = open("book_library.txt", 'w+')
		##WIP
		
#Initial question sequence
print("What do you want to do?")
print("add - Add a book")
print("sort - Sort the books")
user_task = input()

#Task loop
while user_task != 'quit':
	if user_task == 'add':
		user_book_name = input("Book name: ")
		user_book_author = input("Author: ")
		user_book_date = input("Year published (YYYY): ")
		user_book_genre = input("Genre: ")
		
		newbook = Book(user_book_name, user_book_author, user_book_date, user_book_genre)
		
		add_book(newbook)

	elif user_task == 'sort':
		print("How do you want to sort it?")
		print("alphabet")
		print("author")	
		print("date")
		print("genre")
					
		user_method = input()
		
		sort_books(user_method)
	
	#Return to question sequence
	print("What do you want to do?")
	print("add - Add a book")
	print("sort - Sort the books")
	user_task = input()
