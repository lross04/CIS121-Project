'''
Anwar Moubakir
Luke Ross
Youssef Abdelaziz
10/31/2023

CIS 121 Project -- Digital Book Library Classes and Functions
'''

#I moved the classes and function into their own file to clean
#things up and make them look nicer

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
	''' This function adds a given book to the book library '''
	library = open("book_library.csv", 'a')
	newbook_name = book.get_name()
	newbook_author = book.get_author()
	newbook_date = book.get_date()
	newbook_genre = book.get_genre()
	library.write(f'{newbook_name},{newbook_author},{newbook_date},{newbook_genre},\n,')
	library.close()

def find_book(method):
	''' This function returns books within the library given a category. Categories: name, author'''
	if method == 'name':
		user_find_name = input("Enter the book name (Eaxact): ")
		lib_file = open("book_library.csv")
		library = lib_file.read()
		library = library.split(",") #Split all items in the library by comma
		token = 1
		for title in library:
			if user_find_name == title:
				return f"{title}, {library[token]}, {library[token+1]}, {library[token+2]}\n"
			token += 1
		library.close()
		return "Could not find book\n"
		
	elif method == 'author':
		user_input = input("Enther the name of the author: ")
		library = open("book_library.csv")
		book_list = library.read()
		book_list = book_list.split(',')
		token = 0
		is_in = False
		for i in book_list:
			if user_input == i:
				is_in = True
				print(book_list[token-1].strip())
			token += 1
		if is_in == True:
			return "\n"
		elif is_in == False:
			return"Could not find author\n"
			
	elif method == 'year':
		user_find_year = input("Enter the publication year: ")
		lib_file = open("book_library.csv")
		library = lib_file.read()
		library = library.split(",")
		token = 1
		book_with_year = False
		for year in library:
			if user_find_year == year:
				if book_with_year == False:
					print(f"Here are the books we have from {user_find_year}")
				print(f"{library[token-3]}, {library[token-2]}, {year}, {library[token]}")
				book_with_year = True
			token += 1
		if book_with_year == True:
			library.close()
			return ""
		else:
			library.close()
			return "There are no books in the library that were published in that year.\n"
