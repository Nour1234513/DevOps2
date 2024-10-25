'''
   WRITE YOUR NAME HERE!
   Nour Alnajar
'''

import sys
import os
import pytest
from book_store_client.client import Client
from book_store_client.api.actions import add_book
from book_store_client.api.actions import list_books
from book_store_client.models.book_request_response_model import BookRequestResponseModel
from book_store_client.api.actions import reset_test_data
from book_store_client.api.actions import delete_book
from book_store_client.api.actions import search_book
from book_store_client.api.actions import update_book
from book_store_client.api.actions import sell_book
from book_store_client.api.actions import get_book

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Implement your tests here...
class Testexamapi():
   client = Client(base_url="http://localhost:8000")

   def test_add_book_api(self):
      reset_test_data.sync(client=self.client)

      add_book.sync(client=self.client, body=BookRequestResponseModel(name = "nour", author= "alnajjar",isbn= "121", price= 10,copies= 1))
      booklist = list_books.sync(client=self.client)
      assert booklist.__contains__(BookRequestResponseModel(name = "nour", author= "alnajjar",isbn= "121", price= 10,copies= 1))

      reset_test_data.sync(client=self.client)


   def test_delete_book_api(self):
      reset_test_data.sync(client=self.client)

      delete_book.sync(client=self.client, isbn="9781853260629")
      booklist = list_books.sync(client=self.client)
      assert not booklist.__contains__(BookRequestResponseModel(name='War and Peace', author='Leo Tolstoy', isbn='9781853260629', price=12.99, copies=6))

      reset_test_data.sync(client=self.client)

   def test_search_book_api(self):
      book = BookRequestResponseModel(name='War and Peace', author='Leo Tolstoy', isbn='9781853260629', price=12.99, copies=6)
      reset_test_data.sync(client=self.client)

      res = search_book.sync(client=self.client, name= book.name,author= book.author)
      assert res.__contains__(book)
      res.clear()

      res = search_book.sync(client=self.client,name = book.name )
      assert res.__contains__(book)
      res.clear()

      res = search_book.sync(client=self.client, author= book.author)
      assert res.__contains__(book)

      reset_test_data.sync(client=self.client)

   def test_Edit_book_api(self):
      ##BookRequestResponseModel(name='War and Peace', author='Leo Tolstoy', isbn='9781853260629', price=12.99, copies=6)
      reset_test_data.sync(client=self.client)

      update_book.sync(client=self.client, isbn="9781853260629", body=BookRequestResponseModel(name='nour', author='najjar', isbn='963', price=1000, copies=1))
      assert get_book.sync(client=self.client, isbn="963") == BookRequestResponseModel(name='nour', author='najjar', isbn='963', price=1000, copies=1)

      reset_test_data.sync(client=self.client)

   def test_sell_book_api(self):
      reset_test_data.sync(client=self.client)

      sell_book.sync(client=self.client, isbn="9781853260629")
      assert get_book.sync(client=self.client, isbn="9781853260629").copies == 5

      sell_book.sync(client=self.client, isbn="9781853260629")
      assert get_book.sync(client=self.client, isbn="9781853260629").copies == 4

      sell_book.sync(client=self.client, isbn="9781853260629")
      assert get_book.sync(client=self.client, isbn="9781853260629").copies == 3

      reset_test_data.sync(client=self.client)








   