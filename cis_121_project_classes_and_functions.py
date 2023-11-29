'''
Anwar Moubakir
Luke Ross
Youssef Abdelaziz
10/31/2023

CIS 121 Project -- Digital Book Library Classes and Functions
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
	''' This function adds a given book to the book library '''
	library = open("book_library.csv", 'a')
	newbook_name = book.get_name()
	newbook_author = book.get_author()
	newbook_date = book.get_date()
	newbook_genre = book.get_genre()
	library.write(f',{newbook_name},{newbook_author},{newbook_date},{newbook_genre},\n,')
	library.close()

def find_book(method):
	''' This function returns books within the library given a category. Categories: name, author, year'''
	if method == 'title':
		user_find_name = input("Enter the title of the book you're looking for (Eaxact): ")
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
		user_input = input("Enther the name of the author you're looking for: ")
		library = open("book_library.csv")
		book_list = library.read()
		book_list = book_list.split(',')
		token = 0
		is_in = False
		books = []
		for i in book_list:
			if user_input == i:
				is_in = True
				books.append(book_list[token-1].strip())
			token += 1
		if is_in == True:
			print(f"---Here are the books we have from {user_input}---")
			for i in books:
				print(i)
			return ''
		elif is_in == False:
			return"Could not find author\n"
			
	elif method == 'year':
		find_year = input("Enter the publication year you're looking for: ")
		lib_file = open("book_library.csv")
		library = lib_file.read()
		library = library.split(",")
		token = 1
		book_with_year = False
		for year in library:
			if find_year == year:
				if book_with_year == False:
					print(f"---Here are the books we have from {find_year}---")
				print(f"{library[token-3]}, {library[token-2]}, {year}, {library[token]}")
				book_with_year = True
			token += 1
		if book_with_year == True:
			return ""
		else:
			return "There are no books in the library that were published in that year.\n"
			
	elif method == 'genre':
		find_genre = input("Enter the genre you're looking for: ")
		lib_file = open("book_library.csv")
		library = lib_file.read()
		library = library.split(",")
		library.pop(0)
		token = 2
		book_with_genre = False
		for genre in library:
			if find_genre == genre.strip():
				if book_with_genre == False:
					print(f"---Here are the books we have from the {find_genre} genre---")
				print(f"{library[token-5]}, {library[token-4]}, {library[token-3]}, {genre.strip()}")
				book_with_genre = True
			token += 1
		if book_with_genre == True:
			return ""
		else:
			print(library)
			return "There are no books in the library with that genre\n"
			
def library_list(method):
	if method == "title":
		lib_file = open('book_library.csv')
		library = lib_file.read().split(',')
		library.pop(0)
		token = 0
		for item in library:
			if token % 4 == 0:
				print(library[token])
			token += 1
		return ''
	
	elif method == "author":
		lib_file = open('book_library.csv')
		library = lib_file.read().split(',')
		library.pop(0)
		library.pop(0)
		token = 0
		author_names = []
		for item in library:
			if token % 4 == 0:
				if item not in author_names:
					print(library[token])
				author_names.append(item)
			token += 1
		return ''
		
	elif method == "year":
		lib_file = open('book_library.csv')
		library = lib_file.read().split(',')
		for i in range(3):
			library.pop(0)
		token = 0
		years = []
		for item in library:
			if token % 4 == 0:
				if item not in years:
					print(library[token])
				years.append(item)
			token += 1
		return ''
		
	elif method == "genre":
		lib_file = open('book_library.csv')
		library = lib_file.read().split(',')
		for i in range(4):
			library.pop(0)
		token = 0
		genres = []
		for item in library:
			if token % 4 == 0:
				if item not in genres:
					print((library[token].strip()))
				genres.append(item)
			token += 1
		return ''
			
