'''
Anwar Moubakir
Luke Ross
Youssef Abdelaziz
10/31/2023

CIS 121 Project -- Digital Book Library

'''
from cis_121_project_classes_and_functions import *

user_task = ""
options = ('add', 'find', 'quit', 'list')

while user_task not in options:
	#Initial question sequence
	print("What do you want to do?")
	print("add - Add a book")
	print("find - Find a book")
	print("list - List all books")
	print("quit - Quit")
	print()
	user_task = input()
	if user_task not in options:
		print("Input not recognized")
		input("Press enter to continue\n")

#Task loop
while user_task != 'quit':
	#Command line for calling the 'add' function
	if user_task == 'add' or user_task == 'Add':
		user_book_name = input("Book name: ")
		user_book_author = input("Author: ")
		user_book_date = input("Year published (YYYY): ")
		user_book_genre = input("Genre: ")
		
		newbook = Book(user_book_name, user_book_author, user_book_date, user_book_genre)
		
		add_book(newbook)
	
	#Command line for calling the 'find' function
	elif user_task == 'find' or user_task == 'Find':
		print("How do you want to look for your book?")
		print("title - By title")
		print("author - By author")	
		print("year - By year published")
		print("genre - By genre\n")
					
		user_method = input()
		
		print(find_book(user_method))
		
	#Command line for calling the 'list' function
	elif user_task == 'list' or user_task == 'List':
		print("What would you like to list?")
		print("title - List titles in the library")
		print("author - List authors in the library")
		print("year - List years published in the library")
		print("genre - List genres in the library\n")
		method = input()
		print()
		if method == 'title':
			print("---Here are all of the titles currently in the library---")
			print(library_list(method))
		elif method == 'author':
			print("---Here are all of the authors currently in the library---")
			print(library_list(method))
		elif method == 'year':
			print("---Here are all of the published years currently in the library---")
			print(library_list(method))
		elif method == 'genre':
			print("---Here are all of the genres currently in the library---")
			print(library_list(method))

	
	#Return to question sequence
	input("Press enter to continue...\n")
	print("What do you want to do?")
	print("add - Add a book")
	print("find - Find a book")
	print("list - List all books")
	print("quit - Quit")
	print()
	user_task = input()
