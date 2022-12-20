import os
from dotenv import load_dotenv
import requests
import pprint as pp

load_dotenv()

# def test_API():
    # query = "Harry Potter" # Tests query variable in endpoint for later usage w/ user input
    # api_key = os.environ['API_KEY'] # API key secured in .env file and placed in .gitignore, accessible through the os module
    # api_endpoint = f"https://www.googleapis.com/books/v1/volumes?q={query}&key={api_key}" # api endpoint for basic google books search queries
    # response = requests.get(api_endpoint) # HTTP Get Request using the api_endpoint as the url w/ the search query and api_key variable included

    # try: 
    #     if response.status_code == 200: # Ensure status code is OK
    #         volume_info = response.json()['items'][0]['volumeInfo'] # Testing Accessibility Here - syntax to destructure json items object, destructure from array, access volumeInfo for one singular book                                                         
            # pp.pprint({"Request Success": "JSON object displayed below."}) # If try successful, will print request success message to the console.
            # pp.pprint(volume_info) # Displays singular JSON formatted volumeInfo object.
    # except Exception as e:
        # print(f"Error!: {str(e)}") # Exception raised if request error found.

# test_API()

def search_books():
    search_query = input("Hello! Welcome to the Google Bookstore.\nEnter a book to search for:\n")
    if not search_query:
        print("Please try to enter your search again!\n")
        search_books()
    else:
        print(f"\nTop 5 related books for: '{search_query}'")
    
    api_key = os.environ['API_KEY'] # API key secured in .env file and placed in .gitignore, accessible through the os module
    api_endpoint = f"https://www.googleapis.com/books/v1/volumes?q={search_query}+intitle:{search_query}&key={api_key}" # api endpoint for basic google books search queries
    response = requests.get(api_endpoint) # HTTP Get Request using the api_endpoint as the url w/ the search query and api_key variable included
    
    if response.status_code == 200:
        data = response.json()['items']

        for book in data:
            volume_info = book['volumeInfo']
            title = volume_info['title']
            publisher = volume_info['publisher']
            author_lists = volume_info['authors']
            print(author_lists)
            
            # TODO: LOOP THROUGH THE LIST OF AUTHORS. WANT TO DISPLAY WHETHER OR NOT EACH BOOK HAS ONLY 1 AUTHOR OR MORE THAN 1 AUTHOR
            # for i, author in enumerate(author_lists):
                
                # if 
                #     print(f'Author {i + 1}: {author}')
                #     authors = f'Author: {author}'
                #     print(f"1 author: {authors}")
                # elif i > 1:
                #     authors = f'Author {i}: {author}'
                #     print(f"More than 1 author: {authors}")
                    
                    # print(f"\nTitle: {title}\n{authors}\nPublisher: {publisher}\n")
            
        # book_information = list(filter(data))
        

search_books()