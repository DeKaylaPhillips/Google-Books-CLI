import os
import requests
from dotenv import load_dotenv
load_dotenv()

reading_list = [] # Global variable 'reading_list' initialized as an empty list to store and maintain books when added.

class BookData: # This class stores and formats book data to be displayed.
    def __init__(self, book_id, title, author, publisher):
        self.id = book_id
        self.title = title 
        self.author = author
        self.publisher = publisher

    def __str__(self): # Displays each book's details in format of a numbered list from 1-5.
        return f"\n{self.id}. Title: {self.title}\nAuthor: {self.author}\nPublisher: {self.publisher}\n"


class ReadingList:  # This class creates a reading list when a user opts in to add a book to their list.
    def __init__(self, name_of_list):
        self.name_of_list = name_of_list # Title displayed when ReadingList class is called.
        self.reading_list = reading_list # Attribute value is the global reading list.

    def add_to_reading_list(self, book): # This method adds the book a user has selected to the reading list.
        self.reading_list.append(book) 

    def __str__(self): # Displays the title of the reading list, and iterates through the reading list to display and number each book that has been added to the list.
        print(self.name_of_list)
        book_in_reading_list = ''

        for i, book in enumerate(self.reading_list):
            i += 1
            book_in_reading_list += f'{i}. {book}\n' 
        return book_in_reading_list


class GoogleBooksAPI: # This class parses through and handles the data from the Google Books API.
    def __init__(self):
        self.book_results = [] 
        self.book_results_list = []
    
    def get_books_from_api(self, query):
        # Google Books API information.
        maxResults = 5
        api_key = os.environ['API_KEY'] 
        api_endpoint = f"https://www.googleapis.com/books/v1/volumes?q={query}+intitle:{query}&maxResults={maxResults}&key={api_key}" 
        response = requests.get(api_endpoint) 
        
        # Handling the response from the API call.
        if response.status_code == 200:
            if response.json()['totalItems'] == 0: # Search query did not match a keyword affiliated with a book in the API.
                print(f"\nNo search results for query '{query}'.")
                CommandLineInterface.main_menu(self)
            
            search_results = response.json()['items']
            for i, data in enumerate(search_results): # Iterates through the API data and assigns relevant information to variables to be passed into the BookData class.
                i += 1
                book_id = i
                volume_info = data['volumeInfo']
                title = volume_info['title']
                author = volume_info['authors'][0]
                publisher = volume_info.get('publisher', "Unknown") # Default value "unknown" assigned to publisher information not available.
                
                book = BookData(book_id, title, author, publisher) # Instantiates the BookData class.
                self.book_results.append(book) # Appends data received by the BookData class to the book_results in the formatting specified by the BookData's string dunder method.
                self.book_results_list.append({'id': book_id, 'title': title, 'author': author}) # Appends dictionary of book data to the book_results_list for selecting a book to add to the reading list.

    def __str__(self): # Converts memory addresses to strings to display the top 5 books in the format defined in the BookData class.
        book_matches = '' 

        for book in self.book_results: 
            book_matches += f"{book}"
        return book_matches


class CommandLineInterface: # This class handles user input and passes it the the necessary instance methods to display information based on user selections.
    def __init__(self):
        self.main_menu()
    
    def main_menu(self): # Displays the start-up prompt and takes in a search query from the input.
        print("\n== Welcome to Google Books ==")
        query = input("\nEnter a book title or keyword to search.\nEnter (E!) to exit the interface.\n\n")

        if query == "E!" or query == "e!": # User opts to exist the interface.
            print("\n== Thank you! Exiting the Google Books Interface. ==\n")
            exit()

        return self.search_results(query=query) # Passes a user's query to the .search_results() method.

    def search_results(self, query): # Displays the results of a search query.
        if not query: # User did not enter a search string or opt to exit the interface.
            print('\n== No title or keyword entered. ==\n')
            self.main_menu()
        
        api = GoogleBooksAPI() # Instantiates the GoogleBooksAPI class.
        api.get_books_from_api(query=query) # Parses API data to return search results based on the user's search query.
        print(f"\n== Search Results for '{query}' ==") 
        print(api)
        return self.select_book(search_results=api.book_results_list) # Passes the list of dictionaries containing book results to the select_book() instance method.

    def select_book(self, search_results): # Displays a prompt that allows the user to select a book from their query results or return to main menu to make a new search.
        add_to_list = input("Would you like to add a book to your reading list? Enter (Y) for Yes or (N) for No.\n")

 
        if add_to_list == 'N' or add_to_list == 'n': # Returns a user to the main menu to either create a new search query or exit the interface.
            self.main_menu()
        
        elif add_to_list == 'Y' or add_to_list == 'y': # Displays reading list if input value matches a book from search query results.
            book_selection = input("\nEnter the number of the book you'd like to add to the list: \n")

            if book_selection.isalpha() or not book_selection or int(book_selection) not in range(1, 6): # Selection was not a valid input choice ranging from numbers 1-5.
                print("\n== Sorry, that was an invalid selection. ==\n")
                self.main_menu()
            
            for book in search_results: # Adds user's selected book to their reading list.
                if str(book['id']) == book_selection:
                    user_reading_list = ReadingList("\n== Reading List ==\n")
                    user_reading_list.add_to_reading_list(f"{book['title']} by {book['author']}")
                    print(f"\n'{book['title']}' by {book['author']} has been added to your reading list.\n")
                    return self.view_reading_list(reading_list=user_reading_list) # Passes the user's reading list to the .view_reading_list() instance method.
        
        # Selection was not a valid input for the yes or no option choices.
        print("\n== Sorry, that was an invalid selection. ==\n")
        self.main_menu()
    
    def view_reading_list(self, reading_list): # Displays a prompt for a user to either view their reading list or return to the main menu.
        view_list = input("\nEnter (1) to view your reading list or (2) to return to the main menu.\n")
                    
        if view_list == str(1): # Displays the books currently in the user's reading list.
            print(reading_list)
            self.main_menu()
        
        elif view_list == str(2): # Returns user to the main menu.
            self.main_menu()
        
        # Selection was not a valid input option (1 or 2).
        print("\n== Sorry, that was an invalid selection. ==\n")
        self.main_menu()

## INTERFACE
interface = CommandLineInterface()

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
