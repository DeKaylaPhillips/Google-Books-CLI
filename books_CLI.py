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
    
    if response.status_code == 200: # if request to api_endpoint successful
        data = response.json()['items'] # retrieve the "items" in the Json object containing the book data

        for book in data: # iterate through all book information retrieved from the data
            volume_info = book['volumeInfo'] # volumeInfo obj will hold all necessary information to be displayed to the user on the CLI
            title = volume_info['title'] # grabs each title contained in the volumnInfo object  
            publisher = volume_info['publisher'] # grabs each publishing company's name from the volumeInfo object
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

            print(f"\nTitle: {title}\n{author}\nPublisher: {publisher}\n")
            
search_books()