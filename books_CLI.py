import os

import requests
import pprint as pp
from dotenv import load_dotenv
load_dotenv()

reading_list = [] 

def search_books():
    search_query = input("Hello! Welcome to the Google Bookstore.\nEnter a book to search for:\n")
    if not search_query:
        print("Please try to enter your search again!\n")
        search_books()
    else:
        print(f"\nTop 5 Books Related to: '{search_query}'")
    
    api_key = os.environ['API_KEY'] # API key secured in .env file and placed in .gitignore, accessible through the os module
    maxResults = 5
    api_endpoint = f"https://www.googleapis.com/books/v1/volumes?q={search_query}+intitle:{search_query}&maxResults={maxResults}&key={api_key}" # api endpoint for basic google books search query - searches to ensure query is in title, cli displays only 5 results, and api_key included in endpoint
    response = requests.get(api_endpoint) # HTTP Get Request using the api_endpoint as the url w/ the search query and api_key variable included

    if response.status_code == 200: # if request to api_endpoint successful
        data = response.json()['items'] # retrieve the "items" in the Json object containing the book data

        for i, book in enumerate(data): # iterate through all book information retrieved from the data
            i = i + 1
            volume_info = book['volumeInfo'] # volumeInfo obj will hold all necessary information to be displayed to the user on the CLI
            title = volume_info['title'] # grabs each title contained in the volumnInfo object  
            publisher = volume_info.get('publisher', 'Not Available')
            # publisher = volume_info['publisher'] # grabs each publishing company's name from the volumeInfo object
            author_lists = volume_info['authors'] # grabs each list of authors from the volumeInfo object
            num_of_authors = len(author_lists) # used to find out which books have multiple or only one author 
            
            authors = [] # initiates authors variable to a list that will contain a authors who contributed to multiple books and their enumerated value/author string
            if num_of_authors > 1: # if there is more than one author in each author list
                for i, author in enumerate(author_lists): # iterate over the author list containing more than one author
                    i = i + 1 # do not want the author's count to begin counting from 0, so i + 1
                    authors.append(f"Author {i}: {author}") # each author and their associated number/string will be inserted into the authors list 
                    author = '\n'.join(authors) # assigns the value of author to string values printed on top of one another (\n) which will display both authors and there their associated number
            
            elif num_of_authors == 1: # else if there is only one author in the list of authors
                for author in author_lists: # iterate over each singular author 
                    author = (f"Author: {author}") # author is assigned the value of each singular author and will no longer be displayed in list format

            query_results = f"\n{i}. {title}\n{author}\nPublisher: {publisher}\n"
            print(query_results)
   
        selection = input("Enter a book number to add it to your reading list.\n")
        if not selection or int(selection) < 1 or int(selection) > 5:
            print("Invalid book number. Please try your search again!\n")
            search_books()
        else:
            selected_book_title = data[int(selection) - 1]['volumeInfo']['title']
            reading_list.append(selected_book_title)
            print(f"Successfully added {selected_book_title} to your Reading List!\n")

        menu_options(reading_list)

def menu_options(reading_list):
    menu_selection = input("Enter 1 to search for more books. Enter 2 to view your reading list!\n")
    if not menu_selection:
        print("No menu selection. Returning to search.\n")
        search_books()
    elif menu_selection and int(menu_selection) == 1:
        print("Returning to search interface.\n")
        search_books()
    elif menu_selection and int(menu_selection) == 2:
        print(f"Reading List:\n{reading_list}\n")
                
search_books()