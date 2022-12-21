import os
import requests
from dotenv import load_dotenv
load_dotenv()
# import pprint as pp

reading_list = [] 

def search_books():
    search_query = input("Hello! Welcome to the Google Bookstore.\nEnter a book to search for:\n")
    
    if not search_query:
        print("Please try to enter your search again!\n")
        search_books()
    
    elif search_query and type(str(search_query)):
        print(f"\nTop 5 Books Related to: '{search_query}'")
    
    maxResults = 5
    api_key = os.environ['API_KEY'] 
    api_endpoint = f"https://www.googleapis.com/books/v1/volumes?q={search_query}+intitle:{search_query}&maxResults={maxResults}&key={api_key}" 
    response = requests.get(api_endpoint) 

    if response.status_code == 200: 
        data = response.json()['items'] 

        for i, book in enumerate(data): 
            i = i + 1
            
            volume_info = book['volumeInfo'] 
            title = volume_info['title'] 
            publisher = volume_info.get('publisher', 'Not Available')
            author_lists = volume_info['authors'] 
            num_of_authors = len(author_lists) 
            
            authors = [] 
            
            if num_of_authors > 1: 
                for i, author in enumerate(author_lists): 
                    i = i + 1 
                    authors.append(f"Author {i}: {author}") 
                    author = '\n'.join(authors) 
            
            elif num_of_authors == 1: 
                for author in author_lists: 
                    author = (f"Author: {author}") 

            query_results = f"\n{i}. {title}\n{author}\nPublisher: {publisher}\n"
            print(query_results)

        selection = input("Enter a book number to add it to your reading list.\n")
        
        if not selection or int(selection) < 1 or int(selection) > 5:
            print("Invalid book number. Please try your search again!\n")
            search_books()
        
        else:
            selected_book_title = data[int(selection) - 1]['volumeInfo']['title']
            reading_list.append(selected_book_title)
            print(f"\nSuccessfully added {selected_book_title} to your Reading List!\n")
            menu_options(reading_list)

def menu_options(reading_list):
    menu_selection = input("Enter (1) to search for more books.\nEnter (2) to view your reading list.\n")
    
    if not menu_selection:
        print("No menu selection. Returning to search.\n")
        search_books()
    
    elif menu_selection and int(menu_selection) == 1:
        print("Returning to search interface.\n")
        search_books()
    
    elif menu_selection and int(menu_selection) == 2:
        reading_list = '\n'.join(reading_list)
        print(f"Reading List:\n\n{reading_list}\n")
        search_books()
                
search_books()