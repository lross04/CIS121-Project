'''
Anwar Moubakir
Luke Ross
Youssef Abdelaziz
10/31/2023

CIS 121 Project -- Digital Book Library

'''
from cis_121_project_classes_and_functions import *


		
#Initial question sequence
print("What do you want to do?")
print("add - Add a book")
print("find - Find a book")
print("quit - Quit")
print()
user_task = input()

#Task loop
while user_task != 'quit':
	if user_task == 'add' or user_task == 'Add':
		user_book_name = input("Book name: ")
		user_book_author = input("Author: ")
		user_book_date = input("Year published (YYYY): ")
		user_book_genre = input("Genre: ")
		
		newbook = Book(user_book_name, user_book_author, user_book_date, user_book_genre)
		
		add_book(newbook)

	elif user_task == 'find':
		print("How do you want to look for your book?")
		print("name - By name")
		print("author - By author")	
		print("year - By year published")
		print()
					
		user_method = input()
		
		print(find_book(user_method))
	
	#Return to question sequence
	print("What do you want to do?")
	print("add - Add a book")
	print("find - Find a book")
	print("quit - Quit")
	print()
	user_task = input()
