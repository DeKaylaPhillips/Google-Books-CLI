Simple command line application using Google Books API to search for books and construct a reading list.

**Features:**
- Display 5 books matching a query 
- Display each book's author, title, and publishing company 
- Select a book from the displayed books to save to personal Reading Lis 
- View a Reading List with all books the user has selected from their queries 

**Setup/Installation Notes:**
- ***Google Books API***
  > User must create a Google Project with the **Google Books API** and generate an API key (*API calls are limited.*).

- ***.env File***
  > Add user API key as a string value to the `API_KEY=` variable in the provided **.env** file.

- ***requirements.txt file***
  > Install all dependencies from the **requirements.txt** file for proper program functionality.
  > Enter the following command in the root directory: 

        `$ pip install -r requirements.txt` or `pip3 install -r requirements.txt`

- ***Running Unit Tests***
  > To run unit tests in the tests.py file, first ensure CommandLineInterface class is not instantiated within the BookCLI.py file. You can comment out the line below:

        `# interface = CommandLineInterface()`

  > Enter the following command in the root directory:

        `python -m unittest` or `python3 -m unittest`

- ***How to Run the Interface***
  > Refactored interface in BookCLI.py file. To run the application, first ensure the CommandLineInterface class is instantiated with the BookCLI.py file. Look for this line near the bottom of the file:

        `interface = CommandLineInterface()`
    
  > Enter the following command in the root directory:

        `python BookCLI.py` or `python3 BookCLI.py`