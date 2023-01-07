import os
import json
import pprint as pp
import requests
from dotenv import load_dotenv
load_dotenv()

class BookData:
    def __init__(self, title, author, publisher):
        self.title = title
        self.author = author
        self.publisher = publisher

    def __str__(self):
        return f"\nTitle: {self.title}\nAuthor: {self.author}\nPublisher: {self.publisher}\n"

class ReadingList:
    def __init__(self, name_of_list):
        self.name_of_list = name_of_list
        
    def add_to_reading_list(self, book):
        self.reading_list = []
        self.reading_list.append(book)

    def __str__(self):
        results = ''
        print(self.name_of_list)

        for i, book in enumerate(self.reading_list):
            i += 1
            results += f'{i}. {book}\n'
        
        return results

class GoogleBooksAPI:  
    def __init__(self):
        self.book_results = []     
    
    def get_books_from_api(self, query):
        maxResults = 5
        api_key = os.environ['API_KEY'] 
        api_endpoint = f"https://www.googleapis.com/books/v1/volumes?q={query}+intitle:{query}&maxResults={maxResults}&key={api_key}" 
        response = requests.get(api_endpoint) 

        if response.status_code == 200:
            if response.json()['totalItems'] == 0:
                print(f"No search results for query '{query}'.")
            else: 
                search_results = response.json()['items']
                
            try:
                for data in search_results:
                    volume_info = data['volumeInfo']
                    title = volume_info['title']
                    publisher = volume_info['publisher']
                    author = volume_info['authors'][0]
                    book = BookData(title, author, publisher)
                    self.book_results.append(book)
            except Exception as e:
                print(str(e))

    def __str__(self):
        results = ''
        
        for book in self.book_results:
            results += f"{book}"
        
        return results

class CommandLineInterface:
    def __init__(self):
        pass



## TESTING BOOK DATA ##
# book = BookData('Harry Potter & the Sorceror\'s Stone', 'J.K. Rowling', 'JKPublishings')
# print(book.title)
# print(book.author)
# print(book.publisher)

## TESTING READING LIST ##
# list_class = ReadingList('\n== Reading List ==\n')
# list_class.add_to_reading_list('Harry Potter & the Goblet of Fire')
# print(list_class.reading_list) 
# print(list_class) 

## TESTING GOOGLE BOOKS API ##
# api = GoogleBooksAPI()
# api.get_books_from_api(query='Harry Potter')
# print(api)
