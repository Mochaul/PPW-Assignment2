from django.test import TestCase
from django.test import Client
from django.urls import resolve
from .views import index, add_session, remove_session

# Create your tests here.
class LoginUnitTest(TestCase):
	def test_lab_8_url_is_exist(self):
		response = Client().get('/sabibatbet-login/')
		self.assertTrue(response)

	def test_lab8_using_index_func(self):
		found = resolve('/sabibatbet_login/')
		self.assertEqual(found.func, index)