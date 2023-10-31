'''
Anwar Moubakir
Luke Ross
Youssef Abdelaziz
10/31/2023

CIS 121 Project -- Digital Book Library
'''

#Book class with defining attributes
class Book:
	def __init__(self, name, author, publisher, date_published, num_pages):
		self.name = name
		self.author = author
		self.publisher = publisher
		self.date_published = date_published
		self.num_pages = num_pages
