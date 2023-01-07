import unittest
from BookCLI import BookData, ReadingList, GoogleBooksAPI

class TestBookData(unittest.TestCase):
    def test_0_test_constructor(self):
        book_data_obj = BookData(title='Harry Potter & the Chamber of Secrets', author='J.K. Rowling', publisher='JKPublishings')
        
        self.assertEqual(book_data_obj.title, 'Harry Potter & the Chamber of Secrets')
        self.assertEqual(book_data_obj.author, 'J.K. Rowling')
        self.assertEqual(book_data_obj.publisher, 'JKPublishings')

class TestReadingList(unittest.TestCase):
    def test_1_add_to_reading_list(self):
        reading_list_obj = ReadingList('== Reading List ==') 
        book_data_obj = BookData(title='Harry Potter & the Chamber of Secrets', author='J.K. Rowling', publisher='JKPublishings')
        reading_list_obj.add_to_reading_list(book_data_obj)
        
        self.assertEqual(len(reading_list_obj.reading_list), 1)
        self.assertEqual(reading_list_obj.name_of_list, '== Reading List ==')
        self.assertEqual(reading_list_obj.reading_list[0], book_data_obj)

class TestGoogleBooksAPI(unittest.TestCase):
    def test_2_get_books_from_api(self):
        api_obj = GoogleBooksAPI()
        api_obj.get_books_from_api(query='Harry Potter')
        self.assertEqual(len(api_obj.book_results), 5)
        # api_obj.get_books_from_api(query='boopbeebopbow_')  

if __name__ == '__main__':
    unittest.main(verbosity=True)