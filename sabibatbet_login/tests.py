from django.test import TestCase
from django.test import Client
from django.urls import resolve
from .views import index, add_session, remove_session

# Create your tests here.
class LoginUnitTest(TestCase):
	def test_login_url_is_exist(self):
		response = Client().get('/sabibatbet_login/')
		self.assertTrue(response)

	def test_login_using_index_func(self):
		found = resolve('/sabibatbet_login/')
		self.assertEqual(found.func, index)

	def test_login_remove_session(self):
		response = Client().get('/sabibatbet_login/remove-session/')
		self.assertIsNotNone(response)
