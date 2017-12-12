from django.test import TestCase
from django.test import Client
from django.urls import resolve
from .views import index

# Create your tests here.
class sabibatbetProfileUnitTest(TestCase):
	def test_sabibatbet_profile_url_is_exist(self):
		response = Client().get('/sabibatbet-profile/')
		self.assertEqual(response.status_code, 200)

	#def test_lab7_using_index_func(self):
		#found = resolve('/sabibatbet-profile/')
		#self.assertEqual(found.func, index)
